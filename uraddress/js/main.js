/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */


/* On document ready */
$(document).ready(function () {

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
			$('.list', _self).toggleClass('open');
			return false;
		});
		$(document).on('click touchstart', function (event) {
			var target = $(event.target);
			if ((target.closest('.nav').length === 0) && (!target.is('.nav'))) {
				$('.list', _self).removeClass('open');
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

	/* Табы */
	$('.tabs').each(function () {
		$('a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$('.tab-in-' + where).css("display", "block").siblings('.tab-in').css("display", "none");
			return false;
		})
	});

	/* Попап ajax */
	$('.lightbox-ajax').magnificPopup({
		type: 'ajax',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		overflowY: 'scroll',
		settings: {
			cache: false
		}
	});

	/* Попап галерея */
	$('.lightbox-gallery').each(function () {
		$(this).magnificPopup({
			type: 'image',
			mainClass: 'mfp-fade',
			delegate: 'a.link',
			cursor: '',
			gallery: {
				enabled: true,
				navigateByImgClick: true,
				preload: [0, 1]
			}
		});
	});

	/* Попап видео */
	$('.lightbox-video').magnificPopup({
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false
	});

});

function initForms() {
	/* Формы */
	$('input, select').styler();
}

$.extend(true, $.magnificPopup.defaults, {
	tClose: 'Закрыть (Esc)', // Alt text on close button
	closeMarkup: '<div title="%title%" class="mfp-close">&times;</div>',
	tLoading: 'Загрузка...', // Text that is displayed during loading. Can contain %curr% and %total% keys
	gallery: {
		tPrev: 'Назад', // Alt text on left arrow
		tNext: 'Вперед', // Alt text on right arrow
		tCounter: '%curr% из %total%', // Markup for "1 of 7" counter
		arrowMarkup: '<div title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></div>', // markup of an arrow button
		cursor: null
	},
	image: {
		tError: '<a href="%url%">Изображение</a> не найдено.', // Error message when image could not be loaded
		cursor: null
	},
	ajax: {
		tError: '<a href="%url%">Контент</a> не найден.' // Error message when ajax request failed
	},
	callbacks: {
		beforeOpen: function () {
			initForms();
		}
	}
});