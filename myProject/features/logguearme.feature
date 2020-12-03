Feature:
  Loggearse con un usuario existente

  Scenario Outline:
  Loggearse ya registrado.

    Given Ya se inicio el browser.
    And Esta en la pagina del login.
    When Ingresa el usuario "<usuario>" e ingresa la contraseña "<pwd>".
    And presiona al boton Iniciar sesion.
    Then aparece su nickname con un mensaje de bienvenida.
    And se cierra el browser.

    Examples:
      | usuario   | pwd       |
      | nicosalaz | n1c0l4s10 |