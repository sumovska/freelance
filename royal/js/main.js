/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Scroll top button */
	$('.scroll-top').append('<span></span>').click(function () {
		$('html, body').animate({scrollTop: 0}, 300);
		return false;
	});

	/* Nav initialization */
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

	$('.login-link').click(function () {
		$('.login').fadeToggle(100);
		return false;
	});
	$('html').bind("click touchstart", function (e) {
		if ((!$(e.target).is('.login')) && ($(e.target).closest('.login').length < 1)) {
			$('.login').fadeOut(100);
		}
	});

	/* Footer */
	$('.footer').each(function () {
		$(this).clone().appendTo('.header .scroll');
		$(this).hide();
		$('.phone', this).clone().addClass('phone-mobile').appendTo('body');
	});
	$('.header .logo').clone().addClass('logo-mobile').appendTo('body');
	$('body').append('<a href="#" class="search-toggle"></a>');

	/* Searchbox initialization */
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

	/* Index carousel */
	$('.index').each(function () {
		var carousel = $('.carousel', this), index = $(this);
		carousel.bxSlider({
			infinteLoop: false,
			responsive: true,
			adaptiveHieght: true,
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

	/* Rewards block */
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
		$(this).closest('.cover').fadeToggle(200);
		return false;
	});

	/* Gallery */
	$('.gallery').each(function () {
		$('.carousel', this).bxSlider({
			pager: false,
			minslides: 5,
			infiniteLoop: false
		});
		$('.fancybox-gallery', this).fancybox({
			autoSize: false,
			fitToView: false,
			padding: 0,
			helpers: {
				media: {}
			}
		});
	});

	/* Fancybox script */
	$('.fancybox, .fancybox-popup').fancybox({
		margin: 40,
		nextEffect: 'fade',
		prevEffect: 'fade',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.9)'
				}
			}
		}
	});

	/* Orders block */
	$('.block-orders').each(function () {
		$('.number', this).click(function () {
			$(this).closest('.order').toggleClass('order-active');
			return false;
		});
	});

	/* IE fixes */
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