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
				if ((target.closest('.nav-catalog').length === 0) && (!target.is('.nav-catalog'))) {
					$(_self).removeClass('open').removeClass('visible');
				}
			});
		});
		$('.search', this).each(function () {
			var _self = $(this);
			var search = new Bloodhound({
				datumTokenizer: function (datum) {
					return Bloodhound.tokenizers.whitespace(datum.value);
				},
				queryTokenizer: Bloodhound.tokenizers.whitespace,
				remote: {
					url: 'http://api.themoviedb.org/3/search/movie?query=%QUERY&api_key=470fd2ec8853e25d2f8d86f685d2270e',
					filter: function (movies) {
						// Map the remote source JSON array to a JavaScript object array
						return $.map(movies.results, function (movie) {
							return {
								value: movie.original_title
							};
						});
					}
				}
			});

			search.initialize();

			$('.typeahead', this).typeahead({
					hint: true,
					highlight: true,
					minLength: 1
				},
				{
					name: 'search',
					displayKey: 'value',
					source: search.ttAdapter()
				}).on('focus', function () {
					_self.addClass('focus');
				}).on('blue', function () {
					_self.removeClass('focus');
				});
		});
	});


	/* Контакты */
	$('.contacts').each(function () {
		$('.list', this).eq(0).each(function () {
			var tmp;
			tmp = $('.list', this).closest('li').clone();
			tmp = $('<ul class="list"></ul>').append(tmp);
			tmp.addClass('list-additional').insertAfter(this);
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


	/* Каталог + карусель */
	$('.catalog').each(function () {
		var _catalog = $(this);
		if ($(this).is('.catalog-small-carousel')) {
			$(this).on('init', function (slick) {
				_catalog.prevAll('.h4-divide').addClass('h4-divide-prevnext').each(function () {
					var w = +Math.floor($(this).find('.in').width() / 2) - 13;
					$('.slick-prev', _catalog).css('margin-left', w + 'px');
					$('.slick-next', _catalog).css('margin-left', w + 29 + 'px');
				});
			}).slick({
				variableWidth: true,
				adaptiveHeight: true,
				swipeToSlide: true,
				touchThreshold: 10,
				slidesToShow: 5,
				infinite: false,
				arrows: true,
				prevArrow: '<span data-role="none" class="slick-prev" aria-label="previous"></span>',
				nextArrow: '<span data-role="none" class="slick-next" aria-label="next"></span>',
				responsive: [
					{
						breakpoint: 1599,
						settings: {
							slidesToShow: 4
						}
					}, {
						breakpoint: 1279,
						settings: {
							slidesToShow: 3
						}
					}, {
						breakpoint: 999,
						settings: {
							slidesToShow: 1,
							infinite: true,
							arrows: false,
							centerMode: true
						}
					}
				]
			});
		} else {
			$('.item', this).on('mouseenter', function () {
				$(this).height($(this).height());
				$(this).addClass('visible');
			}).on('mouseleave', function () {
				var _item = $(this);
				setTimeout(function () {
					_item.removeAttr('style').removeClass('visible');
				}, 250);
			});
		}
	});


	/* Карусель статей */
	$('.articles').each(function () {
		$('.carousel', this).slick({
			infinite: true,
			variableWidth: true,
			mobileFirst: true,
			arrows: false,
			centerMode: true,
			slidesToShow: 2,
			swipeToSlide: true,
			touchThreshold: 10,
			responsive: [
				{
					breakpoint: 999,
					settings: 'unslick'
				}
			]
		});
	});

	/* Табы */
	$('.tabs').each(function () {
		$('.tabs-list .link', this).each(function () {
			$('a', this).click(function () {
				var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
				$(this).closest('.link').addClass('link-active').siblings('.link-active').removeClass('link-active');
				$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
				return false;
			});
		});
		$('.tabs-list-carousel', this).slick({
			slidesToScroll: 1,
			slidesToShow: 4,
			infinite: true,
			variableWidth: true,
			mobileFirst: true,
			arrows: false,
			swipeToSlide: true,
			touchThreshold: 10,
			responsive: [
				{
					breakpoint: 999,
					settings: 'unslick'
				},
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
	});


	$('.featured-list-carousel').slick({
		infinite: true,
		variableWidth: true,
		mobileFirst: true,
		arrows: false,
		swipeToSlide: true,
		touchThreshold: 10,
		responsive: [
			{
				breakpoint: 999,
				settings: 'unslick'
			}
		]
	});


	/* Сворачивание/разворачивание фильтра */
	$('.filter').each(function () {
		$('.toggle', this).on('click', function () {
			$(this).toggleClass('toggle-active').siblings('form').toggle(200);
		});
		$('.h5 .switch', this).on('click', function () {
			$(this).closest('.h5').toggleClass('h5-active').siblings('.entry-in').fadeToggle(200);
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
		} else {

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

});

