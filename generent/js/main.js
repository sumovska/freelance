/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true, node: true */
/*global window, console, document, $, jQuery, PIE, initialize, styler */

function initForms() {
	$('input, select').styler();
}

/* On document ready */
$(document).ready(function () {

	/* Формы */
	initForms();

	/* Табы */
	$('.tabs').each(function () {
		$('li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$('#' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Карусель маленькая (в сайдбаре) */
	$('.slider-small').each(function () {
		$('.slider-in').slick({
			arrows: false,
			dots: true
		});
		$('.slick-dots button').remove();
		$('.slick-dots li', this).append('<span class="dots"></span>');
	});

	/* Карусель на главной */
	$('.slider').each(function () {
		$('.slider-in').slick({
			arrows: false,
			dots: true
		});
		$('.slick-dots button').remove();
		$('.slick-dots li', this).append('<span class="dots"></span>');
	});

	/* Карусель на главной */
	$('.index').each(function () {
		$('.carousel').slick({
			prevArrow: '<span class="slick-prev" aria-label="previous"></span>',
			nextArrow: '<span class="slick-next" aria-label="next"></span>',
			dots: true
		});
		$('.slick-dots button').remove();
		$('.slick-dots li', this).append('<span class="dots"></span>');
	});

	/* Карусель производителей */
	$('.maker').each(function () {
		$(this).slick({
			slidesToShow: 6,
			slidesToScroll: 1,
			prevArrow: '<span class="slick-prev" aria-label="previous"></span>',
			nextArrow: '<span class="slick-next" aria-label="next"></span>',
			dots: true,
			responsive: [
				{
					breakpoint: 999,
					settings: {
						slidesToShow: 4
					}
				}, {
					breakpoint: 480,
					settings: {
						slidesToShow: 2
					}
				}
			]
		});
		$('.slick-dots button').remove();
		$('.slick-dots li', this).append('<span class="dots"></span>');
	});

	/* Выпадающее меню */
	$('.header', this).append('<span class="toggle"></span>');
	$('.toggle', this).click(function (event) {
		$(this).toggleClass('open');
		$('.nav').each(function () {
			var _self = $(this);
			$(this).toggleClass('open');
			if (_self.hasClass('open')) {
				$(document).on('click touchstart', closeMenu);
			} else {
				$(document).off('click touchstart', closeMenu);
			}
			event.preventDefault();
		});
	});

	/*  Подменю */
	$('.nav-in > li', this).each(function () {
		if ($(this).children('ul').length > 0) {
			$(this).addClass('sub');
		}
		$(this).children('a').on('click', function (event) {
			if ($(window).width() <= 999) {
				$(this).closest('li').toggleClass('open');
				event.preventDefault();
			}
		});
	});


	/*$('.clients').each(function () {
	 $('.item', this).on('mouseenter', function () {
	 $(this).animate(
	 $(this).find('.describe').fadeIn()
	 )
	 }).on('mouseleave', function () {
	 $(this).removeClass('visible').find('.describe').fadeOut();
	 });
	 });*/

	/*  Информационный список */
	$('.info-list').each(function () {
		$('.heading', this).click(function () {
			$(this).toggleClass('open').siblings('.in').slideToggle(200);
			return false;
		});
	});

	/* Разделы */
	$('.sections').each(function () {
		$(this).on('click', '.sections-in li a', function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('#' + where).removeClass('section-hidden').siblings('.section').addClass('section-hidden');
			return false;
		});
	});

	/* Прокрутка */
	$('.slider-energy').each(function () {
		$('.item', this).noUiSlider({
			start: [10, 1300],
			step: 5,
			behaviour: 'drag',
			connect: true,
			range: {
				'min': 10,
				'25%': 625,
				'50%': 1250,
				'75': 1875,
				'max': 2500
			},
			format: wNumb({
				decimals: 0
			})
		});
		$('.item', this).Link('lower').to($('.from', this)).Link('upper').to($('.to', this));
	});

	/* К сравнению */
	$('.describe', this).on('change', 'label', function () {
		var _self = $(this);
		if ($('input', this).is(':checked')) {
			$(this).addClass('checked');
		} else {
			$(this).removeClass('checked');
		}
	});

	/* Слайдер товара */
	$('.slider-item').each(function () {
		$('.slider-for').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			asNavFor: '.slider-nav'
		});
		$('.slider-nav').each(function () {
			$(this).slick({
				slidesToScroll: 1,
				centerPadding: '0',
				slidesToShow: 3,
				vertical: true,
				asNavFor: '.slider-for',
				arrows: false,
				centerMode: true,
				focusOnSelect: true
			});
			$('.slick-slide', this).removeClass('slick-active');
			$('.slick-slide', this).eq(0).addClass('slick-active');
		});
	});

	/* Фильтр */
	$('.wrapper-catalog').each(function () {
		$('.aside').append("<div class='toggle'><span class='toggle-in'>Cкрыть расширенный фильтр</span></div>");
		$('.toggle', this).click(function () {
			var _self = $(this);
			$(this).parentsUntil().closest('.wrapper-container').toggleClass('open');
			/*_self.closest('.aside').fadeToggle(200);*/

		})
	});

});

