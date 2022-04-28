if( socket ){
    socket.on(
        "foobar",
        function( foobar ){
            console.log( foobar );
            document.getElementById( "foobar" ).innerHTML = foobar ;
        }
    );

    socket.emit( "foobar" , "init" );
}