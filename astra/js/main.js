/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Forms init */
	$('input, select').styler();

	/* Header init */
	$('.header').each(function () {
		var _self = $(this);
		/* Fixed header */
		$('.nav', this).each(function () {
			$(window).on('scroll touchmove', function () {
				/* Toggle fixed header */
				if ($(window).scrollTop() > 10) {
					_self.addClass('header-fixed');
				} else {
					_self.removeClass('header-fixed');
				}
				if ($(window).scrollTop() > 21) {
					_self.addClass('header-fixed-shadow');
				} else {
					_self.removeClass('header-fixed-shadow');
				}
			});
		});
		/* Switching products menu */
		$('.products .switch', this).click(function () {
			if (!$(this).closest('li').is('.active')) {
				$(this).closest('li').addClass('active');
				return false;
			}
		});
		/* Responsive menu script */
		$('.toggle', this).click(function () {
			if ($(_self).find('.nav-tr').length < 1) {
				$('.nav', _self).wrapInner('<div class="nav-tr"></div>');
				$('.nav-tr', _self).wrapInner('<div class="nav-td"></div>');
			}
			$('body').toggleClass('body-menu');
			return false;
		});
		$('.social', this).clone().appendTo('.footer');
	});

	/* Popup scripts */
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

	$.extend($.fancybox.defaults.tpl, {
		closeBtn: '<a class="fancybox-button-close" href="javascript:void(0);"><span></span>Закрыть</a>'
	});

	var body = $('body');
	body.on('click', '.technology .stroke .name', function () {
		$(this).siblings('.inside').slideToggle().closest('.stroke').toggleClass('stroke-open').siblings('.stroke-open').removeClass('stroke-open');
		return false;
	});

	body.on('click', '.functions .more', function () {
		$(this).closest('.line').toggleClass('line-active').siblings('.active').removeClass('active');
		return false;
	});

	body.on('click', '.functions .similar li a', function () {
		$(this).closest('li').toggleClass('active').siblings('.active').removeClass('active');
	});

	/* Where city dropdown */
	$('.city').each(function () {
		var list = $('.list', this);
		list.perfectScrollbar();
		$('.dropdown', this).click(function () {
			list.toggle();
			$('span', this).toggleClass('active');
			return false;
		});
	});

	/* Index page carousel */
	$('.index').each(function () {
		function refresh(i) {
			var next, prev, active;
			$('.item', slider).removeClass('active').eq(i).addClass('active');
			active = $('.item.active', slider);
			if (active.next().length > 0) {
				next = active.next().find('img').attr('data-name');
			} else {
				next = $('.item', slider).eq(0).find('img').attr('data-name');
			}
			if (active.prev().length > 0) {
				prev = active.prev().find('img').attr('data-name');
			} else {
				prev = $('.item', slider).eq($('.item', slider).length - 1).find('img').attr('data-name');
			}
			$('.ws_next span', slider).html(next);
			$('.ws_prev span', slider).html(prev);
		}

		var slider = $('.wowslider', this), _self = $(this);
		if ($('body').is('.page-index')) {
			$('.header').clone().prepend('<span class="scroll">Прокрутите скролл вниз</span>').addClass('header-additional').insertAfter(_self);
		}
		slider.append('<div class="ws_bullets"><div></div></div>');
		$('.item', slider).each(function (i) {
			$('.ws_bullets div', slider).append('<a href="#' + (i + 1) + '">' + (i + 1) + '</a>');
		});
		slider.wowSlider({
			effect: "blinds",
			prev: "",
			next: "",
			duration: 20 * 75,
			delay: 20 * 300,
			width: 640,
			height: 360,
			autoPlay: true,
			autoPlayVideo: false,
			playPause: false,
			stopOnHover: false,
			loop: false,
			bullets: 1,
			caption: true,
			captionEffect: "fade",
			controls: true,
			responsive: 3,
			fullScreen: false,
			gestures: 0,
			onStep: function (i) {
				refresh(i);
			},
			images: 0
		});
		refresh(0);
		slider.addClass('loaded');
	});

	/* News script */
	$('.news .unit, .special .unit').each(function () {
		var _self = $('.inform', this);
		$('.link, .photo a', this).click(function () {
			var _a = $(this);
			_self.toggleClass('inform-open');
			$('.hidden', _self).slideToggle();
			return false;
		});
	});

	$('.block-item').each(function () {
		var _self = $(this);
		/* Features carousel */
		$('.carousel').bxSlider({
			controls: false,
			mode: 'vertical',
			adaptiveHeight: true
		});
	});

	$('.popup-gallery').each(function () {
		$('.carousel').bxSlider({
			controls: false,
			mode: 'vertical',
			adaptiveHeight: true,
			maxSlides: 1,
			minSlides: 1
		});
	});

	$('.button-close').click(function () {
		$(this).closest('.cover').fadeToggle(400);
		return false;
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
		var input = $('.amount-text', this), a = 0;
		$('.plus', this).click(function () {
			a = +input.val() + 1;
			return false;
		});
	});

});
