const tl = gsap.timeline({defaults:{duration: 0.5, ease: "power3.out"}})

tl.fromTo('.cookie-container', {opacity: 0, x: -200}, {opacity: 1, x:0, duration:2})

const button = document.querySelector('button');

button.addEventListener('click',() => {
    gsap.to('.cookie-container', {opacity: 0,x: -200, duration: 0.5})
} )