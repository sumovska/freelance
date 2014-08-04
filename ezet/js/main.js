/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	$('.block-content .background .carousel').bxSlider({
		pager: false,
		auto: true,
		pause: 5000,
		speed: 700,
		useCSS: false
	});
	/*$('.similar-products .ware ').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 220,
		minSlides: 4,
		maxSlides: 4,
		margin: 10
	});*/
	$('.block-products .products .ware .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 220,
		minSlides: 4,
		maxSlides: 4,
	});
	$('.block-products .recommend .ware .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 220,
		minSlides: 4,
		maxSlides: 4,
	});
})

