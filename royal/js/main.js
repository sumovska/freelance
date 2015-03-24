/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */
function initForms() {
	/* Формы */
	$('input, select').styler({
		selectPlaceholder: ''
	});
}

function initGallery() {
	/* Галерея в кабинете */
	$('.gallery:visible:not(.gallery-inited)').each(function (i) {
		var slider = $('.carousel', this).bxSlider({
			pager: false,
			responsive: true,
			minSlides: 3,
			maxSlides: 8,
			moveSlides: 1,
			slideWidth: 80,
			slideMargin: 10,
			useCSS: true,
			infiniteLoop: false,
			hideControlOnEnd: true,
			adaptiveHeight: true
		});
		$('.button-close', this).click(function () {
			$(this).closest('li').fadeOut(function () {
				$(this).remove();
				slider.reloadSlider();
			});
			return false;
		});
		initFancybox();
		$(this).addClass('gallery-inited');
	});
}

function initFancybox() {
	/* Всплывающие окна (Fancybox) */
	$('.fancybox-popup').fancybox({
		padding: 20,
		margin: 20,
		wrapCSS: 'fancybox-default',
		nextEffect: 'fade',
		prevEffect: 'fade',
		fitToView: false,
		autosize: true,
		beforeShow: function () {
			initForms();
			initGallery();
		},
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.9)'
				}
			}
		}
	});

	/* Всплывающая галерея (Fancybox) */
	$('.fancybox-gallery').fancybox({
		padding: 0,
		margin: 50,
		nextEffect: 'fade',
		prevEffect: 'fade'
	});
}

