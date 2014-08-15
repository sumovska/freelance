/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	var slider = $('.promo .carousel'), carousel;
	carousel = slider.bxSlider({
		controls: false,
		auto: true,
		autoHover: true,
		speed: 1000,
		mode: 'fade',
		useCSS: false,
		loop: false,
		adaptiveHeight: true
	});

	$('.js-scroll-top').click(function () {
		$.scrollTo(0, 500);
		return false;
	});
	$('.js-order').click(function () {
		$.scrollTo('.footer', 500);
		return false;
	});
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			carousel.destroySlider();
			carousel = slider.bxSlider({
				controls: false,
				auto: true,
				autoHover: true,
				speed: 1000,
				useCSS: false,
				loop: true,
				adaptiveHeight: true
			});
		}
	}
});