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
		$(window).on('scroll touchmove', function () {
			/* Toggle fixed header */
			if ($(window).scrollTop() > 86) {
				$('.header').addClass('header-fixed');
			} else {
				$('.header').removeClass('header-fixed');
			}
		});
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

	/* Recent projects iniblock-numbert */
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

	$('.block-number:not(.block-number-static)').each(function () {
		function count() {
			$('.number', _number).each(function () {
				var _self = $(this), myInterval, max = +_self.attr('data-counter'), counter = 0, len = max.toString().length, mask = '', i = 0, temp = 0, speed = +_self.attr('data-speed'), step = +_self.attr('data-step');
				for (i = 0; i < len; i++) {
					mask = mask + '0';
				}
				myInterval = setInterval(function () {
					counter = counter + step;
					if (counter >= max) {
						clearInterval(myInterval);
						counter = max;
					}
					temp = (mask + counter).slice(-len);
					$('span', _self).each(function (i) {
						$(this).text(temp[i]);
					});
				}, speed);
			});
		}

		var _number = $(this), top = $(this).offset().top - Math.floor(3 * $(window).height() / 4);
		$(window).on('scroll touchmove', function () {
			if (!_number.hasClass('block-number-start')) {
				if ($(window).scrollTop() > top) {
					_number.addClass('block-number-start');
					count();
				}
			}
		});
	});

	$('.block-process').each(function () {
		var _progress = $(this), top = $(this).offset().top - Math.floor(2 * $(window).height() / 3);
		$(window).on('scroll touchmove', function () {
			if (!_progress.hasClass('block-process-start')) {
				if ($(window).scrollTop() > top) {
					_progress.addClass('block-process-start');
				}
			}
		});
	});

	$('.block-project').each(function () {
		var _self = $(this), _project = $('.picture', this), top = _project.offset().top, bottom = _project.offset().top + _project.height();
		$(window).on('scroll touchmove', function () {
			if ($(window).scrollTop() > top) {
				_self.addClass('block-project-start');
				bottom = _project.offset().top + _project.height() - 400;
				if ($(window).scrollTop() > bottom) {
					_self.addClass('block-project-end');
				} else {
					_self.removeClass('block-project-end');
				}
			} else {
				_self.removeClass('block-project-start');
			}
		});
	});

	$('.tabs').each(function () {
		$('li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('#' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	$('.block-number-timer').countdown('2015/05/05', function (event) {
		$(this).html(event.strftime('<div class="col"><div class="number"><span>%D</span><span>%D</span></div><p class="legend">дни</p></div><div class="col"><div class="number"><span>%H</span><span>%H</span></div><p class="legend">часы</p></div><div class="col"><div class="number"><span>%M</span><span>%M</span></div><p class="legend">минуты</p></div>'));
	});


	/* IE fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			$('.block-recent-projects .slider:last-child,.block-info .news-latest .list .item:last-of-type,.footer .col:nth-child(1)').addClass('last-child');
		}
	}
});