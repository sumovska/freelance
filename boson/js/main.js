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
		});
		$('.index .down').click(function () {
			$(window).scrollTop(5);
			return false;
		});
	}
	$(window).resize();

	$('.clients .carousel').bxSlider({
		infiniteLoop: true,
		pager: false,
		slideWidth: 240,
		minSlides: 1,
		maxSlides: 5,
		slideMargin: 0,
		moveSlides: 1
	});

	$('.project-carousel .carousel').bxSlider();

	$('.header .nav').each(function () {
		var _self = $(this);
		$(this).append('<a class="toggle" href="#"></a>');
		$('.toggle', this).click(function () {
			$('ul', _self).fadeToggle(200);
			$('body').toggleClass('body-nav-open');
			return false;
		});
	});

	$('body').bind("click touchstart", function (e) {
		if ($(this).hasClass('body-nav-open')) {
			if (($(e.target).is('.nav ul'))) {
				$(e.target).fadeOut(200);
				$('body').removeClass('body-nav-open');
			}
		}
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
		if ($(window).width() > 1024) {
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
	}
	lastScrollTop = current;
	return scrolling;
}