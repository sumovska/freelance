/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Index page carousel */
	$('.slider .carousel').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		/*auto: true,*/
		speed: 700,
		pager: false,
		slideWidth: 1260,
		minSlides: 1,
		moveSlides: 1
	});
});