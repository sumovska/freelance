/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();

	/* Index page carousel */
	$('.slider .carousel').bxSlider({
		minSlides: 1,
		maxSlides: 2
	});

	$('.features').each(function () {
		var _self = $(this);
		/* Features carousel */
		$('.carousel').bxSlider({
			controls: false,
			mode: 'vertical',
			adaptiveHeight: true
		});
		$('.block-item-add .close').click(function () {
			$(this).closest('.features').fadeToggle(400);
			return false;
		});
	});

	$('.popup-gallery .carousel').bxSlider({
		controls: false,
		mode: 'vertical',
		adaptiveHeight: true,
		maxSlides: 1,
		minSlides: 1
	});

	$('.button-close').click(function () {
		$(this).closest('.cover').fadeToggle(400);
		return false;
	});

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
			where.css('margin-left', -Math.floor(where.outerWidth() / 2));
			where.fadeIn(300, 'swing');
		});
		return false;
	});
	$('.news .unit .inform').each(function () {
		var _self = $(this);
		$('.link', this).click(function () {
			_self.toggleClass('inform-open');
			$('.hidden', _self).slideToggle(400);
			return false;
		});
	});

	$('.header').each(function () {
		$('.products .switch').click(function () {
			$(this).closest('li').toggleClass('active');
			return false;
		});
	});

	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(22, 35, 53, 0.97)'
				}
			}
		}
	});

	/* Popup script */
	$(".header .toggle").fancybox({
		padding: 0,
		wrapCSS: 'fancybox-menu',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(22, 35, 53, 0.97)'
				}
			}
		}
	});

	$(".similar li a").fancybox({
		autoSize: false,
		wrapCSS: 'fancybox-gallery',
		fitToView: false,
		padding: 0,
		helpers: {
			overlay: {
				css: {
					'background': 'rgba(22, 35, 53, 0.5)'
				}
			}
		}
	});

	$('.functions').each(function () {
		$('.more', this).click(function () {
			$(this).closest('.line').toggleClass('line-active').siblings('.active').removeClass('active');
			return false;
		});
		$('.similar li a', this).click(function () {
			$(this).closest('li').toggleClass('active').siblings('.active').removeClass('active');
		});
	});

	/* Dealers scrollbar */
	$('.city').each(function () {
		$('.list', this).perfectScrollbar();
		$('.switch', this).click(function () {
			$(this).siblings('.list').fadeToggle(400);
			$('span', this).toggleClass('active');
			return false;
		});
	});

	$('.tabs').each(function () {
		$('.triggers li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$(this).closest('.tabs').attr('class', 'tabs').addClass('tabs-' + where);
			return false;
		});
	});

	/* Block-cart */
	$('.block-cart .goods .item').each(function () {
		var input = $('.amount-text', this);
		$('.plus', this).click(function () {
			var a = +input.val() + 1;
			return false;
		});
	});

	/* Nav init */
	$('.header .nav').each(function () {
		$(window).on('scroll touchmove', function () {
			/* Toggle fixed header */
			if ($(window).scrollTop() > 14) {
				$('.header').addClass('header-fixed');
			} else {
				$('.header').removeClass('header-fixed');
			}
		});
	});

	$('.popup-instruction').each(function() {
		$('.technology .stroke .name', this).click(function () {
			$(this).siblings('.inside').fadeToggle(400).closest('.stroke').toggleClass('stroke-open').siblings('.stroke-open').removeClass('stroke-open');
			return false;
		});
	});

});
