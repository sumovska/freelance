/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();

	$('.index').each(function () {
		/* Index carousel */
		$('.carousel', this).bxSlider ({
			adaptiveHeight: true,
			pager: false
		});
	});
	$('.block-gallery').each(function () {
		/* Gallery carousel */
		$('.carousel', this).bxSlider ({
			pager: false,
			minSlides: 6,
			maxSlides: 6
		});
	});
	$('.nav').each(function () {
		var _self = $(this);
		$('.toggle', this).click(function () {
			if ($('.nav-space', _self).length === 0) {
				$('ul', _self).wrap('<div class="nav-space"></div>')
			}
			$('.nav-space', _self).fadeToggle(200);
			$('body').toggleClass('body-nav-open');
			return false;
		});
		$('.close', this).click(function () {
			$('.nav-space', _self).fadeToggle(200);
			$('body').removeClass('body-nav-open');
			return false;
		});
	});

	/* Top checkins scrollbar */
	$('.block-dealers').each(function () {
		$('.list', this).perfectScrollbar();
	});

	/* Popup script */
	$('.fancybox-popup').fancybox({
		padding: 0,
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.8)'
				}
			}
		}
	});
});