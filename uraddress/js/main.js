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

	$('.nav').each(function () {
		var _self = $(this);
		$(this).append('<span class="toggle"></span>');
		$('.toggle', this).click(function () {
			if ($('.nav-space', _self).length === 0) {
				$('.list', _self).wrap('<div class="nav-space"></div>')
			}
			$('.nav-space', _self).fadeToggle(200);
			$('body').toggleClass('body-nav-open');
			return false;
		});
	});

	$('body').click(function() {
		if ($(this).hasClass('body-nav-open')) {
			if (($(e.target).is('.nav .list'))) {
				$(e.target).closest('.nav-space').fadeOut(200);
				$('body').removeClass('body-nav-open');
			}
		}
	});


});