/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Формы */
	$('input, select').styler();


	/* Выпадающее меню */
	$('.nav').each(function () {
		var _self = $(this);
		$(this).find('.sub > a').click(function () {
			$(this).closest('li').each(function () {
				var _this = $(this);
				_this.toggleClass('open');
				setTimeout(function () {
					_this.toggleClass('visible');
				}, 100);
			});
			return false;
		});
		$(document).on('click touchstart', function (event) {
			var target = $(event.target);
			if ((target.closest('.nav').length === 0) && (!target.is('.nav'))) {
				$('.open', _self).removeClass('open').removeClass('visible');
			}
		});
	});


	/* Шапка */
	$('.header').each(function () {
		$('.login', this).each(function () {
			var _self = $(this);
			$('.sub > a', this).on('click', function () {
				$(this).closest('li').each(function () {
					var _this = $(this);
					_this.toggleClass('open');
					setTimeout(function () {
						_this.toggleClass('visible');
					}, 100);
				});
				return false;
			});
			$(document).on('click touchstart', function (event) {
				var target = $(event.target);
				if ((target.closest('.login').length === 0) && (!target.is('.login'))) {
					$('.open', _self).removeClass('open').removeClass('visible');
				}
			});
		});
		$('.nav-catalog', this).each(function () {
			var _self = $(this);
			$('.link', this).on('click', function () {
				_self.toggleClass('open');
				setTimeout(function () {
					_self.toggleClass('visible');
				}, 100);
				return false;
			});
			$(document).on('click touchstart', function (event) {
				var target = $(event.target);
				console.log(event.target);
				if ((target.closest('.nav-catalog').length === 0) && (!target.is('.nav-catalog'))) {
					$(_self).removeClass('open').removeClass('visible');
				}
			});
		});
	});


	/* Контакты */
	$('.contacts').each(function () {
		$('.list', this).eq(0).each(function () {
			$('.list', this).clone().addClass('list-additional').insertAfter(this);
		});
	});


	/* Карусель на главной */
	$('.index').each(function () {
		$('.carousel', this).slick({
			dots: true,
			arrows: false,
			autoplay: true,
			autoplaySpeed: 5000,
			infinite: true,
			adaptiveHeight: false,
			customPaging: function (slider, i) {
				return '<span data-role="none">' + (i + 1) + '</span>';
			}
		});
	});


	/*  Всплывающие окна (Fancybox) */
	$('.fancybox').fancybox({
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
		if ($(window).width() > 999) {
			$('.catalog-small-carosel').unslick();
			$('.articles .carousel').unslick();
			$('.tabs-list-carousel').unslick();
			$('.featured-list-carousel').unslick();
		} else {
			$('.catalog-small-carousel').slick({
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
			$('.offers .carousel').slick({
				slidesToScroll: 1,
				slidesToShow: 2,
				infinite: true,
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
			$('.tabs-list-carousel').slick({
				slidesToScroll: 1,
				slidesToShow: 4,
				variableWidth: true,
				responsive: [
					{
						breakpoint: 600,
						settings: {
							slidesToShow: 2
						}
					}
				],
				prevArrow: '<span data-role="none" class="slick-prev" aria-label="previous"></span>',
				nextArrow: '<span data-role="none" class="slick-next" aria-label="next"></span>'
			});
			$('.featured-list-carousel').slick({
				slidesToScroll: 1,
				slidesToShow: 4,
				arrows: false,
				variableWidth: true
			});
			$('.slick-cloned').removeClass('slick-active');
			$('.sidenav').each(function () {
				$('li.active').click(function () {
					$(this).siblings('li').toggle();
					return false;
				});
			});
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
		$('.toggle').click(function () {
			$(this).toggleClass('toggle-active').siblings('form').toggle(200);
		});
		$('.h5 .switch').click(function () {
			$(this).closest('.h5').toggleClass('h5-active').siblings('.entry-in').fadeToggle(200);
		});

	});

	/* Табы */
	$('.tabs-list .link').each(function () {
		$('a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('.link').addClass('link-active').siblings('.link-active').removeClass('link-active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

});

