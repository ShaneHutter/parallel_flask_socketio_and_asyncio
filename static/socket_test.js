if( socket ){
    socket.on(
        "cmd",
        function( cmd ){
            console.log( cmd )
        }
    )
}