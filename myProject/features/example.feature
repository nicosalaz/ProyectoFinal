uiklñFeature: Publicacion de un mensaje en Facebook.
	Scenario:Publicar un mensaje en el muro de un amigo en Facebook.
    	Given ingrese a la aplicacion de facebook
        And ingrese a mi cuenta correctamente
        And busque la cuenta de mi amigo.
        When ingreso al perfil de mi amigo
        And selecciono la caja de texto.
        And escribo un mensaje en la caja de texto.
        And presiono el boton de compartir.
        Then aparece el mensaje en el muro del amigo.
