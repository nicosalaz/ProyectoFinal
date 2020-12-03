Feature:
  Registrarse como cliente.

  Background:
    Given ya se haya iniciado el browser.

  Scenario Outline:
  Registrarse como nuevo usuario.

    Given este en la pagina de registrar.
    When Escribe cedula "<cedula>"
    And Escribe nombre "<nom>"
    And Escribe apellido "<ape>"
    And Escribe telefono "<tel>"
    And Escribe direccion "<dir>"
    And Escribe Fecha "<fecha>"
    And escribe Usuario "<usu>"
    And Escribe clave "<pwd>"
    And se oprime el boton registrar
    Then se crea el usuario y se redirecciona a la página del login

    Examples:
      | cedula     |  | nom     |  | ape     |  | tel        |  | dir           |  | fecha      |  | usu                |  | pwd     |
      | 1193248095 |  | Nicolas |  | Salazar |  | 3006801421 |  | cll 30 #10-14 |  | 15/05/1990 |  | nicoSala@gmail.com |  | 1234568 |