/* On document ready */
$(document).ready(function () {

	/* Формы */
	initForms();

	/* Навигация */
	$('.nav').each(function () {
		$(this).wrap('<div class="scroll"></div>');
		$(this).after('<a class="nav-toggle" href="#"></a>');
		$('.nav-toggle').click(function () {
			var html = $('html');
			html.toggleClass('html-nav-open');
			$(this).animate({margin: 0}, 450, function () {
				html.width('101%');
				html.width('100%');
			});
			return false;
		});
		$('.container').click(function () {
			$('html').removeClass('html-nav-open');
		});
		$('li.sub', this).children('a').click(function () {
			if (Modernizr.touch || ($(window).width() < 1025)) {
				$(this).siblings('ul.sub').slideToggle({
					'complete': function () {
						$(this).closest('li').toggleClass('open');
					},
					'step': function () {
						resizeEvent();
					}
				});
				$(this).closest('li,sub').siblings('li.sub.open').find('.sub').slideUp({
					'complete': function () {
						$(this).closest('li').toggleClass('open');
					},
					'step': function () {
						resizeEvent();
					}
				});
				return false;
			}
		});
	});
	$('.header .logo').clone().addClass('logo-mobile').appendTo('body');

	/* Скролл наверх */
	$('.scroll-top').append('<span></span>').click(function () {
		if (Modernizr.touch) {
			$('html, body').animate({scrollTop: 0}, 0);
		} else {
			$('html, body').animate({scrollTop: 0}, 300);
		}
		return false;
	});

	/* Ссылка на окно овторизации */
	$('.login-link').click(function () {
		$('.login').fadeToggle(100);
		return false;
	});
	$('html').bind("click touchstart", function (e) {
		if ((!$(e.target).is('.login')) && ($(e.target).closest('.login').length < 1)) {
			$('.login').fadeOut(100);
		}
	});

	/* Поле поиска */
	$('body').append('<a href="#" class="search-toggle"></a>');
	$('.search').each(function () {
		function openSearch() {
			if (!$('html').hasClass('body-search-open')) {
				_self.show().animate({'width': '100%'}, 400, 'swing', function () {
					$('html').addClass('body-search-open');
				});
			} else {
				if ($(this).is('.search-toggle')) {
					closeSearch();
				}
			}
			return false;
		}

		function closeSearch() {
			var html = $('html');
			if (html.hasClass('body-search-open')) {
				html.removeClass('body-search-open');
				_self.animate({'width': '40px'}, 400, 'swing', function () {
					_self.removeAttr('style');
				});
			}
			return false;
		}

		var _self = $(this);
		$(this).append('<a href="#" class="search-toggle"></a>');
		$('.search-toggle').click(openSearch);
		$('input[type="text"]', _self).focus(openSearch);
		$('html').bind("click touchstart", function (e) {
			if ($(this).hasClass('body-search-open')) {
				if ((!$(e.target).is('.search')) && ($(e.target).closest('.search').length < 1)) {
					closeSearch();
				}
			}
		});
	});

	/* Футер */
	$('.footer').each(function () {
		$(this).clone().appendTo('.header .scroll');
		$(this).hide();
		$('.phone', this).clone().addClass('phone-mobile').appendTo('body');
	});

	/* Карусель на главной */
	$('.index').each(function () {
		var carousel = $('.carousel', this), index = $(this);
		carousel.bxSlider({
			infinteLoop: false,
			responsive: true,
			adaptiveHieght: true,
			useCSS: true,
			swipeThreshold: 20,
			speed: 800,
			preloadImages: 'all',
			auto: true,
			autoControls: true,
			pause: 5000,
			onSliderLoad: function () {
				$('.bx-controls', index).wrap('<div class="bx-controls-space"></div>');
				carousel.find('.item:not(.bx-clone)').eq(1).clone().addClass('bx-clone').appendTo(carousel);
				carousel.width($('.item').length * 100 + '%');
				$('.bx-wrapper', index).append('<span class="forward"></span>');
				$('.forward', index).click(function () {
					carousel.goToNextSlide();
					carousel.stopAuto()
				});
			}
		});
	});

	/* Награды */
	$('.rewards').each(function () {
		$('.scroll', this).mCustomScrollbar({
			axis: "x",
			scrollInertia: 100,
			scrollButtons: {enable: false},
			autoHideScrollbar: false,
			mouseWheel: {invert: true},
			theme: "rounded-dark",
			autoExpandScrollbar: true
		});
	});

	/* Сворачивание/разворачивание фильтра */
	$('.filter .toggle').click(function () {
		var o = 1, _self = $(this);
		if ($(this).is('.open')) {
			o = 0;
		}
		$(this).siblings('.inside').animate({opacity: o}, function () {
			$(this).slideToggle(function () {
				_self.toggleClass('open');
			});
		});
		return false;
	});

	/* Catalog new block */
	$('.catalog-new').each(function () {
		$('.scroll', this).mCustomScrollbar({
			axis: "x",
			scrollInertia: 100,
			scrollButtons: {enable: false},
			autoHideScrollbar: false,
			mouseWheel: {invert: true},
			theme: "rounded-dark",
			autoExpandScrollbar: true
		});
	});

	/* FAQ block */
	$('.faq').each(function () {
		$('.title a', this).click(function () {
			$(this).closest('.item').toggleClass('active');
			return false;
		});
	});

	/* Block-item */
	$('.block-item .info').each(function () {
		$('.colors li a').click(function () {
			$(this).closest('li').toggleClass('active').siblings('.active').removeClass('active');
		});
	});

	/* Tabs-list toggle */
	$('.tabs-list').each(function () {
		$('.submenu-triggers a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Tabs-list toggle */
	$('.tabs-abc').each(function () {
		$('.triggers a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Cart block */
	$('.button-close').click(function () {
		$(this).closest('.entry').fadeToggle(200);
		return false;
	});

	$('.submenu-small').each(function () {
		var _self = $(this);
		$('a', this).click(function () {
			if ($(this).closest('li').is('.active')) {
				_self.toggleClass('submenu-small-open');
				return false;
			}
		});
	});

	$('.steps-small').each(function () {
		var _self = $(this);
		$('a', this).click(function () {
			if ($(this).closest('li').is('.active')) {
				_self.toggleClass('steps-small-open');
				return false;
			}
		});
	});

	$('.check-all .jq-checkbox').click(function () {
		$('.check input:checkbox').not(this).click();
	});

	/* Orders block */
	/* Включение/выключение формы сообщения */
	$('.cabinet-orders').each(function () {
		$('.number', this).click(function () {
			$(this).closest('.order').toggleClass('order-open');
			return false;
		});
	});

	/* Сворачивание/разворачивание формы сообщения */
	$('.cabinet-manager').each(function () {
		$('.cabinet-message .link', this).click(function () {
			$('.form-message').toggleClass('open');
			return false;
		});
	});

	/* Галерея в кабинете */
	initGallery();

	/* Попапы */
	initFancybox();

	/* IE баги */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			$('.two .col:nth-child(2n - 1)').addClass('nth-child-2n-1');
		}
	}
	if (!Modernizr.svg) {
		$('.header .logo img').attr('src', 'img/ie/logo.png');
	}
	if (!Modernizr.borderradius) {
		if (window.PIE) {
			$('.index .forward, .rewards .list img').each(function () {
				PIE.attach(this);
			});
		}
	}

	resizeEvent();
	scrollEvent();
});

$(window).on('scroll touchmove', function () {
	return scrollEvent();
});

$(window).on('resize', function () {
	return resizeEvent();
});

function resizeEvent() {
	$('.header').each(function () {
		if (($('.nav', this).outerHeight(true) + $('.footer', this).outerHeight(true) + 20) >= $(this).outerHeight(true)) {
			$(this).addClass('header-relative');
		} else {
			$(this).removeClass('header-relative');
		}
	});
}

function scrollEvent() {
	/* Переключение плавающего хедера */
	if ($(window).scrollTop() > 60) {
		$('html').addClass('header-fixed');
	} else {
		$('html').removeClass('header-fixed');
	}
}