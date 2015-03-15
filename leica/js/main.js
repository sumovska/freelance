/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* Поиск по тексту, независмый от регистра */
$.extend($.expr[":"], {
	"Contains": function (elem, i, match) {
		return (elem.textContent || elem.innerText || "").toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
	}
});

/* Загрузка страницы */
$(window).load(function () {

	/* Инициализация форм */
	$('input, select').styler();
	$('button, .link-red-border').append('<i class="before"></i><i class="after"></i>').addClass('inited');
	$('.link-red-mail').append('<i class="ico"></i>');

	/* Карусель на главной */
	$('.slider').each(function () {
		var _self = $(this);
		$('.carousel', this).addClass('carousel-inited').bxSlider({
			responsive: true,
			infiniteLoop: ($('.carousel li', _self).length > 1) ? true: false,
			preloadImages: 'all',
			adaptiveHeight: true,
			auto: true,
			pause: 5000,
			pager: ($('.carousel li', _self).length > 1) ? true: false,
			controls: ($('.carousel li', _self).length > 1) ? true: false
		}).find('.text').append('<i class="corner"></i>');
	});

	/* Карусель галереи */
	$('.gallery').each(function () {
		var _self = $(this), galleryCarousel;

		function initGallery() {
			_self.addClass('gallery-carousel');
			galleryCarousel = $('.carousel', _self).addClass('carousel-inited').bxSlider({
				infiniteLoop: false,
				responsive: true,
				minSlides: 3,
				maxSlides: 8,
				moveSlides: 1,
				slideWidth: 147,
				pager: false,
				hideControlOnEnd: true
			});
			console.log(galleryCarousel);
			_self.addClass('gallery-inited');
		}

		function stopGallery() {
			galleryCarousel.destroySlider();
			_self.removeClass('gallery-inited');
			$('.carousel', _self).removeClass('carousel-inited');
			_self.removeClass('gallery-carousel');
		}

		function viewGallery() {
			_self.removeClass('gallery-full');
			$('.carousel a', _self).each(function () {
				var src = $('img', this).prop('data-src');
				$('img', this).attr('src', src).removeAttr('data-src');
			});
		}

		$('.views', _self).each(function () {
			$('.view-1 a', this).click(function () {
				viewGallery();
				if (!_self.hasClass('gallery-inited')) {
					initGallery();
				}
				$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
				return false;
			});
			$('.view-2 a', this).click(function () {
				stopGallery();
				viewGallery();
				$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
				return false;
			});
			$('.view-3 a', this).click(function () {
				stopGallery();
				_self.addClass('gallery-full');
				$('.carousel a', _self).each(function () {
					var src = $('img', this).prop('src');
					$('img', this).attr('data-src', src).attr('src', $(this).prop('href'));
				});
				$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
				return false;
			});
		});
		if (_self.hasClass('gallery-carousel')) {
			initGallery();
		}
	});

	/* Галерея товара */
	$(".fancybox-media").fancybox({
		padding: 0,
		helpers: {
			media: {},
			title: {
				type: null
			},
			thumbs: {
				width: 72,
				height: 72,
				position: 'bottom'
			}
		}
	});

	/* Попап */
	$(".fancybox-popup").fancybox({
		autoSize: false,
		fitToView: false,
		width: 'auto',
		height: 'auto',
		padding: 0,
		wrapCSS: 'fancybox-blue'
	});

	/* Кнопки "в корзину", "оформить сразу" */
	$('.button-cart, .button-checkout').append('<i class="icon"></i>');

	/* Главное меню */
	$('.nav').each(function () {
		var _self = $(this);
		$('.toggle', this).click(function () {
			_self.children('ul').addClass('nav-fixed').fadeToggle();
		});
		$('ul', this).each(function () {
			$(this).children('li').children('ul').each(function () {
				$(this).parent('li').addClass('sub');
			});
			$(this).children('li.sub').hover(function () {
				if (!Modernizr.touch) {
					$(this).find('ul').stop(true).slideDown(200);
				}
				return false;
			}, function () {
				if (!Modernizr.touch) {
					$(this).find('ul').stop(true).slideUp(200);
				}
			});
		}).click(function () {
				if ($(this).is('.nav-fixed')) {
					$(this).fadeOut(function () {
						$(this).removeClass('nav-fixed');
					});
				}
			});
	});

	/* Дополнительное меню */
	$('.submenu').each(function () {
		var _self = $(this);
		window.submenu = {};
		submenu.self = $(this);
		submenu.sidebar = $('.sidebar');
		submenu.floating = false;
		submenu.anchor = false;
		submenu.anchors = [];
		submenu.active = 1;
		$(this).append('<a class="toggle" href="#"></a>');
		$('.toggle', this).click(function () {
			submenu.self.addClass('submenu-open')
			$('body').addClass('body-submenu-open')
			return false;
		});
		$(this).children('li').children('ul').each(function () {
			$(this).parent('li').addClass('sub');
		});
		$(this).find('a').click(function () {
			submenu.active = 0;
			$(this).parents('li').each(function () {
				submenu.active = submenu.active + $(this).index() + 1
			});
		});
		$(this).find('.sub').children('a').click(function () {
			$(this).siblings('ul').slideToggle(function () {
				$(this).closest('li.sub').toggleClass('open');
			});
			return false;
		});
		if (_self.hasClass('submenu-floating')) {
			submenu.floating = true;
			$(this).find('a').click(function () {
				submenuRefresh();
			});
		}
		if (_self.hasClass('submenu-anchor')) {
			submenu.anchor = true;
			$(this).find('a').click(function () {
				var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1"), d = 500, off = 0;
				d = Math.floor(Math.abs((+$(window).scrollTop() - +$(where).offset().top) * .6));
				if (d < 400) {
					d = 300;
				}
				if (d > 2000) {
					d = 2000;
				}
				if (+$(where).css('padding-top').split('px')[0] < 10) {
					off = -20;
				}
				$.scrollTo(where, {
					duration: d,
					easing: 'swing',
					offset: {top: off}
				});
				return false;
			});
		}
	});
	$('body').bind("click touchstart", function (e) {
		if ($(this).hasClass('body-submenu-open')) {
			if (($(e.target).closest('.submenu-open').length < 1)) {
				$('.submenu').removeClass('submenu-open');
				$(this).removeClass('body-submenu-open');
			}
		}
	});

	/* Выбор города */
	$('.header .city select').change(function () {
		$('.header .phone').find('.phone-' + $(this).val()).addClass('visible').siblings('.visible').removeClass('visible');
	});

	/* Всплывающие подсказки */
	$('.icons img, .question').each(function () {
		var a = 0;
		if ($(window).width() > 1600) {
			a = Math.floor(($(window).width() - 1600) / 2);
		}
		$(this).tooltipster({
			maxWidth: 180,
			animation: 'fade',
			position: 'right',
			delay: 100,
			offsetX: -8 - a,
			offsetY: 10
		});
	});

	/* Кнопка прокрутки навверх */
	$('.scroll-top').click(function () {
		$.scrollTo('.header', {
			duration: 500,
			easing: 'swing'
		});
		return false;
	});

	/* Пересчет корзины */
	$('.cart-block').each(function () {
		function refresh() {
			var total = 0, totalI = 0;
			$('.item:not(.deleted)', _self).each(function () {
				var price = $('.p', this), amount = $('.amount-text', this), totalItem = $('.s', this), amountText = $('.n', this), n = 0, t = 0;
				n = +amount.val();
				if (!n) {
					n = 1;
				}
				amountText.text(n);
				if (n === 1) {
					$('.one', this).addClass('one-hidden');
				} else {
					$('.one', this).removeClass('one-hidden');
				}
				t = +price.text() * n;
				totalItem.text(t);
				totalI = totalI + n;
				total = total + t;
			});
			$('.ti', _self).text(totalI);
			$('.t', _self).text(total);
		}

		var _self = $(this);
		refresh();
		$('.item', _self).each(function () {
			var _item = $(this);
			$('.delete, .restore', _item).click(function () {
				_item.toggleClass('deleted');
				if (_item.is('.deleted')) {
					$(".amount-text", _item).prop('disabled', true);
				} else {
					$(".amount-text", _item).removeProp('disabled');
				}
				refresh();
				return false;
			});
			$('.amount', _item).each(function () {
				var input = $(".amount-text", this);
				$(".plus", this).click(function () {
					var a = +input.val() + 1;
					if (!_item.hasClass('deleted')) {
						if ((a > 0) && (a < 100)) {
							input.val(a);
							refresh();
						}
					}
					return false;
				});
				$(".minus", _item).click(function () {
					var a = +input.val() - 1;
					if (!_item.hasClass('deleted')) {
						if ((a > 0) && (a < 100)) {
							input.val(a);
							refresh();
						}
					}
					return false;
				});
				//noinspection JSUnresolvedFunction
				input.keydown(function (e) {
					if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
						(e.keyCode == 65 && e.ctrlKey === true) ||
						(e.keyCode >= 35 && e.keyCode <= 39)) {
						return;
					}
					if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
						e.preventDefault();
					}
				}).keyup(function (e) {
						refresh();
					}).blur(function () {
						if ($(this).val() < 1) {
							$(this).val(1);
						}
						refresh();
					});
			});
		});
	});

	/* Табы в корзине */
	$('.tabs').each(function () {
		$('a', this).click(function () {
			var attr = $(this).attr('href').replace(/^.*#(.*)/, "$1"), where = $('.' + attr);
			$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
			where.removeClass('tab-hidden').find(':input').removeProp('disabled');
			where.siblings('.tab:not(.tab-hidden)').addClass('tab-hidden').find(':input').prop('disabled');
			return false;
		});
	});

	/* Список вакансий */
	$('.jobs .position').each(function () {
		var _self = $(this), inter;
		$('.heading a', this).click(function () {
			function startInterval() {
				submenuRefresh();
				inter = setTimeout(startInterval, 5);
			}

			if ($('.submenu').is(':visible')) {
				startInterval();
			}
			$('.description', _self).slideToggle(500, function () {
				_self.toggleClass('open');
				if ($('.submenu').is(':visible')) {
					clearTimeout(inter);
					submenuRefresh();
				}
			});
			return false;
		});
	});

	/* Медиатека на странице диллеры */
	$('.media-library .area').perfectScrollbar({
		suppressScrollX: true
	});

	/* Placeholder polyfill */
	$('input, textarea').placeholder();

	$('.header .search input:text').keyup(function () {
		var _self = $(this), a, res;

		$(this).siblings('.search-results').remove();
		if ($(this).val().length > 0) {
			a = '<ul class="search-results"><li><a href="#">овощи</a></li><li><a href="#">фрукты</a></li><li><a href="#">овощи</a></li><li><a href="#">овощи</a></li><li><a href="#">овощи</a></li></ul>';
			$(a).insertAfter(this);
		}
		res = _self.siblings('.search-results');
		res.find('a').click(function () {
			_self.val($(this).text());
			res.remove();
		});
	});

	if ((typeof google != 'undefined') && document.getElementById('office-map')) {
		initOfficeMap();
		initPartnersMap();
	}

	if ($.browser.msie) {
		if ($.browser.version < 10) {
			DoRotate(-360);
		}
	}

	$('.weekpicker tr').click(function () {
		window.location.href = '?date=' + $(this).find('td[date]:first').attr('date') + '-' + $(this).find('td[date]:last').attr('date');
		return false;
	});

	$('.partners .logos li').hover(function () {
		$(this).height($(this).height()).addClass('hover');
	}, function () {
		$(this).removeClass('hover');
	});

	submenuRefresh();
	$(window).resize();
});

