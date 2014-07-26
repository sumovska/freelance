/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	$('.image-carousel .carousel').bxSlider({
		controls: false,
		auto: true,
		pause: 5000,
		speed: 700,
		useCSS: false
	});
	$('.block-partners .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 115,
		minSlides: 6,
    	maxSlides: 6,
    	slideMargin: 5
	});
	$('.slider-photo .screen .carousel').bxSlider({
		auto: true,
		pager: false,
		pause: 5000,
		speed: 700,
		useCSS: false
	});
	$('.slider-photo .scroll .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 115,
		minSlides: 14,
    	maxSlides: 14,
    	slideMargin: 5
	});
})