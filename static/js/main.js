// There there now, its all going to be alright

(function(jquery,swiper, twlm, tmlm ,underscore, greensock, loco_scroll){




let mobile_menu = $('._jsNav');
let close_menu = $('._jsClose');
let body = $('body');
mobile_menu.on('click',(e)=>{
	e.preventDefault();
body.addClass('nav--open')
})

close_menu.on('click',(e)=>{
	e.preventDefault();
body.removeClass('nav--open')
})




})($, Swiper, TweenMax, TimelineMax, _, com['greensock'], LocomotiveScroll ) 


// console.error('inside global scope');
