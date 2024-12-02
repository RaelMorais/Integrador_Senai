import {loadCartItem,removeCartItem} from "./functions.js";
let cartItens = JSON.parse(localStorage.getItem("listaCompras")) 


let pedidos = JSON.parse(localStorage.getItem("pedidos"))
if (pedidos == null){ 
    pedidos = []
}

let cartItensHTML = document.querySelector('#checkout .grid_col_1')
loadCartItem(cartItens,cartItensHTML)
removeCartItem(cartItens)




