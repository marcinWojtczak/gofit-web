const navigationHeight = document.querySelector('.nav').offsetHeight;

document.documentElement.style.setProperty('--scroll-padding', navigationHeight + 'px');


const animation = [document.querySelector('.button'), document.querySelector('.menu-wrap'), document.querySelector('hamburger-btn')]

animation.forEach(function(item){
    item.addEventListener('click', () => document.querySelector('.menu-wrap').classList.toggle('show'));
    item.addEventListener('click', () => document.querySelector('.hamburger-btn').classList.toggle('change'));
    item.addEventListener('click', () => document.querySelector('.line').classList.toggle('change'));
})



