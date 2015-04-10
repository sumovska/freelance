/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Формы */
	$('input, select').styler();

	/* Всплывающее окно (попапы) */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 20,
		autoResize: true,
		autoCenter: true,
		helpers: {
			media: {}
		}
	});

	/* Всплывающее окно (галерея) */
	$('.fancybox-gallery').fancybox({
		padding: 0,
		margin: 30,
		helpers: {
			media: {}
		},
		tpl: {
			closeBtn: '<span title="Close" class="fancybox-close fancybox-close-top"></span>'
		}
	});

	/* Анимация спецпредложений */
	$('.special li').hover(function () {
		$(this).find('.text', this).eq(0).stop().animate({
			top: (+$(this).outerHeight() - +$('.text', this).outerHeight() - 6) + 'px'
		}, function () {
		});
	}, function () {
		$(this).find('.text', this).stop().animate({
			bottom: 'auto',
			top: '6px'
		}, function () {
			$(this).removeAttr('style');
		});
	});

	/* Навигация */
	$('.nav').each(function () {
		var _self = $(this);
		$(this).append('<span class="toggle"></span>');
		$('.toggle', this).click(function () {
			$('.list', _self).slideToggle();
			return false;
		});
		$(document).on('click touchstart', function (event) {
			var target = $(event.target);
			if ((target.closest('.nav').length === 0) && (!target.is('.nav'))) {
				$('.list', _self).slideUp();
			}
		});
	});

	/* Выпадающая форма заказа */
	$('.address-order').each(function () {
		$('.button-default', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).toggleClass('open');
			$('#' + where).slideToggle('slow');
			return false;
		});
	});

	/* Табы */
	$('.tab-hidden').css("display", "none");
	$('.pages-tabs').each(function () {
		$('a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$('.tab-' + where).css("display", "block").siblings('.tab').css("display", "none");
			return false;
		});
	});

	$('.address-inner').each(function () {
		$('.tabs').each(function () {
			$('a', this).click(function () {
				var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
				$(this).closest('li').addClass('active').siblings('li').removeClass('active');
				$('.tab-in-' + where).css("display", "block").siblings('.tab-in').css("display", "none");
				return false;
			})
		})
	});

});