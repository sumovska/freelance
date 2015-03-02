/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();

	/* Nav init */
	$('.header').each(function () {
		$(window).on('scroll touchmove', function () {
			/* Toggle fixed header */
			if ($(window).scrollTop() > 5) {
				$('.header').addClass('header-fixed');
			} else {
				$('.header').removeClass('header-fixed');
			}
		});
	});

	$('.button-close').click(function () {
		$(this).closest('.cover').fadeToggle(200);
		return false;
	});

	$('.filter').each(function() {
		$('.toggle').click(function() {
			$(this).siblings('.inside').fadeToggle();
			return false;
		});
	});
});