function DoRotate(angle) {
	var $elem = $('.loading img');
	$({deg: 0}).animate({deg: angle}, {
		duration: 1000,
		easing: 'linear',
		step: function (now) {
			$elem.css({
				transform: 'rotate(' + now + 'deg)'
			});
		},
		complete: function () {
			DoRotate(angle);
		}
	});
}


/* Обновление плавающего меню */
function submenuRefresh() {
	submenuResize();
	submenuScroll();
}

/* Обновление плавающего меню по изменению размера окна */
function submenuResize() {
	if (typeof window.submenu != 'undefined') {
		if (submenu.floating === true) {
			if ($(window).width() > 1024) {
				submenu.self.width($('.sidebar').outerWidth());
			} else {
				submenu.self.removeProp('style');
			}
			submenu.triggerTop = +submenu.sidebar.offset().top - 20;
			submenu.offsetBottom = +$('.footer').outerHeight() + 23;
			submenu.triggerBottom = +$('body').outerHeight() - submenu.offsetBottom - +submenu.self.outerHeight(true);
		}
		if (submenu.anchor === true) {
			submenu.anchors = [];
			$('a:not(.toggle)', submenu.self).each(function () {
				var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1"), pos = 0;
				pos = Math.floor($(where).offset().top);
				if (+$(where).css('padding-top').split('px')[0] < 10) {
					pos = pos - 25;
				}
				submenu.anchors.push(pos);
			});
		}
	}
}

