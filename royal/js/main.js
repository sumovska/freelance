/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* Формы */
function initForms(scope) {
	if (typeof scope === 'undefined') scope = document;
	$('input, select', scope).styler({
		selectPlaceholder: ''
	});
}

/* Галерея в кабинете */
function initGallery(scope) {
	var slider;
	if (typeof scope === 'undefined') scope = document;
	$('.gallery:visible:not(.gallery-inited):not(.gallery-hidden)', scope).each(function (i) {
		slider = $('.carousel', this).bxSlider({
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
		initFancybox(this);
		$(this).addClass('gallery-inited');
	});
	if (typeof slider != 'undefined') return slider;
}

/* Всплывающие окна (Fancybox) */
function initFancybox(scope) {
	if (typeof scope === 'undefined') scope = document;
	$('.fancybox-popup', scope).fancybox({
		padding: 20,
		margin: 20,
		wrapCSS: 'fancybox-default',
		nextEffect: 'fade',
		prevEffect: 'fade',
		fitToView: true,
		beforeShow: function () {
			var wrap = $('.fancybox-wrap');
			initForms(wrap);
			initGallery(wrap);
			initTags(wrap);
			initNumbers(wrap);
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
	$('.fancybox-gallery', scope).fancybox({
		padding: 0,
		margin: 50,
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
}

/* Теги */
function initTags(scope) {
	if (typeof scope === 'undefined') scope = document;
	$('.tags:not(.inited)', scope).each(function () {
		var _self = $(this);
		$('.add a', _self).click(function () {
			$('<div class="selector"><select data-placeholder="Выберите&hellip;"><option value="" selected>Выберите&hellip;</option><option value="Верхняя одежда">Верхняя одежда</option><option value="Костюмы">Костюмы</option><option value="Трикотаж">Трикотаж</option></select><a href="#" class="button-close"></a></div>').insertAfter($(this).parent());
			initForms(_self);
			return false;
		});
		_self.on('change', '.selector select', function () {
			if ($(this).val()) {
				$('<span class="name"><span>' + $(this).val() + '</span><a href="#" class="button-close" title="Удалить"></a></span>').insertAfter($('.selector:last', _self));
				$(this).closest('.selector').remove();
			}
		});
		_self.on('mousedown', '.name .button-close', function () {
			$(this).closest('.name').fadeOut(function () {
				$(this).remove();
			});
			return false;
		});
		_self.on('mousedown', '.button-close', function () {
			$(this).closest('.selector').fadeOut(function () {
				$(this).remove();
			});
			return false;
		});
		_self.addClass('inited');
	});
	$('.image-loader:not(.inited)', scope).each(function () {
		function loader(current) {
			var reader = new FileReader(), img = $('<img alt="">');
			reader.onload = function (e) {
				$('<li/>').append(img.attr('src', e.target.result)).append('<a href="#" class="button-close"></a>').appendTo(gallery);
				if (typeof carousel != 'undefined') carousel.reloadSlider();
			};
			reader.readAsDataURL(current);
		}

		var _self = $(this), gallery = $('.gallery .carousel', _self), carousel;
		gallery.closest('.gallery').removeClass('gallery-hidden');
		carousel = initGallery(_self);
		if ($('li', carousel).length === 0) {
			gallery.closest('.gallery').addClass('gallery-hidden');
		}
		_self.on('change', '.file-add input:file', function () {
			var arr = $(this).prop('files');
			if (arr.length > 0) {
				$('li', gallery).remove();
				gallery.closest('.gallery').removeClass('gallery-hidden');
			}
			for (var i = 0; i < arr.length; i++) {
				loader(arr[i]);
			}
		});
		_self.on('mousedown', '.button-close', function () {
			$(this).closest('li').fadeOut(function () {
				$(this).remove();
				carousel.reloadSlider();
			});
			if ($('li', carousel).length === 0) {
				gallery.closest('.gallery').addClass('gallery-hidden');
			}
			return false;
		});
		_self.addClass('inited');
	});
}

function initNumbers(scope) {
	if (typeof scope === 'undefined') scope = document;
	$('.number', scope).each(function () {
		var input = $('input', this), up = $('.up', this), down = $('.down', this);
		input.keydown(function (e) {
			if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
				(e.keyCode == 65 && e.ctrlKey === true) ||
				(e.keyCode >= 35 && e.keyCode <= 39)) {
				return;
			}
			if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
				e.preventDefault();
			}
		});
		up.click(function () {
			if (+input.val() < 99) {
				input.val(+input.val() + 1);
			}
		});
		down.click(function () {
			if (+input.val() > 0) {
				input.val(+input.val() - 1);
			}
		});
	});
	$('.table-sizes').each(function() {
		$('.td-toggle', this).click(function() {
			$(this).closest('.tr').toggleClass('tr-active');
		});
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
	$('.block-item').each(function () {
		var _images = $('.images', this), _scroll = $('.images .scroll', this);
		$('.colors li a', this).click(function () {
			$(this).closest('li').toggleClass('active').siblings('.active').removeClass('active');
			return false;
		});
		$('.pic', _images).click(function () {
			_images.toggleClass('open');
			if (_images.is('.open')) {
				_scroll.height(+$('.container').height());
			} else {
				_scroll.removeAttr('style');
			}
			_scroll.mCustomScrollbar("update");
		});
		_scroll.mCustomScrollbar({
			axis: "y",
			scrollInertia: 100,
			scrollButtons: {enable: false},
			autoHideScrollbar: false,
			theme: "rounded-dark",
			autoExpandScrollbar: true
		});
		$(document).on('click touchstart', function (event) {
			var target = $(event.target);
			if ((target.closest('.images').length === 0) && (!target.is('.images'))) {
				_images.removeClass('open');
				_scroll.removeAttr('style');
			}
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

	/* Теги */
	initTags();

	/* Корзина */
	$('.table-order').each(function () {
		$(this).on('change', '.checkbox-toggle input', function () {
			console.log('a');
			$(this).closest('.table').find('.jq-checkbox:not(.checkbox-toggle) :checkbox').prop('checked', $(this).is(':checked')).change().trigger('refresh');
			return false;
		});
	});

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

	initNumbers();
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