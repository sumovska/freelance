/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

function resizeWindow() {
	var w = Math.floor(($(window).width() - $('.footer .wrapper').eq(0).width()) / 2), c = $('.content').eq(0).outerWidth();
	if (w < 0) {
		w = 0;
	}
	if (+$(window).width() > 1279) {
		$('.repair-area, .choose').width(c + w - 290);
		$('.grey-table').width(c + w - 310);
		$('.col-left').removeAttr('style');
		$('.col-right .faq').width(c + w - 249);
		$('.green .bg').width(w + 41);
	} else {
		$('.repair-area, .choose').width(c + w - 41);
		$('.grey-table').width(c + w - 61);
		$('.col-left').width(c + w - 54);
		$('.col-right .faq').width(c + w);
		$('.green .bg').width(w);
	}
	if (+$(window).width() > 1023) {
		$('.map').width(c + w);
		$('.feedback').width(c + w - 34);
	} else {
		$('.map').width(c + w + 10);
		$('.feedback').width(c + w - 24);
	}
	$('.black-area .bg').width(c + w);
}


var myMap;
function initMap() {
	var mLat = $('#CompanyLat').val();
	var mLng = $('#CompanyLng').val();
	myMap = new ymaps.Map("map", {
		center: [mLat, mLng],
		zoom: 16,
		controls: []
	});

	myPlacemark = new ymaps.Placemark([mLat, mLng], {
		hintContent: 'MacPlus'
	}, {
		iconLayout: 'default#image',
		iconImageHref: $('#map_marker').val(),
		iconImageSize: [75, 98],
		iconImageOffset: [-37, -98]
	});
	myMap.geoObjects.add(myPlacemark);
}

$(window).load(function () {
	$('.green, .black-area').each(function () {
		$(this).append('<div class="bg"></div>');
	});

	/* Toggle tooltip */
	$('.icons > li > a').click(function () {
		$(this).closest('li').toggleClass('active');
		return false;
	});

	/* Hide tooltip */
	$('body').click(function (event) {
		var target = $(event.target);
		if ($(target).closest('.tooltip').length === 0) {
			$('.header .icons li').removeClass('active');
		}
	});

	if (typeof ymaps != 'undefined' && $('#map').length) {
		ymaps.ready(initMap);
	}

	/* Popup */
	$('body').append('<div class="overlay"></div>');
	$('.overlay').click(function () {
		$('.popup, .overlay').fadeOut(200);
		return false;
	});
	$('.popup').each(function () {
		var _self = $(this);
		$('.js-close', this).click(function () {
			_self.fadeOut(200);
			$('.overlay').fadeOut(200);
			return false;
		});
	});
	$('.js-popup').click(function () {
		var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
		$('.overlay, .' + where).fadeIn(300);
		return false;
	});

	$('.popup').each(function () {
		var _self = $(this);
		$('.links', this).each(function () {
			$('a', this).click(function () {
				var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
				$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
				$('.' + where, _self).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
				return false;
			})
		});
		$('.form form', this).submit(function () {
			var valid = true;
			$(':input', this).not('.not_must').each(function () {
				if ($(this).val().trim().length === 0) {
					$(this).addClass('error');
					valid = false;
				} else {
					$(this).removeClass('error');
				}
			});
			if (valid) {
				$('.errortext', _self).hide();
			} else {
				$('.errortext', _self).show();
			}
			$(':input.error', this).eq(0).focus();
			if (valid) {
				switch (_self.attr('id')) {
					case 'contact_form':
						askQuestion(_self);
						break
					default:
						$('.' + _self.attr('id') + '-done').show();
						_self.hide();
				}
			}
			return false;
		});
	});

	resizeWindow();

	$('.repair-area').each(function () {
		$('.carousel', this).bxSlider({
			controls: false,
			responsive: true,
			minSlides: 1,
			adaptiveHeight: true
		});
	});

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);
});

$(window).resize(function () {
	resizeWindow();
});