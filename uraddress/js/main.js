/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Формы */
	$('input, select').styler();

	/* Всплывающее окно (попапы) */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 50,
		helpers: {
			media: {}
		}
	});

	/* Всплывающее окно (галерея) */
	$('.fancybox-gallery').fancybox({
		padding: 0,
		margin: 50,
		helpers: {
			media: {}
		},
		tpl: {
			closeBtn : '<span title="Close" class="fancybox-close fancybox-close-top"></span>'
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

	/* Навигация */
	$('.nav').each(function () {
		var _self = $(this);
		$(this).append('<span class="toggle"></span>');
		$('.toggle', this).click(function () {
			if ($('.nav-space', _self).length === 0) {
				$('.list', _self).wrap('<div class="nav-space"></div>')
			}
			$('.nav-space', _self).fadeToggle();
			$('body').toggleClass('body-nav-open');
			return false;
		});
	});

	/* Выпадающее меню в мобильной версии */
	$('body').click(function () {
		if ($(this).hasClass('body-nav-open')) {
			if (($(e.target).is('.nav .list'))) {
				$(e.target).closest('.nav-space').fadeOut(200);
				$('body').removeClass('body-nav-open');
			}
		}
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


});