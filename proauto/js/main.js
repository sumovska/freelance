/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	$('.nav').each(function () {
		$('a', this).click(function () {
			var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1");
			d = Math.floor(Math.abs((+$(window).scrollTop() - +$(where).offset().top) * .5));
			if (d < 500) {
				d = 500;
			}
			if (d > 2000) {
				d = 2000;
			}
			/*history.pushState(null, null, where);*/
			$.scrollTo(where, {
				duration: d,
				easing: 'swing',
				offset: {top: -41}
			});
			return false;
		});
	});

	$('.scroll-top').click(function () {
		d = Math.floor(Math.abs(+$(window).scrollTop() * .5));
		if (d < 500) {
			d = 500;
		}
		if (d > 2000) {
			d = 2000;
		}
		$.scrollTo(0, {
			duration: d,
			easing: 'swing'
		});
		return false;
	});

	$('.jumbotron').each(function () {
		var _self = $(this);
		$("<img />").attr("src", "img/jumbo.jpg").one("load",function () {
			_self.addClass('jumbotron-loaded');
		}).each(function () {
				if (this.complete) {
					$(this).load()
				}
			});
	});

	$('.works').each(function () {
		window.works = $(this);
		$(this).addClass('carousel-inited');
		window.carousel = $('.carousel', this);
		carousel.bxSlider({
			responsive: true,
			infiniteLoop: true,
			useCSS: false,
			preloadImages: 'all',
			slideMargin: 20,
			onSliderLoad: function (currentIndex) {
				changeIndex(currentIndex, true);
			},
			onSlideBefore: function ($slideElement, oldIndex, newIndex) {
				changeIndex(newIndex);
			}
		});
	});

	$('.map').each(function () {
		ymaps.ready(init);
		var myMap, myPlacemark;

		function init() {
			myMap = new ymaps.Map("map", {
				center: [55.706792, 37.615821],
				zoom: 15,
				controls: []
			});
			myPlacemark = new ymaps.Placemark([55.706792, 37.621821]);
			myMap.geoObjects.add(myPlacemark);
		}
	});
	$(window).scroll();
});

$(window).on('scroll touchmove', function () {
	/* Переключение плавающего хедера */
	if ($(window).scrollTop() > 6) {
		$('body').addClass('fixed');
	} else {
		$('body').removeClass('fixed');
	}
});

function changeIndex(currentIndex, load) {
	var current = carousel.find('li:not(.bx-clone)').eq(currentIndex), prev = works.find('.bx-prev'), next = works.find('.bx-next');
	$('.pic', prev).fadeOut(300, function () {
		var _self = $(this);
		current.prev('li').find('.pic').clone().hide().appendTo(prev).fadeIn(300, function () {
			_self.remove();
		});
	});
	$('.pic', next).fadeOut(250, function () {
		var _self = $(this);
		current.next('li').find('.pic').clone().hide().appendTo(next).fadeIn(250, function () {
			_self.remove();
		});
	});
	if (load) {
		current.prev('li').find('.pic').clone().appendTo(prev);
		current.next('li').find('.pic').clone().appendTo(next);
	}
}