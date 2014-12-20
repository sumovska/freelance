/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Phone triggers */
	$('.top .call').each(function () {
		var _self = this;
		$('.triggers a', this).click(function () {
			var where = $(this).attr('href').replace(/^.*#(.*)/, "$1");
			$('.' + where, _self).addClass('active').siblings().removeClass('active');
			$(this).closest('li').toggleClass('active').siblings('li').removeClass('active');
			return false;
		});
	});

	$('.header .nav').each(function () {
		var _nav = $(this), _html = $('html');
		$('.toggle').click(function () {
			$(this).toggleClass('active');
			if ($(this).is('.active')) {
				_html.addClass('sublist-open');
				$('.sublist', _nav).fadeIn(300, 'linear');
			} else {
				_html.removeClass('sublist-open');
				$('.sublist', _nav).fadeOut(300, 'linear');
			}
			return false;
		});
		$('body').bind("click touchstart", function (e) {
			if (_html.hasClass('sublist-open')) {
				if (!($(e.target).is('.sublist')) && ($(e.target).closest('.sublist').length === 0 )) {
					$('.sublist', _nav).fadeOut(300, 'linear');
					$('.toggle').toggleClass('active');
					_html.removeClass('sublist-open');
				}
			}
		});
	});

	$('.index').each(function () {
		/* Index carousel */
		$('.carousel', this).bxSlider({
			adaptiveHeight: true,
			pause: 10000,
			controls: false,
			pagerCustom: '.pager'
		});
	});

	$('.block-features').each(function () {
		/* Features carousel */
		$('.carousel', this).bxSlider({
			pager: false
		});
	});

	$('.block-recent-projects').each(function () {
		/* Recent projects carousel */
		$('.carousel', this).bxSlider({
			pager: false
		});
	});

	$('.block-kinds').each(function () {
		/* Catalog carousel */
		$('.carousel', this).bxSlider({
			maxSlides: 4,
			pager: false
		});
	});

	/* Services */
	$('.block-services').each(function () {
		var _self = $(this), list = $('.list', _self);
		$('.show', this).click(function () {
			var h = list.height('auto').outerHeight(true);
			list.removeAttr('style').animate({'height': h});
			$(this).hide();
			return false;
		});
	});

	$('.block-news').each(function () {
		var _self = $(this);
		$('.all', this).click(function () {
			$(this).hide();
			$('.hidden', _self).fadeToggle(400);
			return false;
		});
	});
	$('.block-action').each(function () {
		var _self = $(this);
		$('.all', this).click(function () {
			$(this).hide();
			$('.hidden', _self).fadeToggle(400);
			return false;
		});
	});

	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.8)'
				}
			}
		}
	});

	$(window).on('scroll touchmove', function () {
		/* Toggle fixed header */
		if ($(window).scrollTop() > 86) {
			$('.header').addClass('header-fixed');
		} else {
			$('.header').removeClass('header-fixed');
		}
	});
});