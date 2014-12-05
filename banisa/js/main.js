/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	$('body').append('<div class="overlay"></div>');
	$('.overlay').click(function () {
		var _self = $(this);
		$('.popup').fadeOut(300, 'swing', function () {
			_self.fadeOut(300, 'swing');
		});
	});
	$('.js-popup').click(function () {
		var where = $('.' + $(this).attr('href').replace(/^.*#(.*)/, "$1"));
		$('.overlay').fadeIn(300, 'swing', function () {
			where.css('margin-left', -Math.floor(where.outerWidth() / 2)).css('margin-top', -Math.floor(where.outerHeight() / 2));
			where.fadeIn(300, 'swing');
		});
		return false;
	});

	$('.index').each(function () {
		$('.carousel', this).bxSlider({
			controls: false,
			pagerCustom: '.pager',
			adaptiveHeight: true
		});
		$('.item .about').each(function () {
			var _self = $(this);
			$('.more', this).click(function () {
				$(this).next('.toggle').fadeToggle(400);
				return false;
			});
		});
	});
});

$(window).on('scroll touchmove', function () {
	return scrollEvent();
});
/* Обработчики скролла */
function scrollEvent() {
	var current = $(window).scrollTop(), body, h = 0;
	/* Переключение плавающего хедера */
	if (current > 15) {
		$('.header').addClass('header-fixed');
	} else {
		$('.header').removeClass('header-fixed');
	}
}
