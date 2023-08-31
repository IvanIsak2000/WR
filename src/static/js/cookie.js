const tl = gsap.timeline({defaults:{duration: 0.5, ease: "power3.out"}})

tl.fromTo('.cookie-container', {opacity: 0, y: -200}, {opacity: 1, y:0, duration:2})

const cookie_accept = document.querySelector('.accept');

cookie_accept.addEventListener('click',() => {
    gsap.to('.cookie-container', {opacity: 0,x: -200, duration: 0.5})
} )


const login = document.querySelector('ckick', () =>{
    gsap.to()
})
