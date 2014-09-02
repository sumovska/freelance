
/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */


/* On document ready */
$(document).ready(function () {
	$('.image-carousel .image').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		speed: 700,
		auto: true,
		slideWidth: 1108,
		slideMargin: 22,
		minSlides: 1,
		moveSlides: 1
	});
});


/* On document ready */
$(document).ready(function () {
	$('.parts-carousel .parts').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		pager: false,
		slideWidth: 272,
		minSlides: 4,
		maxSliders: 4,
		moveSlides: 1
	});
});
