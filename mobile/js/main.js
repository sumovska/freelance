/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();

	/* Карусель на главной */
	$('.index').each(function () {
		$('.carousel', this).slick({
			adaptiveHeight: false,
			dots: true,
			arrows: false,
			customPaging: function (slider, i) {
				return '<span data-role="none">' + (i + 1) + '</span>';
			}
		});
	});

	/*  Всплывающие окна (Fancybox) */
	$('.fancybox-popup').fancybox({
		padding: 0
	});

	/* Слайдер с навигацией */
	$('.slider').each(function () {
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
				asNavFor: '.slider-for',
				arrows: false,
				centerMode: true,
				focusOnSelect: true
			});
			$('.slick-slide', this).removeClass('slick-active');
			$('.slick-slide', this).eq(0).addClass('slick-active');
		});
	});

	/* Ценовая прокрутка */
	$('.price-slider').each(function () {
		$('.item', this).noUiSlider({
			start: [1200, 6000],
			step: 1,
			behaviour: 'drag',
			connect: true,
			range: {
				'min': 0,
				'max': 30000
			},
			format: wNumb({
				decimals: 0
			})
		});
		$('.item', this).Link('lower').to($('.from', this)).Link('upper').to($('.to', this));
	});

	function runSlider() {
		if ($(window).width() > 768) {
			$('.catalog-small').unslick("unslick");
		} else {
			$('.catalog-small').slick({
				slidesToScroll: 1,
				slidesToShow: 2,
				variableWidth: true,
				centerMode: true,
				arrows: false,
				responsive: [
					{
						breakpoint: 600,
						settings: {
							slidesToShow: 1,
							centerMode: true
						}
					}
				]
			});
			$('.offers').slick({
				slidesToScroll: 1,
				slidesToShow: 2,
				infinite: true,
				centerMode: true,
				arrows: false,
				responsive: [
					{
						breakpoint: 600,
						settings: {
							slidesToShow: 1,
							centerMode: true
						}
					}
				]
			});
			$('.featured-list').slick({
				slidesToScroll: 1,
				slidesToShow: 4,
				arrows: false,
				variableWidth: true
			});
			$('.tabs-list').slick({
				slidesToShow: 5,
				variableWidth: true,
				prevArrow: '<span data-role="none" class="slick-prev" aria-label="previous"></span>',
				nextArrow: '<span data-role="none" class="slick-next" aria-label="next"></span>'
			});
			$('.slick-cloned').removeClass('slick-active');
		}
	}

	runSlider();
	var r;

	$(window).resize(function () {
		clearTimeout(r);
		r = setTimeout(runSlider, 500);
	});

	/* Сворачивание/разворачивание фильтра */
	$('.filter').each(function () {
		$('.open').click(function () {
			$(this).closest('.toggle').addClass('toggle-active').siblings('form').fadeIn(200);
		});
		$('.close').click(function () {
			$(this).closest('.toggle').removeClass('toggle-active').siblings('form').fadeOut(200);
		});
		$('.h5 .switch').click(function () {
			$(this).closest('.h5').toggleClass('h5-active').siblings('.list', '.price-slider').fadeToggle(200);
		});
	});

	/* Табы */
	$('.tabs').each(function () {
		$('.tabs-list li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

});

