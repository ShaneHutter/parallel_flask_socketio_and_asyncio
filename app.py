#!/usr/bin/env python3
"""Unix Socket to Flask SocketIO

* Create a two way unix socket pair for a ctl program to communicate with a running flask app
* Listening on the socket in the app will require a nonblocking async function
* Goals for proof of concept
    * issue a command to list all clients viewing site, providing client side details
    * Send a string to the browser console by running a command on the cli of the host
    * Dynamically load scripts, or change site details via the cli
"""

from eventlet   import monkey_patch
monkey_patch()

from asyncio    import start_unix_server, coroutine , run

from threading  import Thread

from flask          import Flask, render_template
from flask_socketio import SocketIO
from flask_session  import Session
from flask_compress import Compress


### App setup
app = Flask(
    __name__,
    static_url_path = "",
    )
Session( app )
Compress( app )


# Socket IO setup
socketio = SocketIO(
    app,
    async_mode = 'eventlet',
    engineio_logger = True,
    )


# Serverside SocketIO
@socketio.on( "foobar" )
def handle_cmd( foobar ):
    socketio.emit( "foobar" , foobar , broadcast = True )


# Async Unix socket listen
@coroutine
def usock_listen( r_sock , w_sock ):
    _ret = ""
    while True:
        _recv = yield from r_sock.read(4)
        if not _recv:
            break
        _ret += _recv.decode()
    handle_cmd( _ret )


async def start_usock():
    usock_srv = await start_unix_server( usock_listen , path = "foobar.sock" )
    async with usock_srv:
        await usock_srv.serve_forever()


# App routes
@app.route( "/" )
def index():
    return render_template( "index.jinja" )

# Main for non-prod tests
if __name__ == 'app':
    print( "gunicorn runs me" )
    Thread( target = run , args = [ start_usock() ] ).start()
    #Thread( target = socketio.run , args = [ app ] ).start()
    #socketio.run( app )