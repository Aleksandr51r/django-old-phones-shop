// Класс для управления каруселью внутри одной карточки
class CarouselItem {
    constructor(card) {
        this.card = card
        this.slides = card.querySelectorAll('.article__carousel-item')
        this.current = 0
        this.prevBtn = card.querySelector('.article__prev')
        this.nextBtn = card.querySelector('.article__next')
        this.showSlide(this.current)
        this.addListeners()
    }

    showSlide(index) {
        this.slides.forEach((slide, i) => {
            slide.classList.toggle(
                'article__carousel-item--active',
                i === index
            )
        })
    }

    addListeners() {
        if (!this.prevBtn || !this.nextBtn || this.slides.length === 0) return

        this.nextBtn.addEventListener('click', (e) => {
            console.log(this.current)
            e.preventDefault()
            e.stopPropagation()
            this.current = (this.current + 1) % this.slides.length
            this.showSlide(this.current)
        })

        this.prevBtn.addEventListener('click', (e) => {
            e.preventDefault()
            e.stopPropagation()
            this.current =
                (this.current - 1 + this.slides.length) % this.slides.length
            this.showSlide(this.current)
        })
    }
}

// prettier-ignore
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.article')
    cards.forEach((card) => new CarouselItem(card))


    const searchContainer = document.getElementsByClassName('content__form-filter')[0]
    const catalog = document.getElementsByClassName('content__catalog')[0]
    const resizeButton = document.getElementsByClassName('content__filter-resize')[0]
    const search = document.getElementsByClassName('content__filter-fields')[0]
        
    function toggleFilter(e) {
        e.preventDefault()
        e.stopPropagation()
        searchContainer.classList.toggle('content__form-filter--active')
        search.classList.toggle('content__filter-fields--active')
        catalog.classList.toggle('content__catalog--filter-active')
    }
    let active = false


    function handleResize() {
        if (window.innerWidth <= 991 && !active) {
            resizeButton.addEventListener('click', toggleFilter)
            active = true
        } else if (window.innerWidth > 991 && active) {
            resizeButton.removeEventListener('click', toggleFilter)
            active = false
        }
    }

    handleResize()
    window.addEventListener('resize', handleResize) 



 
    

})