/* Обновление плавающего меню по скроллу окна */
function submenuScroll() {
	if (typeof window.submenu != 'undefined') {
		var y = $(window).scrollTop();
		if (submenu.floating === true) {
			if (y >= submenu.triggerTop) {
				submenu.self.addClass('submenu-fixed');
			} else {
				submenu.self.removeClass('submenu-fixed');
			}
			if (y >= submenu.triggerBottom) {
				submenu.self.addClass('submenu-fixed-bottom').css('bottom', submenu.offsetBottom);
			} else {
				submenu.self.removeClass('submenu-fixed-bottom').css('bottom', 'auto');
			}
		}
		if (submenu.anchor === true) {
			var i = 0;
			do {
				i = i + 1;
			} while ((i < submenu.anchors.length) && (submenu.anchors[i] <= y));
			if (submenu.active != i) {
				$('li.active', submenu.self).removeClass('active');
				$('li', submenu.self).eq(i - 1).addClass('active').parents('li').addClass('active');
				submenu.active = i;
			}
		}
	}
}

/* Обновление контента по изменению размера окна */
function contentResize() {
	/* Применения */
	$('.use-sections').each(function () {
		var min1 = 0, min2 = 0, _self = $(this);
		$('.area', this).height('auto');
		$('.col', this).each(function (index) {
			var h = $('.area', this).height();
			if (index < 4) {
				if (h > min1) {
					min1 = h;
				}
			} else {
				if (h > min2) {
					min2 = h;
				}
			}
		});
		$('.col', this).each(function (index) {
			var h = $('.area', this).height();
			if (index < 4) {
				$('.area', this).css('height', min1);
			} else {
				$('.area', this).css('height', min2);
			}
		});
	});

	/* Контакты */
	$('.contacts-small').each(function () {
		var min = 0, _self = $(this);
		$('.list-contacts-small', this).each(function (index) {
			var h = $(this).height();
			if (h > min) {
				min = h;
			}
		});
		$('.list-contacts-small', this).height(min);
	});
	if ((typeof window.eventCarousel != 'undefined') && ($(window).width() <= 1024)) {
		window.eventCarousel.destroySlider();
		delete window.eventCarousel;
		$('.events').removeClass('events-inited').find('*').removeProp('style');
		$('.events .carousel').removeClass('carousel-inited');
		$('.events .carousel-pager').remove();
		$('.events .bx-clone').remove();
	} else if ((typeof window.eventCarousel == 'undefined') && ($(window).width() > 1024)) {
		initEvents();
	}
}

