Feature:Registrarse como cliente.
  Background:
    Given Este en el registrarse.
      And tenga la informacion a pedir.

  Scenario Outline:Registrarse como nuevo usuario.
    Given este en registro.
      And tenga la informacion.
     When Escribe cedula <cedula>
      And Escribe nombre <nom>
      And Escribe apellido <ape>
      And Escribe telefono <tel>
      And Escribe direccion <dir>
      And Escribe Fecha <fecha>
      And escribe Usuario <usu>
      And Escribe clave <pass>
      And le unde boton continuar
     Then la cuenta se crea

    Examples:
      | cedula     |  | nom     |  | ape     |  | tel        |  | dir       |  | fecha   |  | usu         |  | pass    |
      | 1193248095 |  | Nicolas |  | Salazar |  | 3006801421 |  | cll 30 #10-14 |  | 90/5/84 |  | nicolasSala |  | 1234568 |

