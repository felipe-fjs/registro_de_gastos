let menu = document.getElementById('menu-burguer')
let navbar = document.getElementById('navbar')
function menuBurguer(){
    if (window.getComputedStyle(navbar).maxHeight == '0px' || navbar.style.maxHeight == '0px') {
        navbar.style.maxHeight = '180px'
    } else {
        navbar.style.maxHeight = '0'
    }
}