function initEvents() {
	/* Карусель ключевых событий */
	$('.events').each(function () {
		var carousel = $('.carousel', this), pager = $('<ul class="carousel-pager"></ul>');
		pager.appendTo(this);
		carousel.children('li').each(function (index) {
			var li = $('<li></li>'), dots = $('<span class="dots"></span>');
			$('.list li', this).each(function () {
				$('<i></i>').appendTo(dots);
			});
			li.append('<a href="#" data-slide-index="' + index + '"></a>');
			$('a', li).append(dots).append('<span class="year">' + $('.year', this).text().split(' ')[0] + '</span>');
			li.appendTo(pager);
		});
		$(this).addClass('events-inited');
		carousel = carousel.addClass('carousel-inited').bxSlider({
			responsive: true,
			infiniteLoop: true,
			preloadImages: 'all',
			controls: false,
			pagerCustom: pager,
			auto: true,
			autoHover: true,
			pause: 5000
		});
		submenuRefresh();
		window.eventCarousel = carousel;
	});
}


//инициализация карты проезда в офис в контактах
function initOfficeMap() {
	//построение маршрута от метро Алексеевская до офиса
	function getRouteToMetro() {
		var request = {
			origin: metroCoords,
			destination: officeMapCoords,
			travelMode: google.maps.TravelMode.TRANSIT
		};

		directionsService.route(request, function (response, status) {
			if (status == google.maps.DirectionsStatus.OK) {
				directionsDisplay.setDirections(response);
			}
		});
	}

	var geoLocationActive = false;

	var officeMapCoords = new google.maps.LatLng(55.8103102, 37.6562394);
	var metroCoords = new google.maps.LatLng(55.807779, 37.638693); //метро Алексеевская

	var officeMapOptions = {
		center: officeMapCoords,
		zoom: 15,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	//сервис маршрутизации – строим путь к офису
	var directionsService = new google.maps.DirectionsService();
	var directionsDisplay = new google.maps.DirectionsRenderer();

	var officeMap = new google.maps.Map(document.getElementById("office-map"), officeMapOptions);

	var infoWindowOffice = new InfoBox({
		content: '<div id="address-office" class="infobox">улица Павла Корчагина, дом 2</div>',
		disableAutoPan: false,
		maxWidth: 180,
		alignBottom: true,
		pixelOffset: new google.maps.Size(-90, -20),
		zIndex: null,
		boxStyle: {
			width: "180px"
		},
		closeBoxMargin: "5px",
		closeBoxURL: "http://www.google.com/intl/en_us/mapfiles/close.gif",
		infoBoxClearance: new google.maps.Size(1, 1)
	});

	infoWindowOffice.setPosition(officeMapCoords);
	infoWindowOffice.open(officeMap);

	directionsDisplay.setOptions({
		draggable: true,
		suppressInfoWindows: true
	});

	directionsDisplay.setMap(officeMap);

	//используем geolocation API, если есть и пользователь разрешил определение
	//то при нахождении в Москве строим путь до офиса
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			geoLocationActive = true;

			var geocoder = new google.maps.Geocoder();

			var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
			var city = '';

			//получаем город, чтобы не строить маршурт из Новособирска в Москву на улицу Павла Корчагина
			geocoder.geocode({'latLng': pos}, function (results, status) {
				if (status == google.maps.GeocoderStatus.OK && results[0]) {
					for (var i = 0; i < results[0].address_components.length; i += 1) {

						if (results[0].address_components[i].types[0] == "locality") {
							city = results[0].address_components[i].long_name;
							break;
						}
					}

					if (city && city == 'Moscow') {
						officeMap.setCenter(pos);

						var request = {
							origin: pos,
							destination: officeMapCoords,
							travelMode: google.maps.TravelMode.DRIVING
						};

						directionsService.route(request, function (response, status) {
							if (status == google.maps.DirectionsStatus.OK) {
								if (response.routes[0].legs[0].distance.value > 500) {
									directionsDisplay.setDirections(response);
								} else {
									//для тех, кто открывает из самого офиса показываем также путь от метро
									getRouteToMetro();
								}
							}
						});
					} else
						getRouteToMetro();
				}
			});
		});
	}

	setTimeout(function () {
		if (!geoLocationActive) {
			getRouteToMetro();
		}
	}, 5000);

}

