/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Init forms */
	$('input, select').styler();

	/* Header */
	$('.header').each(function () {
		var _header = $(this);
		$('.cell', this).each(function () {
			var _self = $(this);
			$('.link', this).click(function () {
				_self.siblings('.cell').removeClass('active');
				_self.toggleClass('active');
				return false;
			});
		});
	});

	$('.index').each(function () {
		$('.carousel', this).bxSlider({
			controls: false
		});
	});

	/* Filter */
	$('.filter').each(function () {
		$('.slider', this).each(function () {
			var _self = $(this);
			var item = $('.item', this).noUiSlider({
				start: [ 3000, 190000 ],
				step: 100,
				behaviour: 'drag',
				connect: true,
				range: {
					'min': 3000,
					'max': 315000
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