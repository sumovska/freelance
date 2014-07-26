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
});