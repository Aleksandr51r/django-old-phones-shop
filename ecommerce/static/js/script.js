


document.addEventListener('DOMContentLoaded', () => {


    // nav burger 
    const links = document.querySelectorAll('.header__nav-link')
    const menu = document.querySelector('.header__nav-menu')
    const hamburger = document.querySelector('.header__hamburger')
    const linksContainer = document.querySelector('.header__links-container')
    const overlay = document.querySelector('.overlay')


    function menuToggle() {
        overlay.classList.toggle('overlay--active')
        hamburger.classList.toggle('header__hamburger--active')
        menu.classList.toggle('header__nav-menu--active')
        linksContainer.classList.toggle('header__links-container--active')
        links.forEach((link, index) => {
            setTimeout(() => {
                link.classList.toggle('header__nav-link--active')
            }, index * 50)
        })
    }

    const elements = [overlay, hamburger]

    elements.forEach((el) => {
        el.addEventListener('click', menuToggle)
    })
})
