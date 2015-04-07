/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Формы */
	$('input, select').styler();

	/* Всплывающее окно */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 50,
		helpers: {
			media: {}
		}
	});

	/* Анимация спецпредложений */
	$('.special li').hover(function () {
		$(this).find('.text', this).eq(0).stop().animate({
			top: (+$(this).outerHeight() - +$('.text', this).outerHeight() - 6) + 'px'
		}, "slow", function () {
		});
	}, function () {
		$(this).find('.text', this).stop().animate({
			bottom: 'auto',
			top: '6px'
		}, "slow", function () {
			$(this).removeAttr('style');
		});
	});

});