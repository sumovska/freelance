/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Init forms */
	$('input, select').styler();

	/* Header */
	$('.header').each(function () {
		function handler() {
			var target = $(event.target);
			if ((target.closest('.search').length === 0)) {
				$('.search').removeClass('active');
			}
			if (target.closest('.cart').length === 0) {
				$('.cart').removeClass('active');
			}
		}

		$('.cell', this).each(function () {
			var _self = $(this);
			$('.link', this).click(function () {
				_self.siblings('.cell').removeClass('active');
				_self.toggleClass('active');
				if (_self.is('.active')) {
					$('body').bind("click", handler);
					$("input[type='text']", _self).focus();
				} else {
					$('body').unbind("click", handler);
				}
				return false;
			});
		});
		$('.menu > ul > li').hover(function () {
			$('.submenu', this).fadeIn(40);
		}, function () {
			$('.submenu', this).fadeOut(25);
		});
	});

	/* Index carousel */
	$('.index').each(function () {
		$('.carousel', this).bxSlider({
			infiniteLoop: false,
			responsive: true,
			controls: false,
			preloadImages: 'all',
			auto: true,
			autoHover: true,
			easing: 'ease'
		});
	});

	/* Item */
	$('.last-reviews').each(function () {
		$('.carousel', this).bxSlider({
			infiniteLoop: false,
			hideControlOnEnd: true,
			adaptiveHeight: true,
			responsive: true,
			pager: false,
			preloadImages: 'all',
			easing: 'ease'
		});
	});

	/* Sale */
	$('.sale').each(function () {
		$('.carousel', this).bxSlider({
			pager: false,
			easing: 'ease'
		});
	});

	/* Item */
	$('.catalog-item').each(function () {
		var gallery = $('.gallery', this);
		$('.carousel', this).bxSlider({
			controls: false,
			pagerCustom: gallery
		});
		$('a', gallery).click(function () {
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
		});
	});

	/* Filter */
	$('.filter').each(function () {
		$('.slider', this).each(function () {
			var _self = $(this);
			var item = $('.item', this).noUiSlider({
				start: [3000, 190000],
				step: 1000,
				behaviour: 'drag',
				connect: true,
				range: {
					'min': 3000,
					'max': 315000
				},
				serialization: {
					lower: [
						$.Link({
							target: $(".from var", _self)
						})
					],
					upper: [
						$.Link({
							target: $(".to var", _self)
						})
					],
					format: {
						// Set formatting
						thousand: ' ',
						decimals: 0
					}
				}
			});
		});
	});

	/* Tabs */
	$('.tabs').each(function () {
		$('.triggers li a', this).click(function () {
			var where = $(this).attr('href').replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Google Map */
	$('.about .map').each(function () {
		window.marker = null;
		function initMap() {
			var map, pos, style, mapOptions;
			pos = new google.maps.LatLng(55.752278, 37.6685159);
			style = [
				{
					"featureType": "road",
					"elementType": "labels.icon",
					"stylers": [
						{"saturation": 1},
						{"gamma": 1},
						{"visibility": "on"},
						{"hue": "#e6ff00"}
					]
				}
			];
			mapOptions = {
				center: pos,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				zoom: 16,
				backgroundColor: "#eeeeee",
				panControl: false,
				mapTypeControl: false,
				scaleControl: false,
				streetViewControl: false,
				overviewMapControl: false,
				scrollwheel: false,
				navigationControl: false,
				zoomControlOptions: {
					style: google.maps.ZoomControlStyle.SMALL
				}
			};
			map = new google.maps.Map(document.getElementById('map'), mapOptions);
			var mapType = new google.maps.StyledMapType(style, {name: "Grayscale"});
			map.mapTypes.set('grey', mapType);
			map.setMapTypeId('grey');
			var marker_image = 'img/pin.png';
			new google.maps.MarkerImage(marker_image, null, null, null, new google.maps.Size(90, 90));
			marker = new google.maps.Marker({
				position: pos,
				map: map
			});
		}

		/* Google Map */
		if (typeof google != 'undefined') {
			initMap();
		}
	});
});