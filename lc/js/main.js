/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	var body = $('body');

	/* Инициализация форм */
	$(':input').styler();

	/* Попап */
	$(".fancybox").fancybox();

	/* Меню брендов */
	$('.brands').each(function () {
		$('li', this).each(function () {
			if ($(this).children('ul').length > 0) {
				$(this).addClass('sub');
			}
		});
		$('li.sub > a', this).click(function () {
			$(this).closest('li').toggleClass('open').siblings('.open').removeClass('open');
			return false;
		});
	});
	body.bind('mousedown', function (e) {
		if (($(e.target).closest('.sub').length < 1) && (!$(e.target).is('.brands'))) {
			$('.brands li.open').removeClass('open');
		}
	});

	/* Субменю */
	$('.submenu').each(function () {
		$('li', this).each(function () {
			if ($(this).children('ul').length > 0) {
				$(this).addClass('sub');
			}
		});
		$('li.sub > a', this).click(function () {
			$(this).siblings('ul').slideToggle(200, function () {
				$(this).closest('li').toggleClass('open');
			});
			return false;
		});
	});

	/* Карусель */
	$('.carousel .catalog').bxSlider({
		infiniteLoop: true,
		useCSS: false,
		pager: false,
		slideWidth: 219,
		maxSlides: 4,
		moveSlides: 1
	});

	/* Переключение чата */
	$('.chat').each(function () {
		var _self = $(this);
		$('.toggle', this).click(function () {
			if (_self.is('.chat-open')) {
				_self.animate({
					width: '34px'
				}, function () {
					_self.removeClass('chat-open');
				});
			} else {
				_self.animate({
					width: '304px'
				}, function () {
					_self.addClass('chat-open');
				});
			}
			return false;
		});
	});
	body.bind('mousedown', function (e) {
		if (($(e.target).closest('.chat').length < 1)) {
			$('.chat-open').animate({
				width: '34px'
			}, function () {
				$('.chat-open').removeClass('chat-open');
			});
		}
	});

	/* IE Fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			$('.crumbs-title .name:last-child').addClass('last-child');
			$('.community-group .member-link:nth-child(3n)').addClass('nth-child-3n');
		}
	}
});

