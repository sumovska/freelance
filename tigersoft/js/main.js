/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

var carousels = [], slider = {};


function Slider(obj) {
	var _this = this;
	this.elem = $(obj);
	this.bar = $('.bar', this.elem);
	this.number = $('.num :input', this.elem);
	this.servers = $('.server :input', this.elem);
	this.total = $('.total var', this.elem);
	this.priceCount = function (num) {
		return (num <= 3) ? 3000 : (num <= 5) ? 3500 : Math.round((-2 * num * num + 645 * num + 250) / 10) * 10;
	};
	this.serverCount = function (num) {
		return num * 1200;
	};
	this.serverText = function (num) {
		var i = +num.slice(-1), txt;
		if (i === 1 && ((+_this.servers.val() < 10) || (+_this.servers.val() > 20))) {
			txt = 'сервер';
		} else if ((i > 1 && i < 5) && ((+_this.servers.val() < 10) || (+_this.servers.val() > 21))) {
			txt = 'сервера';
		} else {
			txt = 'серверов';
		}
		return num + ' ' + txt;
	};
	this.init = function () {
		this.bar.slider({
			min: 3,
			max: 100,
			value: this.number.val(),
			slide: function (event, ui) {
				_this.number.val(ui.value);
				_this.total.text(_this.priceCount(ui.value) + _this.serverCount(_this.servers.val()));
			}
		});
		this.number.attr('maxlength', 3).val(this.bar.slider('option', 'value')).keydown(function (event) {
			var key = window.event ? event.keyCode : event.which;
			if (!(event.keyCode === 8 || event.keyCode === 46 || event.keyCode === 37 || event.keyCode === 39)) {
				return !((key < 48 || key > 57) && (key < 96 || key > 105));
			}
		}).keyup(function () {
				_this.bar.slider('value', $(this).val());
				_this.total.text(_this.priceCount($(this).val()) + _this.serverCount(_this.servers.val()));
				return true;
			}).blur(function () {
				if ($(this).val() < _this.bar.slider('option', 'min')) {
					$(this).val(_this.bar.slider('option', 'min'));
				} else if ($(this).val() > _this.bar.slider('option', 'max')) {
					$(this).val(_this.bar.slider('option', 'max'));
				}
				_this.bar.slider('value', $(this).val());
				_this.total.text(_this.priceCount($(this).val()) + _this.serverCount(_this.servers.val()));
			});
		this.servers.val(0);
		this.total.text(this.priceCount(this.number.val()) + this.serverCount(this.servers.val()));
		$('.from var', this.elem).text(this.bar.slider('option', 'min'));
		$('.to var', this.elem).text(this.bar.slider('option', 'max'));
		$('.server .link', this.elem).click(function () {
			if (+_this.servers.val() === 0) {
				_this.servers.val(1);
				$(this).text('1 сервер').closest('.server').addClass('server-visible');
			} else {
				_this.servers.val(0);
				$(this).text('есть сервер?').closest('.server').removeClass('server-visible');
			}
			_this.total.text(_this.priceCount(_this.number.val()) + _this.serverCount(_this.servers.val()));
			return false;
		});
		$('.server .plus', this.elem).click(function () {
			if (+_this.servers.val() <= 100) {
				_this.servers.val(+_this.servers.val() + 1);
			}
			$(this).siblings('.link').text(_this.serverText(_this.servers.val()));
			_this.total.text(_this.priceCount(_this.number.val()) + _this.serverCount(_this.servers.val()));
			return false;
		});
		$('.server .minus', this.elem).click(function () {
			_this.servers.val(+_this.servers.val() - 1);
			if (+_this.servers.val() > 0) {
				$(this).siblings('.link').text(_this.serverText(_this.servers.val()));
			} else {
				$(this).siblings('.link').text('есть сервер?').closest('.server').removeClass('server-visible');
			}
			_this.total.text(_this.priceCount(_this.number.val()) + _this.serverCount(_this.servers.val()));
			return false;
		});
	};
}


