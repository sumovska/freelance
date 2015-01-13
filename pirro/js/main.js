/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();

	/* Index carousel */
	$('.index').each(function () {
		$('.carousel', this).bxSlider({
			adaptiveHeight: true,
			pager: false
		});
	});

	/* Gallery carousel */
	$('.block-gallery').each(function () {
		$('.carousel', this).bxSlider({
			pager: false,
			minSlides: 6,
			maxSlides: 6
		});
	});

	/* Header */
	$('.header').each(function () {
		$('.callback li a').click(function () {
			$(this).closest('li').toggleClass('active').siblings('.active').removeClass('active');
		});
	});

	/* Nav */
	$('.nav').each(function () {
		var _self = $(this);
		$('.toggle', this).click(function () {
			if ($('.nav-space', _self).length === 0) {
				$('.list', _self).wrap('<div class="nav-space"></div>')
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

	/* Dealers scrollbar */
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

	/* Sidebar */
	$('.sidebar').each(function () {
		var _self = $(this);
		$('.filter-link .link').click(function () {
			$(_self).toggleClass('sidebar-open');
			$('.filter').fadeToggle(200);
			return false;
		});
		/* Filter */
		$('.filter').each(function () {
			$('.slider', this).each(function () {
				var _self = $(this);
				var item = $('.item', this).noUiSlider({
					start: [40, 220],
					step: 1,
					behaviour: 'drag',
					connect: true,
					range: {
						'min': 0,
						'max': 250
					},
					serialization: {
						lower: [
							$.Link({
								target: $(".from var", _self)
							})
						],
						upper: [
							$.Link({
								target: $(".to var", _self)
							})
						],
						format: {
							// Set formatting
							thousand: ' ',
							decimals: 0
						}
					}
				});
			});
		});
	});
});