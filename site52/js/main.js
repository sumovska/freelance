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

	$('.header .nav').each(function() {
		$('.toggle').click(function () {
			var _self = $(this);
			_self.toggleClass('active');
			$('.sublist').fadeToggle(300);
			return false;
		});
	});

	$('.index').each(function () {
		/* Index carousel */
		$('.carousel', this).bxSlider({
			auto: true,
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

	$(window).on('scroll touchmove', function () {
		/* Toggle fixed header */
		if ($(window).scrollTop() > 86) {
			$('.header').addClass('header-fixed');
		} else {
			$('.header').removeClass('header-fixed');
		}
	});
});