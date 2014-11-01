/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Инициализация блока видео */
	if ($('.index').length > 0) {
		window.video = $('.index .video .resize').eq(0);
		window.video.css({
			'width': 'auto',
			'top': '50%',
			'left': '50%'
		})
	}
	$(window).resize();

	$('.image-carousel .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 276,
		minSlides: 6,
		maxSlides: 6,
		slideMargin: 52,
		moveSlides: 1
	});

	$('.project-carousel .carousel').bxSlider({
		auto: true,
		infiniteLoop: false,
		slideWidth: 1200,
		minSlides: 1,
		maxSlides: 1,
		slideMargin: 52,
		moveSlides: 1,
		speed: 700
	});
});

$(window).resize(function () {
	/* Изменение размеров видео на главной */
	if (typeof window.video != 'undefined') {
		if (window.video.width() <= window.video.parent().width()) {
			window.video.width('100%').height('auto');
		}
		if (window.video.height() <= window.video.parent().height()) {
			window.video.width('auto').height('100%');
		}
		window.video.css({
			'margin-left': '-' + Math.floor(+window.video.width() / 2) + 'px',
			'margin-top': '-' + Math.floor(+window.video.height() / 2) + 'px'
		})
	}
});

window.lastScrollTop = 0;
window.scrolling = true;
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
	if (typeof window.video != 'undefined') {
		/* скролл до нужного места */
		h = $(window).height() - 40;
		if ((current > 1) && (current < (h - 1)) && scrolling) {
			$(window).disablescroll();
			scrolling = false;
			if (current <= lastScrollTop) {
				h = 0;
			}
			$('html, body').animate({
				scrollTop: h
			}, 500, 'swing', function () {
				$(window).disablescroll('undo');
				scrolling = true;
			});
		}
	}
	lastScrollTop = current;
	if (!scrolling) {
		return false;
	}
}