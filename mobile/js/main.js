/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();

	$('.index').each(function () {
		$('.carousel', this).slick({
			adaptiveHeight: false,
			dots: true,
			arrows: false,
			customPaging: function (slider, i) {
				return '<span data-role="none">' + (i + 1) + '</span>';
			}
		});
	});

	/* Slider carousel */
	$('.slider').each(function () {
		$('.slider-for').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			asNavFor: '.slider-nav'
		});
		$('.slider-nav').each(function () {
			$(this).slick({
				slidesToScroll: 1,
				centerPadding: '0',
				slidesToShow: 3,
				asNavFor: '.slider-for',
				arrows: false,
				centerMode: true,
				focusOnSelect: true
			});
			$('.slick-slide', this).removeClass('slick-active');
			$('.slick-slide', this).eq(0).addClass('slick-active');
		});
	});

	$('.price-slider').each(function () {
		$('.item', this).noUiSlider({
			start: [1200, 6000],
			step: 1,
			behaviour: 'drag',
			connect: true,
			range: {
				'min': 0,
				'max': 30000
			},
			format: wNumb({
				decimals: 0
			})
		});
		$('.item', this).Link('lower').to($('.from', this)).Link('upper').to($('.to', this));
	});
});

