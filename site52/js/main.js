/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Init forms */
	$('input, select').styler();

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

	/* Nav init */
	$('.header .nav').each(function () {
		var _nav = $(this), _html = $('html');
		$('.toggle', _nav).click(function () {
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
		$('.close', _nav).click(function () {
			$('.toggle', _nav).removeClass('active');
			_html.removeClass('sublist-open');
		});
		if ($(window).width() > 700) {
			$('body').bind("click touchstart", function (e) {
				if (_html.hasClass('sublist-open')) {
					if (!($(e.target).is('.sublist')) && ($(e.target).closest('.sublist').length === 0 )) {
						$('.sublist', _nav).fadeOut(300, 'linear');
						$('.toggle').toggleClass('active');
						_html.removeClass('sublist-open');
					}
				}
			});
		}
	});

	/* Index init */
	$('.index').each(function () {
		/* Index carousel */
		$('.carousel', this).bxSlider({
			adaptiveHeight: true,
			swipeThreshold: 25,
			pause: 10000,
			controls: false,
			pagerCustom: '.pager'
		});
	});

	/* About init */
	$('.about').each(function () {
		var _self = $(this);
		$('.more, .close', this).click(function () {
			var _more = $(this);
			_self.parent().find('.about').toggle();
			return false;
		});
	});

	/* Features init */
	$('.block-features').each(function () {
		/* Features carousel */
		$('.carousel', this).bxSlider({
			swipeThreshold: 25,
			pager: false
		});
	});

	/* Recent projects init */
	$('.block-recent-projects').each(function () {
		/* Recent projects carousel */
		$('.carousel', this).bxSlider({
			swipeThreshold: 25,
			pager: false
		});
	});

	/* Kinds init */
	$('.block-kinds').each(function () {
		/* Catalog carousel */
		$('.carousel', this).bxSlider({
			swipeThreshold: 25,
			maxSlides: 4,
			pager: false
		});
	});

	/* Services init */
	$('.block-services').each(function () {
		var _self = $(this), list = $('.list', _self);
		if (!Modernizr.touch) {
			$('.services li', this).hover(function () {
				$(this).siblings('li').addClass('blur');
			}, function () {
				$(this).siblings('li').removeClass('blur');
			});
		}
		$('.show', this).click(function () {
			var h = list.height('auto').outerHeight(true);
			list.removeAttr('style').animate({'height': h}, function () {
				$(this).height('auto');
			});
			$(this).hide();
			return false;
		});
	});

	/* News init */
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
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.8)'
				}
			}
		}
	});

	/* Scroll up init */
	$('.up').click(function () {
		$('html, body').animate({scrollTop: 0}, 600, 'swing');
		return false;
	});

	/* Onscroll */
	$(window).on('scroll touchmove', function () {
		/* Toggle fixed header */
		if ($(window).scrollTop() > 86) {
			$('.header').addClass('header-fixed');
		} else {
			$('.header').removeClass('header-fixed');
		}
	});

	/* IE fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			$('.block-recent-projects .slider:last-child,.block-info .news-latest .list .item:last-of-type,.footer .col:nth-child(1)').addClass('last-child');
		}
	}
});