$(document).ready(function () {
	$('.slider').each(function () {
		slider = new Slider(this);
		slider.init();
	});

	$('.nav').each(function () {
		$('a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1"), current = $(this), tab_active = $('.tab-active'), content = $('.content');
			if (!current.closest('ul').hasClass('animated')) {
				if (where !== 'contacts' && !current.closest('li').hasClass('active')) {
					if (!tab_active.hasClass('tab-' + where)) {
						current.closest('ul').addClass('animated');
						content.height(tab_active.outerHeight(true));
						if (where === 'support') {
							tab_active.stop().css({
								'position': 'absolute',
								'right': 'auto',
								'left': 0
							}).animate({
									left: '-970px'
								}, 400, function () {
									$(this).removeClass('tab-active').css('top', 'auto');
								});
							$('.tab-' + where).css({
								'right': (-content.width()) + 'px',
								'left': 'auto',
								'position': 'relative'
							}).addClass('tab-active').animate({
									right: 0
								}, 400, function () {
									current.closest('li').addClass('active').siblings('li.active').removeClass('active');
									current.closest('ul').removeClass('animated');
									$.each(carousels, function () {
										if (this.container.is(':visible') && !this.container.is('.inited')) {
											this.setup();
											this.container.addClass('inited');
										}
									});
								});
						} else if (where === 'service') {
							tab_active.stop().css({
								'position': 'absolute',
								'right': 0,
								'left': 'auto',
								'top': 0
							}).animate({
									right: (-content.width()) + 'px'
								}, 400, function () {
									$(this).removeClass('tab-active').css('top', 'auto');
								});
							$('.tab-' + where).css({
								'left': (-content.width()) + 'px',
								'right': 'auto',
								'position': 'relative'
							}).addClass('tab-active').animate({
									left: 0
								}, 400, function () {
									current.closest('li').addClass('active').siblings('li.active').removeClass('active');
									current.closest('ul').removeClass('animated');
								});
						}
						content.animate({
							height: $('.tab-' + where).outerHeight(true)
						}, 400, function () {
							$(this).height('auto');
						});
					} else {
						$.scrollTo('.header', 200, {
							easing: 'swing',
							onAfter: function () {
								current.closest('li').addClass('active').siblings('li.active').removeClass('active');
							}
						});
					}
				} else if (where === 'contacts') {
					$.scrollTo('#contacts', 800, {
						easing: 'swing',
						onAfter: function () {
							current.closest('li').addClass('active').siblings('li.active').removeClass('active');
						}
					});
				}
			}
			return false;
		});
	});

	$('.reviews').each(function () {
		$('.list', this).jcarousel({
			scroll: 1,
			wrap: 'both',
			buttonNextHTML: '<p></p>',
			buttonPrevHTML: '<p></p>',
			initCallback: function (carousel) {
				carousels.push(carousel);
				var current = $(carousel.container).closest('.carousel');
				current.append('<div class="carousel-prev"></div><div class="carousel-next"></div>');
			},
			itemFirstInCallback: function (carousel) {
				var before = 0, after = 0, current = $(carousel.container).closest('.carousel'), prev = current.find('.carousel-prev'), next = current.find('.carousel-next');
				if ((carousel.first - 1) === 0) {
					before = carousel.size();
				} else {
					before = carousel.first - 1;
				}
				if ((carousel.first + 1) > carousel.size()) {
					after = 1;
				} else {
					after = carousel.first + 1;
				}
				prev.html('');
				$(carousel.list[0]).children('li').eq(before - 1).find('.logo').clone(true, true).appendTo(prev);
				$('img', prev).css('margin-top', -Math.floor($('img', prev).outerHeight() / 2));
				$('img', prev).css('margin-left', -Math.floor($('img', prev).outerWidth() / 2));
				next.html('');
				$(carousel.list[0]).children('li').eq(after - 1).find('.logo').clone(true, true).appendTo(next);
				$('img', next).css('margin-top', -Math.floor($('img', next).outerHeight() / 2));
				$('img', next).css('margin-left', -Math.floor($('img', next).outerWidth() / 2));
			}
		});
	});

	$('.toggles').each(function () {
		$('.link a', this).click(function () {
			$(this).closest('.link').toggleClass('link-active').siblings('.space').slideToggle(100);
			if ($(this).closest('.link').hasClass('link-address')) {
				if ($(this).closest('.link').hasClass('link-active')) {
					$('.contacts-map').slideDown(200, function () {
						$.scrollTo('.contacts-map', 400, {
							easing: 'swing'
						});
						if ($('div', this).length < 1) {
							$(this).append('<div class="yandex-map" id="ymaps-map-id_13445345307809642955" style="width: 100%; height: 350px;"></div><script type="text/javascript">function fid_13445345307809642955(ymaps) {var map = new ymaps.Map("ymaps-map-id_13445345307809642955", {center: [30.321302999999958, 60.02252836955561],zoom: 15,type: "yandex#map"});map.controls.add("zoomControl").add("mapTools").add(new ymaps.control.TypeSelector(["yandex#map", "yandex#satellite", "yandex#hybrid", "yandex#publicMap"]));map.geoObjects.add(new ymaps.Placemark([30.321303, 60.021326], {balloonContent: "<strong>Тайгер софт</strong>"}, {preset: "twirl#lightblueDotIcon"}));};</script><script type="text/javascript" src="http://api-maps.yandex.ru/2.0/?coordorder=longlat&amp;load=package.full&amp;wizard=constructor&amp;lang=ru-RU&amp;onload=fid_13445345307809642955"></script>');
						}
					});
				} else {
					$('.contacts-map').slideUp(200);
				}
			}
			return false;
		});
	});

	$('.faq').each(function () {
		$('.list .question a', this).click(function () {
			$(this).closest('li').toggleClass('active');
			return false;
		});
	});

	$('.display').each(function () {
		var current = $(this);
		$('.on', current).show();
		$('.cursor', current).delay(1000).fadeIn(10, function () {
			$(this).fadeIn(10).delay(300).fadeOut(10).delay(300).fadeIn(10).delay(300).fadeOut(10).delay(300).fadeIn(10).delay(300).fadeOut(10).delay(300).fadeIn(10).delay(300).fadeOut(10);
			$(this).hide();
		});
		$('.title', current).delay(3500).slideDown(500, function () {
			$(this).show();
			$('.preloader', current).fadeIn(500);
			$('.step-1', current).fadeIn(800, function () {
				$(this).show().delay(2000).fadeOut(400, function () {
					$(this).hide();
					$('.step-2', current).fadeIn(800, function () {
						$(this).show().delay(2000).fadeOut(400, function () {
							$(this).hide();
							$('.step-3', current).fadeIn(800, function () {
								$(this).show().delay(2000).fadeOut(400, function () {
									$(this).hide();
									$('.cursor', current).hide();
									$('.step-4', current).fadeIn(800, function () {
										$('.preloader', current).fadeOut(500);
									});
								});
							});
						});
					});
				});
			});
		});
	});

	/* IE */
	if ($.browser.msie && $.browser.version < 9) {
		$('.howmuch .phone, .reviews .list li, .questions .phone, .wrap, .display, .why .list li.arrow, .support .list li.arrow, .questions').append('<i class="before"></i>');
		$('.why .list li.arrow').before('<div class="clear"></div>');
		if (window.PIE) {
			$('.search :input').each(function () {
				PIE.attach(this);
			});
		}
	}
});