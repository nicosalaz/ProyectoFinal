  Feature:
  Comprar ya loggeado

  Background:
    Given Ya se inció el browser.
      And se loggeó correctamente.

  Scenario:
  Comprar loggeado

    Given estas en catalogo de productos.
      And Seleccionas un producto.
      And Se da click en el boton para ir al carrito.
      And se visualiza el producto seleccionado en carrito.
     When se de click en el boton de filizar comprar
     Then se realizara la compra y te mostrará el total a pagar.