/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();
	
	$('.index').each(function() {
		$('.carousel', this).bxSlider({
			controls: false
		});
	});

	$('.slider').each(function () {
		$('.item', this).noUiSlider({
			start: [1200, 2359],
			step: 1,
			behaviour: 'drag',
			connect: true,
			range: {
				'min': 0,
				'max': 3000
			},
			format: wNumb({
				decimals: 0
			})
		});
		$('.item', this).Link('lower').to($('.from', this)).Link('upper').to($('.to', this));
	});
});