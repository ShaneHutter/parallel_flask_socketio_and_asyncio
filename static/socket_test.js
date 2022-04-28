let notify_perm;

if( socket ){
    socket.on(
        "foobar",
        function( foobar ){
            console.log( foobar );
            document.getElementById( "foobar" ).innerHTML = foobar ;
        }
    );

    socket.emit( "foobar" , "init" );

    socket.on(
        "notify",
        function( message ){
            if( Notification ){
                notify_perm = Notification.permission
                console.log( notify_perm )
                if( notify_perm = "default" ){
                    Notification.requestPermission(
                        function( permission ){
                            console.log( permission )
                            notify_perm = permission
                            if( notify_perm == "granted" ){
                                console.log( notify_perm )
                            }
                        }
                    )
                } else if( notify_perm = "granted" ) {
                    console.log( notify_perm )
                }
            }
        }
    )

}