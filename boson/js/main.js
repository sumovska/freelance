/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Инициализация блока видео */
	if ($('.index').length > 0) {
		window.video = $('.index .video .resize').eq(0);
		window.video.one("load", function () {
			window.video.hide().addClass('loaded').fadeIn(100);
			window.video.css({
				'width': 'auto',
				'top': '50%',
				'left': '50%'
			});
		}).each(function () {
			if (this.complete) $(this).load();
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

	$('.gallery .carousel').bxSlider();

	$('.header .nav').each(function () {
		var _self = $(this);
		$(this).append('<a class="toggle" href="#"></a>');
		$('.toggle', this).click(function () {
			if ($('.nav-space', _self).length === 0) {
				$('ul', _self).wrap('<div class="nav-space"></div>')
			}
			$('.nav-space', _self).fadeToggle(200);
			$('body').toggleClass('body-nav-open');
			return false;
		});
	});

	$('body').bind("click touchstart", function (e) {
		if ($(this).hasClass('body-nav-open')) {
			if (($(e.target).is('.nav ul'))) {
				$(e.target).closest('.nav-space').fadeOut(200);
				$('body').removeClass('body-nav-open');
			}
		}
	});

	/* Popup */
	$('.popup').wrap('<div class="overlay"><div class="overlay-in"></div></div>');
	$('.js-popup').click(function () {
		var where = $('.' + $(this).attr('href').replace(/^.*#(.*)/, "$1"));
		$('.overlay').fadeIn(300, 'swing', function () {
			where.animate({opacity: 1}, 300, 'swing');
			$('html').addClass('popup-open');
		});
		return false;
	});
	$('.js-close').click(function () {
		closePopups();
		return false;
	});
	$(document).keyup(function(e) {
		if(e.keyCode== 27) {
			closePopups();
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

function closePopups() {
	$('.popup').animate({opacity: 0}, 300, 'swing', function () {
		$('.overlay').fadeOut(300, 'swing', function () {
			$('html').removeClass('popup-open');
		});
	});
}

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