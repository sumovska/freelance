/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Scrolling navigation */
	$('#nav').onePageNav({
		currentClass: 'active',
		scrollSpeed: 1000,
		easing: 'easeInOutQuad',
		xoffset: -60
	});

	/* Init forms */
	$('input, select').styler();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		easing: 'easeOutQuad',
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.8)'
				}
			}
		}
	});

	/* Video popup script */
	$(".fancybox-video").fancybox({
		padding: 0,
		easing: 'easeOutQuad',
		autoSize: false,
		fitToView: false,
		helpers: {
			media: {},
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.8)'
				}
			}
		}
	});

	/* Google Map init */
	$('.map').each(function () {
		function loadMap(url) {
			$.ajax({url: url, dataType: 'html', type: 'GET'}).done(function (resp) {
				container.html(resp);
			});
		}

		var url = './map.html', container = $('#map-container');
		$('.tabs .list a').click(function () {
			var url = $(this).attr('href');
			$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
			container.html("<p class='loading'>Идет загрузка карты&hellip;</p>");
			setTimeout(function () {
				loadMap(url);
			}, 300);
			return false;
		});
		loadMap(url);
	});

	var $window = $(window), $start = 0, $scroll = $window.scrollTop(), $width = $window.width(), $height = $window.height(), $offset = 0, $low = 0, $top = 0, $switch;

	$window.on('scroll touchmove', function () {
		$scroll = $window.scrollTop();
		/* Переключение плавающего хедера */
		if ($scroll >= 10) {
			$('.nav').addClass('nav-fixed');
		} else {
			$('.nav').removeClass('nav-fixed');
		}
	});
	$('.winter .space').each(function () {
		var _self = $(this), _bg;
		_self.append('<div class="bg"></div>');
		_bg = $('.bg', _self);
		$window.resize(function () {
			$height = $window.height();
			if ($height > 800) {
				$low = 1 + ($height - 800) / 800;
			} else {
				$low = 1;
			}
			$offset = _self.offset().top;
			$start = $offset - $height;
			$end = $offset + 590;
		});
		$window.scroll(function () {
			if (($start <= $scroll) && ($scroll <= $end)) {
				$top = -(($scroll - $offset) / (1.7 / $low));
				_bg.css({top: $top + 'px'});
			}
		});
	});

	$('.video').each(function () {
		var _self = $(this);
		$window.resize(function () {
			$width = $window.width();
			if ($width > 1024) {
				console.log('b' + $('video', _self).length);
				if ($('video', _self).length < 1) {
					console.log('add');
					$(_self).append('<video preload autoplay loop muted><source src="./video/ehrle.mp4" type="video/mp4"><source src="./video/ehrle.ogv" type="video/ogg"><source src="./video/ehrle.webm" type="video/webm"></video>');
				}
			} else {
				console.log('a' + $('video', _self).length);
				if ($('video', _self).length > 0) {
					console.log('delete');
					$('video', _self).remove();
				}
			}
		});
	});

	$window.resize();
	$window.scroll();
	$('body').addClass('body-loaded');
});