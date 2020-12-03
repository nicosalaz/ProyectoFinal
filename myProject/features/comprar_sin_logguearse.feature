  Feature:
  Realizar un compra en una tienda online.

  Scenario:
  Comprar sin loggearse.

    Given que estas en la pagina principal
    When agregas un producto al carrito de compra
    Then te envia a la pagina del login y ves el logo de Login.
    And se cierra el browser.
