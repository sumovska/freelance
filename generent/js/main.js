/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true, node: true */
/*global window, console, document, $, jQuery, PIE, initialize, styler */

function initForms() {
	$('input, select').styler();
}

/* On document ready */
$(document).ready(function () {

	/* Формы */
	initForms();

	$('.tabs').each(function () {
		$('li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$('#' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	$('.slider-small').each(function () {
		$('.slider-in').slick({
			arrows: false,
			dots: true
		});
		$('.slick-dots button').remove();
		$('.slick-dots li').append('<span class="dots"></span>');
	});

});

