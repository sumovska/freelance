/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

$(document).ready(function () {

});

$(window).load(function () {

	/* Header trigger */
	$('.header .toggle').click(function () {
		var body = $('body');
		$('html, body').toggleClass('header-open');
		if (body.hasClass('page-index')) {
			if (body.hasClass('header-open')) {
				$.fn.fullpage.setAllowScrolling(false);
			} else {
				$.fn.fullpage.setAllowScrolling(true);
			}
		}

		return false;
	});

	/* Gallery carousel */
	$('.gallery').each(function () {
		$('.carousel ul', this).bxSlider({
			captions: true,
			responsive: true,
			preloadImages: 'all',
			useCSS: false
		});
		$('.carousel', this).addClass('carousel-inited');
	});

	/* Slider carousel */
	$('.slider').each(function () {
		$('.carousel ul', this).bxSlider({
			mode: 'fade',
			speed: 800,
			infiniteLoop: true,
			easing: 'ease',
			adaptiveHeight: true,
			useCSS: false,
			preloadImages: 'all',
			controls: false,
			auto: true,
			minSlides: 1,
			maxSlides: 1,
			moveSlides: 1,
			pause: 10000
		});
		$('.carousel', this).addClass('carousel-inited');
	});

	/* Events carousel */
	$('.events').each(function () {
		$('.carousel .blogs', this).bxSlider({
			pager: false,
			useCSS: false,
			hideControlOnEnd: true,
			adaptiveHeight: true,
			infiniteLoop: false,
			preloadImages: 'all',
			slideWidth: 300,
			minSlides: 1,
			maxSlides: 5,
			moveSlides: 1,
			slideMargin: 30
		});
		$('.carousel', this).addClass('carousel-inited');
	});

	/* Chronicle carousel */
	$('.chronicle').each(function () {
		$(this).children('.carousel').addClass('carousel-inited').children('ul').bxSlider({
			infiniteLoop: false,
			adaptiveHeight: true,
			preloadImages: 'all',
			controls: false,
			useCSS: false,
			pagerCustom: '.carousel-pager'
		});
		$(this).find('.carousel-pager').bxSlider({
			infiniteLoop: false,
			hideControlOnEnd: true,
			adaptiveHeight: true,
			preloadImages: 'all',
			slideWidth: 260,
			minSlides: 1,
			maxSlides: 7,
			moveSlides: 1,
			slideMargin: 0,
			controls: true,
			pager: false,
			useCSS: false
		});
		$('.carousel li', this).each(function () {
			var pager = $('.carousel-inner-pager', this);
			pager.show();
			$('.carousel-inner ul', this).bxSlider({
				mode: 'fade',
				infiniteLoop: false,
				adaptiveHeight: true,
				preloadImages: 'all',
				controls: false,
				speed: 800,
				easing: 'ease',
				useCSS: false,
				pagerCustom: pager
			})
		});
	});

	/* Slider on index page & preloader */
	$('.page-index').each(function () {
		window.fullpage = $('.slider-index').fullpage({
			menu: '.slider-index-pager',
			scrollingSpeed: 400,
			easing: 'swing',
			loopBottom: true,
			afterRender: function () {
				$('.overlay').find('.logo').animate({
					opacity: 1,
					width: 190,
					height: 100,
					'margin-left': -95,
					'margin-top': -50
				}, {
					duration: 1000,
					complete: function () {
						$('body').queryLoader2({
							barColor: "#4ef1e7",
							backgroundColor: "#000",
							percentage: true,
							barHeight: 1,
							deepSearch: true,
							minimumTime: 4000,
							onLoadComplete: function () {
								$('#qLoverlay').addClass('loader-end');
								setTimeout(
									function () {
										$('body').addClass('page-index-loaded');
									}, 1700);
							}
						});
						$.fn.fullpage.setAllowScrolling(true);
						$('.overlay').hide();
						$('#qLoverlay').append('<div class="logo"><img src="img/logo.png" alt=""></div>').addClass('loader-start');
					}
				});
			}
		});
		$.fn.fullpage.setAllowScrolling(false);
		$('.bottom', this).click(function () {
			$.fn.fullpage.moveSectionDown();
			return false;
		});

	});

	/* Slider on index page & preloader */
	$('.page-chronicle').each(function () {
		$('body').queryLoader2({
			barColor: "#fff",
			backgroundColor: "#fff",
			percentage: true,
			barHeight: 1,
			deepSearch: true,
			minimumTime: 2000,
			fadeOutTime: 1000,
			onLoadComplete: function () {
				setTimeout(
					function () {
						$('body').addClass('page-chronicle-loaded');
					}, 500);
			}
		});
	});

	/* Blogs */
	$('.blogs').each(function () {
		var _self = $(this);
		$('.entry', this).hover(function () {
			_self.addClass('blogs-hover');
			$(this).addClass('entry-hover');
		}, function () {
			$(this).removeClass('entry-hover');
		});
		_self.hover(function () {
		}, function () {
			_self.removeClass('blogs-hover');
		});
	});

	/* Date picker */
	$('.datepicker').each(function () {
		var _self = $(this), today = new Date(), dd = today.getDate(), mm = today.getMonth() + 1, yyyy = today.getFullYear(), min, max;
		today = dd + '.' + mm + '.' + yyyy;
		min = (+dd + 14) + '.' + mm + '.' + yyyy;
		max = dd + '.' + mm + '.' + (+yyyy + 1);
		_self.addClass('incomplete').datetimepicker({
			lang: 'ru',
			i18n: {
				ru: {
					dayOfWeek: ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"]
				}
			},
			mask: true,
			timepicker: false,
			scrollInput: false,
			closeOnDateSelect: true,
			scrollMonth: false,
			todayButton: false,
			dayOfWeekStart: 1,
			yearStart: +yyyy,
			yearEnd: +yyyy + 1,
			minDate: min,
			defaultDate: min,
			maxDate: max,
			defaultSelect: true,
			format: 'd.m.Y',
			formatDate: 'd.m.Y',
			onGenerate: function (ct) {
				jQuery(this).find('.xdsoft_date.xdsoft_weekend')
					.addClass('xdsoft_disabled');
			},
			onChangeMonth: function () {
				return false;
			},
			onChangeDateTime: function () {
				_self.removeClass('incomplete').removeClass('error');
			}
		});
		_self.unbind("keypress keydown keyup").on("keypress keydown keyup", function (e) {
			var keys = [9, 13], allowed = false;
			for (var i = keys.length; i--;) {
				if (e.keyCode === keys[i]) {
					allowed = true;
				}
			}
			if (!allowed) {
				e.stopPropagation();
				return false;
			}
		});
	});

	/* Time picker */
	$('.timepicker').each(function () {
		var _self = $(this);
		_self.addClass('incomplete').datetimepicker({
			lang: 'ru',
			datepicker: false,
			defaultTime: '12:00',
			mask: true,
			format: 'H:i',
			timepickerScrollbar: false,
			allowTimes: ['12:00', '13:00', '14:00', '15:00', '16:00'],
			onChangeDateTime: function () {
				_self.removeClass('incomplete').removeClass('error');
			}
		});
		_self.unbind("keypress keydown keyup").on("keypress keydown keyup", function (e) {
			var keys = [9, 13], allowed = false;
			for (var i = keys.length; i--;) {
				if (e.keyCode === keys[i]) {
					allowed = true;
				}
			}
			if (!allowed) {
				e.stopPropagation();
				return false;
			}
		});
	});

	/* Mask for phone input */
	$('.mask-phone').inputmask({
		mask: "+7 (9{3}) 999-99-99",
		greedy: false,
		onBeforePaste: function (pastedValue, opts) {
			pastedValue = pastedValue.toLowerCase();
			return pastedValue.replace("mailto:", "");
		},
		definitions: {
			'*': {
				validator: "[0-9!#$%&'*+/=?^_`{|}~\-]",
				cardinality: 1,
				casing: "lower"
			}
		},
		oncomplete: function () {
			$(this).removeClass('error').removeClass('incomplete');
		},
		onincomplete: function () {
			$(this).addClass('error').addClass('incomplete');
		}
	});

	/* Mask for email input */
	$('.mask-email').inputmask({
		mask: "*{1,20}[.*{1,20}][.*{1,20}][.*{1,20}]@*{1,20}[.*{2,6}][.*{1,2}]",
		greedy: false,
		onBeforePaste: function (pastedValue, opts) {
			pastedValue = pastedValue.toLowerCase();
			return pastedValue.replace("mailto:", "");
		},
		definitions: {
			'*': {
				validator: "[0-9A-Za-z!#$%&'*+/=?^_`{|}~\-]",
				cardinality: 1,
				casing: "lower"
			}
		},
		oncomplete: function () {
			$(this).removeClass('error').removeClass('incomplete');
		},
		onincomplete: function () {
			$(this).addClass('error').addClass('incomplete');
		}
	});

	/* Mask for people number input */
	$('.mask-number').inputmask({
		mask: "9{1,2}",
		greedy: false,
		onBeforePaste: function (pastedValue, opts) {
			pastedValue = pastedValue.toLowerCase();
			return pastedValue.replace("mailto:", "");
		},
		definitions: {
			'*': {
				validator: "[0-9]",
				cardinality: 1,
				casing: "lower"
			}
		},
		oncomplete: function () {
			$(this).removeClass('error').removeClass('incomplete');
		},
		onincomplete: function () {
			$(this).addClass('error').addClass('incomplete');
		}
	});

	/* Forms */
	$('.form').submit(function () {
		var valid = true, total = 0, number = $('.mask-number', this), fill = true, numberline = number.eq(0).closest('.line');
		$('.required', this).each(function () {
			if (!$(this).val() || $(this).hasClass('incomplete')) {
				valid = false;
				$(this).addClass('error');
			} else {
				$(this).removeClass('error');
			}
		});
		if ($('.required.error', this).length > 0) {
			valid = false;
		}
		number.each(function () {
			if ($(this).val().length > 0) {
				total = total + +$(this).val();
			} else {
				fill = false;
			}
		});
		if (fill) {
			if (total > 25) {
				number.addClass('error');
				valid = false;
				if (numberline.nextAll('.line-error').length < 1) {
					numberline.after('<p class="line line-error" style="color:red;font-size:12px;">Суммарное количество посетителей не должно превышать 25</p>')
				}
			} else {
				number.removeClass('error');
				numberline.nextAll('.line-error').remove();
			}
		}
		if (valid) {
			hidePopups();
			showPopup('popup-success');
		} else {
			$(this).find('.error').eq(0).focus();
		}
		return false;
	});

	/* Popups */
	$('.popup').wrapInner('<div class="popup-table"><div class="popup-td"></div></div>').find('.close').click(function () {
		hidePopups();
		return false;
	});
	$('.js-popup').click(function () {
		var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
		showPopup(where);
		return false;
	});

	/* Fade on scroll */
	if (!Modernizr.touch) {
		$('.content-invisble > *').viewportChecker({
			offset: 150
		});
	}

	/* Forms Initialization */
	$('input, select').styler();

	/* Black&White image conversion */
	$('.grayscale').gray();
	$('.events .entry > a').hover(function () {
		$('.picture', this).removeClass('grayscale');
	}, function () {
		$('.picture', this).addClass('grayscale');
	});

	/* Tabs */
	$('.tabs').each(function () {
		$('a', this).click(function () {
			var attr = $(this).attr('href').replace(/^.*#(.*)/, "$1");
			$(this).addClass('active').siblings('.active').removeClass('active');
			$('.' + attr).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	$('.up').click(function () {
		$('html, body').animate({
			scrollTop: 0
		}, 500, 'swing');
		return false;
	});

	resizePopup();
	$(window).resize();
	$(window).scroll();
})
;

$(window).resize(function () {
	var h, body = $('body');
	h = window.innerHeight;
	if (body.hasClass('page-slider')) {
		if ($(window).width() > 768) {
			body.attr('data-height', h);
		} else {
			body.attr('data-height', 595);
		}
		$('.slider').height(h);
	}
	if ($(window).width() < 1270 && !body.hasClass('page-touch')) {
		body.addClass('page-touch');
	}
	if ($(window).width() >= 1270 && body.hasClass('page-touch')) {
		$('body').removeClass('page-touch');
	}
	resizePopup();
});

window.lastScrollTop = 0;

$(window).on('touchmove', function () {
	return scrollEvent();
});
$(window).on('scroll', function () {
	return scrollEvent();
});


function scrollEvent() {
	var body = $('body'), current = $(window).scrollTop(), h = body.attr('data-height');
	if (body.hasClass('header-top') && !body.hasClass('page-index') && ($(window).width() > 768)) {
		/* переключение черной/белой шапки */
		if (current < (h - $('.header').height())) {
			$('.slider .carousel li').css('background-position', '50%' + (50 + current / 6) + '%');
			if (!body.hasClass('header-white')) {
				body.addClass('header-white');
			}
		} else {
			if (body.hasClass('header-white')) {
				body.removeClass('header-white');
			}
		}
	}
	if (!Modernizr.touch) {
		/* переключение свернутой/развернутой шапки */
		if (current > 50) {
			if (!body.hasClass('header-collapsed')) {
				body.addClass('header-collapsed');
			}
		} else {
			if (body.hasClass('header-collapsed')) {
				body.removeClass('header-collapsed');
			}
		}

		if (body.hasClass('page-slider')) {
			/* скролл до нужного места */
			if ((current > 1) && (current < (h - 1)) && !body.hasClass('scrolling')) {
				if (current <= lastScrollTop) {
					h = 0;
				}
				$('html, body').animate({
					scrollTop: h
				}, 500, 'swing', function () {
					scrollEnable();
					body.removeClass('scrolling');
				});
				scrollDisable();
				body.addClass('scrolling');
			}
		}
		lastScrollTop = current;
		if (body.hasClass('scrolling')) {
			return false;
		}
	}
}


function scrollPreventDefault(e) {
	e = e || window.event;
	if (e.preventDefault)
		e.preventDefault();
	e.returnValue = false;
}
function scrollKeydown(e) {
	// left: 37, up: 38, right: 39, down: 40,
	// spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
	var keys = [37, 38, 39, 40];
	for (var i = keys.length; i--;) {
		if (e.keyCode === keys[i]) {
			preventDefault(e);
			return;
		}
	}
}
function scrollWheel(e) {
	scrollPreventDefault(e);
}
function scrollEnable() {
	if (window.removeEventListener) {
		window.removeEventListener('DOMMouseScroll', scrollWheel, false);
	}
	window.onmousewheel = document.onmousewheel = document.onkeydown = null;
}
function scrollDisable() {
	if (window.addEventListener) {
		window.addEventListener('DOMMouseScroll', scrollWheel, false);
	}
	window.onmousewheel = document.onmousewheel = scrollWheel;
	document.onkeydown = scrollKeydown;
}
function showPopup(where) {
	var time = 500, body = $('body');
	if ($('.popup').is(':visible') > 0) {
		time = 0;
		$('html, body').animate({
			scrollTop: 0
		}, 200, 'swing');
	}
	$('.' + where).fadeIn(time, function () {
		$(this).addClass('popup-loaded');
		body.addClass('popup-open');
		if (body.hasClass('page-index')) {
			$.fn.fullpage.setAllowScrolling(false);
		}
		resizePopup();
	});
}
function hidePopups() {
	$('.popup').fadeOut(200, function () {
		$(this).removeClass('popup-loaded');
		if ($('body').hasClass('page-index')) {
			$.fn.fullpage.setAllowScrolling(true);
		}
	});
	$('body').removeClass('popup-open');

}
function resizePopup() {
	$('.popup-anons').each(function () {
		var hh = $(this).outerHeight() - 300;
		$('.anons', this).height(hh);
	});
}