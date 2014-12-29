/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();
	
	$('.index').each(function () {
		/* Index carousel */
		$('.carousel', this).bxSlider({
			pause: 10000,
			controls: false,
			pagerCustom: '.pager'
		});
	});
	$('.block-staff').each(function () {
		/* Staff carousel */
		$('.carousel', this).bxSlider({
			pager: false,
			minSlides: 2
		});
	});
	$('.gallery').each(function () {
		/* Gallery carousel */
		$('.carousel', this).bxSlider({
			pager: false,
			minSlides: 4
		});
	});
	$('.up').click(function () {
		$('html, body').animate({scrollTop: 0}, 600, 'swing');
		return false;
	});
	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.84)'
				}
			}
		}
	});
});