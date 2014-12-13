/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	$('.next').click(function () {
		var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1");
		$.scrollTo(where, {
			duration: 500,
			easing: 'swing'
		});
		return false;
	});

	$('.h3-line').each(function () {
		$(this).wrapInner('<span class="line"></span>');
	});

	$('body').append('<div class="overlay"></div>');
	$('.overlay').click(function () {
		var _self = $(this);
		$('.popup').fadeOut(500, 'swing', function () {
			_self.fadeOut(500, 'swing');
			$('html').removeClass('body-popup');
		});
	});
	$('.popup-open').click(function () {
		var where = $('.popup-' + $(this).attr('href').replace(/^.*#(.*)/, "$1"));
		$('.overlay').fadeIn(500, 'swing', function () {
			where.css('margin-left', -Math.floor(where.outerWidth() / 2)).css('margin-top', -Math.floor(where.outerHeight() / 2));
			where.fadeIn(500, 'swing');
			$('html').addClass('body-popup');
		});
		return false;
	});
	scrollEvent();
	resizeEvent()
});

$(window).on('scroll touchmove', function () {
	return scrollEvent();
});
/* Обработчики скролла */
function scrollEvent() {
	/* Переключение плавающего хедера */
	if ($(window).scrollTop() > 1) {
		$('.header').addClass('header-fixed');
	} else {
		$('.header').removeClass('header-fixed');
	}
}


$(window).on('resize', function () {
	resizeEvent();
});
window.inited = false;
function initCarousel() {
	window.carousel = $('.index .carousel ul').bxSlider({
		mode: 'fade',
		speed: 1000,
		pause: 5000,
		infiniteLoop: true,
		easing: 'ease',
		adaptiveHeight: false,
		useCSS: false,
		preloadImages: 'all',
		pager: false,
		controls: false,
		auto: true
	});
	window.inited = true;
}


/* Обработчики ресайза */
function resizeEvent() {
	if ($(window).width() < 768) {
		if (window.inited && window.carousel) {
			window.carousel.destroySlider();
			window.carousel.width('auto');
			window.inited = false;
		}
	} else {
		if (!window.inited) {
			initCarousel();
			window.inited = true;
		}
	}
}