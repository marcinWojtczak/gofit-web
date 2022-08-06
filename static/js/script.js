const navigationHeight = document.querySelector('.navbar').offsetHeight;


console.log(document.documentElement);

document.documentElement.style.setProperty('--scroll-padding', navigationHeight + "px");

// $('.main-nav a').on('click', function(e) {
//     if(this.hash != '') {
//         e.preventDefault();

//         const hash = this.hash;

//         $('html, body').animate(
//             {
//                 scrollTop: $(hash).offset().top
//             }, 
//             800
//         );
//     }
// });

// $('.offer a').on('click', function(e) {
//     if(this.hash != '') {
//         e.preventDefault();

//         const hash = this.hash;

//         $('html, body').animate(
//             {
//                 scrollTop: $(hash).offset().top
//             }, 
//             800
//         );
//     }
// });

// $('.team a').on('click', function(e) {
//     if(this.hash != '') {
//         e.preventDefault();

//         const hash = this.hash;

//         $('html, body').animate(
//             {
//                 scrollTop: $(hash).offset().top
//             }, 
//             800
//         );
//     }
// });

// $('.footer a').on('click', function(e) {
//     if(this.hash != '') {
//         e.preventDefault();

//         const hash = this.hash;

//         $('html, body').animate(
//             {
//                 scrollTop: $(hash).offset().top
//             }, 
//             800
//         );
//     }
// });