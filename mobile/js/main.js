/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true, node: true */
/*global window, console, document, $, jQuery, PIE, initialize, styler */

/* On document ready */
$(document).ready(function () {

	/* Формы */
	$('input, select').styler();


	/* Выпадающее меню */
	$('.nav').each(function () {
		function closeMenu(event) {
			var target = $(event.target);
			if ((target.closest('.nav').length === 0) && (!target.is('.nav'))) {
				$('.open', _nav).removeClass('open').removeClass('visible');
				$(document).off('click touchstart', closeMenu);
			}
		}

		var _nav = $(this);

		_nav.on('click', '.sub > a', function (event) {
			$(this).closest('li').each(function () {
				var _this = $(this);
				_this.toggleClass('open');
				if (_this.is('.open')) {
					$(document).on('click touchstart', closeMenu);
				}
				setTimeout(function () {
					_this.toggleClass('visible');
				}, 100);
			});
			event.preventDefault();
		});
	});


	/* Шапка */
	$('.header').each(function () {
		function closeLogin(event) {
			var target = $(event.target);
			if ((target.closest('.login').length === 0) && (!target.is('.login'))) {
				$('.open', _login).removeClass('open').removeClass('visible');
				$(document).off('click touchstart', closeLogin);
			}
		}

		function closeNav(event) {
			var target = $(event.target);
			if ((target.closest('.nav-catalog').length === 0) && (!target.is('.nav-catalog'))) {
				$(_nav).removeClass('open').removeClass('visible');
				$(document).off('click touchstart', closeNav);
			}
		}

		var _login = $('.login', this), _nav = $('.nav-catalog', this), _search = $('.search', this);

		_login.each(function () {
			$(this).on('click', '.sub > a', function (event) {
				$(this).closest('li').each(function () {
					var _this = $(this);
					_this.toggleClass('open');
					if (_this.is('.open')) {
						$(document).on('click touchstart', closeLogin);
					}
					setTimeout(function () {
						_this.toggleClass('visible');
					}, 100);
				});
				event.preventDefault();
			});
		});

		_nav.each(function () {
			$(this).on('click', '.link', function (event) {
				_nav.toggleClass('open');
				if (_nav.is('.open')) {
					$(document).on('click touchstart', closeNav);
				}
				setTimeout(function () {
					_nav.toggleClass('visible');
				}, 100);
				event.preventDefault();
			});
		});

		_search.each(function () {
			//noinspection JSUnusedGlobalSymbols
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
					_search.addClass('focus');
				}).on('blur', function () {
					_search.removeClass('focus');
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
		//noinspection JSUnusedGlobalSymbols
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
			slidesToShow: 5,
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
		$(this).on('click', '.tabs-list .link a', function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('.link').addClass('link-active').siblings('.link-active').removeClass('link-active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
		$('.tabs-list-carousel', this).slick({
			slidesToScroll: 1,
			slidesToShow: 4,
			infinite: false,
			variableWidth: true,
			mobileFirst: true,
			arrows: true,
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

	/* Хлебные крошки */
	$('.breadcrumbs').each(function () {
		$(this).on('click', '.back', function () {
			history.back();
			return false;
		});
	});


	/* Сворачивание/разворачивание фильтра */
	$('.filter').each(function () {
		_filter = $(this);
		$('.toggle', this).on('click', function () {
			$(this).toggleClass('toggle-active');
			_filter.toggleClass('open');
		});
		$('.h5', this).on('click', function () {
			$(this).closest('.entry').toggleClass('open');
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

	/* Count */
	$('.count').each(function () {
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
			if (+input.val() < 10) {
				input.val(+input.val() + 1);
			}
		});
		down.click(function () {
			if (+input.val() > 0) {
				input.val(+input.val() - 1);
			}
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

	/* Боковая навигация */
	$('.sidenav').each(function () {
		_nav = $(this);
		$(this).on('click', 'li.active a', function () {
			_nav.toggleClass('open');
			return false;
		});
	});

	/* Форма доставки */
	$('.block-delivery').each(function () {
		$('label.radio', this).click(function () {
			var _self = $(this);
			$(this).parent(this).siblings('.delivery-in', this).slideToggle(200);
			_self.parentsUntil().siblings('.block-delivery').find('.delivery-in', this).slideUp(200);
		});
	});

	/* Изменение пароля */
	$('.password', this).click(function () {
		$(this).parent(this).siblings('.form-in').slideToggle(200);
		return false;
	});

	/* Таблица заказов */
	$('tr.order', this).click(function () {
		var _self = $(this);
		$(this).toggleClass('open');
		$(this).nextUntil('.order', '.hidden').slideToggle(200);
	});

	/* Добавлено в корзину */
	$('.block-item .to-cart', this).click(function(){
		$(this).html("В корзине").addClass('added');
		return false;
	});

});

