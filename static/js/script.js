const navigationHeight = document.querySelector('.navbar').offsetHeight;

console.log(document.documentElement);

document.documentElement.style.setProperty('--scroll-padding', navigationHeight + "px");

document.querySelector('.menu-btn').addEventListener('click', () => document.querySelector('.nav-list').classList.toggle('show'));