function infoContent(text, id) {
	var result = document.createElement('div');
	result.className = 'infobox';

	if (id) {
		result.id = id;
	}

	result.innerHTML = text;

	return result;
}

//инициализация карты партнеров и филиалов
function initPartnersMap() {
	var markerSize = { x: 18, y: 31 };

	//===============================================================
	//делаем прототип метки с цифрок на маркер

	google.maps.Marker.prototype.setLabel = function (label) {
		this.label = new MarkerLabel({
			map: this.map,
			marker: this,
			text: label
		});

		this.label.bindTo('position', this, 'position');
	};

	var MarkerLabel = function (options) {
		this.setValues(options);
		this.span = document.createElement('span');
		this.span.className = 'map-marker-label';
	};

	MarkerLabel.prototype = $.extend(new google.maps.OverlayView(), {
		onAdd: function () {
			this.getPanes().overlayImage.appendChild(this.span);
			var self = this;

			this.listeners = [
				google.maps.event.addListener(this, 'position_changed', function () {
					self.draw();
				}),
				google.maps.event.addListener(this.marker, 'visible_changed', function () {
					//при статуса маркера отображается/скрывается метка
					//статус видимости маркера добавлен в MarkerClusterer кастомно в addMarker!
					self.span.style.display = this.visible ? null : 'none';
				})
			];
		},
		draw: function () {
			var text = String(this.get('text'));

			var position = this.getProjection().fromLatLngToDivPixel(this.get('position'));
			this.span.innerHTML = text;
			this.span.style.left = (position.x - (markerSize.x / 2)) - (text.length * 3) + 17 + 'px';
			this.span.style.top = (position.y - markerSize.y ) + 'px';
		}
	});
	//===============================================================


	var partnersMap = new google.maps.Map(document.getElementById('partners-map'), {
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		scrollwheel: false,
		zoom: 5,
		center: new google.maps.LatLng(55.8103102, 37.6562394)
	});

	var infobox = new InfoBox({
		content: '',
		disableAutoPan: false,
		alignBottom: true,
		maxWidth: 250,
		pixelOffset: new google.maps.Size(-115, -40),
		zIndex: null,
		boxStyle: {
			width: "250px"
		},
		closeBoxMargin: "12px 4px 2px 2px",
		closeBoxURL: "http://www.google.com/intl/en_us/mapfiles/close.gif",
		infoBoxClearance: new google.maps.Size(1, 1)
	});

	var markerClusterer;
	var points = [];
	$('.list-contacts-small').each(function () {
		var point = $(this),
			pos = point.data('coords').split(',');

		var marker = new google.maps.Marker({
			map: partnersMap,
			position: new google.maps.LatLng(pos[0], pos[1]),
			shadow: null,
			icon: new google.maps.MarkerImage('/img/pin_' + point.data('address-type') + '.png',
				new google.maps.Size(36, 62),
				new google.maps.Point(0, 0),
				new google.maps.Point(0, 31),
				new google.maps.Size(18, 31)
			),
			label: $('.n', point).html(),
			title: $('.ico-address', point).html()
		});

		google.maps.event.addListener(marker, 'click', function () {
			infobox.setContent(infoContent(this.title));
			infobox.open(partnersMap, this);

			partnersMap.panTo(this.position);
		});

		points.push(marker);
	});

	//стиль для объдиняющего маркера
	markerClusterer = new MarkerClusterer(partnersMap, points, {
		maxZoom: 10,
		styles: [
			{
				url: '/img/pin_city.png',
				height: 45,
				width: 28,
				anchor: [10, 45],
				textColor: '#fff',
				textSize: 12,
				bgSize: '27px 45px'
			}
		]
	});

	//центрируем карту по маркерам
	var latlngbounds = new google.maps.LatLngBounds();
	points.forEach(function (p) {
		latlngbounds.extend(p.position);
	});
	partnersMap.setCenter(latlngbounds.getCenter());
	partnersMap.fitBounds(latlngbounds);
}

function tooltipResize() {
	/* Всплывающие подсказки */
	$('.icons img, .question').each(function () {
		var a = 0;
		if ($(window).width() > 1600) {
			a = Math.floor(($(window).width() - 1600) / 2);
		}
		$(this).tooltipster('destroy');
		$(this).tooltipster({
			maxWidth: 180,
			animation: 'fade',
			position: 'right',
			delay: 100,
			offsetX: -8 - a,
			offsetY: 10
		});
	});
}

/* Ресайз страницы */
$(window).resize(function () {
	submenuResize();
	contentResize();
	tooltipResize();
	$('.partners .logos li img').removeAttr('style');
});

/* Скролл страницы */
$(window).scroll(function () {
	submenuScroll();
});