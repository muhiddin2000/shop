const burger = document.querySelector('.navbar-burger')
const menu = document.querySelector('#navbarBasicExample')
burger.addEventListener('click',()=>{
    menu.classList.toggle('is-active')
})