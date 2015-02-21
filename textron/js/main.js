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
				$('.cell', _header).removeClass('active');
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
});