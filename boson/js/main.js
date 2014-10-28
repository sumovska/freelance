/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	var imageCarousel = $('.image-carousel .carousel');
	imageCarousel.bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 276,
		minSlides: 6,
		maxSlides: 6,
		slideMargin: 52,
		moveSlides: 1
	});

	
});
