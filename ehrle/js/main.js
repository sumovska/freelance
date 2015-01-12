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
		},
		afterClose: function () {
			$('#callback #form').show();
			$('#callback #success').hide();
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
		_self.parent().prepend('<div class="corner corner-tl"></div><div class="corner corner-tr"></div><div class="corner corner-bl"></div><div class="corner corner-br"></div>');
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
			$end = $offset + 764;
		});
		$window.scroll(function () {
			if (($start <= $scroll) && ($scroll <= $end)) {
				$top = (($scroll - $offset) / (2.4 / $low));
				_bg.css({top: $top + 'px'});
			}
		});
	});

	$('.calculator .form').each(function () {
		var _self = $(this), a = 0, b = 0, c = 0, c1 = 0, c2 = 0;

		function reload() {
			a = $('input[name="a"]:checked').val();
			b = $('input[name="b"]:checked').val();
			c = $('input[name="c1"]:checked').val() * $('input[name="c2"]:checked').val();
			$('.p', _self).text(Math.floor(a * b * c));
			$('.s', _self).text(Math.floor(a * b / 100));
		}

		$('input:radio').change(function () {
			reload();
		});
		reload();
	});

	$('.video').each(function () {
		var _self = $(this);
		$window.resize(function () {
			$width = $window.width();
			if ($width > 1024) {
				if ($('video', _self).length < 1) {
					$(_self).append('<video preload autoplay loop muted><source src="./video/ehrle.mp4" type="video/mp4"><source src="./video/ehrle.ogv" type="video/ogg"><source src="./video/ehrle.webm" type="video/webm"></video>');
				}
			} else {
				if ($('video', _self).length > 0) {
					$('video', _self).remove();
				}
			}
		});
	});

	$window.resize();
	$window.scroll();
	$('body').addClass('body-loaded');

	$('#callback .form').on('submit', function (e) {
		e.preventDefault();
		var form = $('#callback form');
		var data = form.serialize();
		$('#callback form button').text('Отправка...').attr('disabled', 'disabled');
		form.css('opacity', '.5');

		$.post("handler.php", data).done(function (response) {
			if (response == 'ok') {
				yaCounter27583617.reachGoal('LEAD');
				form.trigger('reset');
				$('#callback #form').hide();
				$('#callback form button').text('Отправка').removeAttr('disabled');
				form.css('opacity', '1');
				$('#callback #success').show();
			}
		});

	});

	$(document).on('submit', '#product1f', function (e) {
		e.preventDefault();
		var form = $('#product1f');
		var data = form.serialize();
		$('#product1f button').text('Отправка...').attr('disabled', 'disabled');
		form.css('opacity', '.5');

		$.post("handler.php", data).done(function (response) {
			if (response == 'ok') {
				yaCounter27583617.reachGoal('LEAD');
				form.trigger('reset');
				$('#product1f').hide();
				$('#product1t').hide();

				$('#product1f button').text('Отправка').removeAttr('disabled');
				form.css('opacity', '1');
				$('#products-popup1 #success1').show();
			}
		});

	});
	$(document).on('submit', '#product2f', function (e) {
		e.preventDefault();
		var form = $('#product2f');
		var data = form.serialize();
		$('#product2f button').text('Отправка...').attr('disabled', 'disabled');
		form.css('opacity', '.5');

		$.post("handler.php", data).done(function (response) {
			if (response == 'ok') {
				yaCounter27583617.reachGoal('LEAD');
				form.trigger('reset');
				$('#product2f').hide();
				$('#product2t').hide();

				$('#product2f button').text('Отправка').removeAttr('disabled');
				form.css('opacity', '1');
				$('#products-popup2 #success2').show();
			}
		});
		$(document).on('submit', '#product3f', function (e) {
			e.preventDefault();
			var form = $('#product3f');
			var data = form.serialize();
			$('#product3f button').text('Отправка...').attr('disabled', 'disabled');
			form.css('opacity', '.5');

			$.post("handler.php", data).done(function (response) {
				if (response == 'ok') {
					yaCounter27583617.reachGoal('LEAD');
					form.trigger('reset');
					$('#product3f').hide();
					$('#product3t').hide();

					$('#product3f button').text('Отправка').removeAttr('disabled');
					form.css('opacity', '1');
					$('#products-popup3 #success3').show();
				}
			});

		});
		$(document).on('submit', '#product4f', function (e) {
			e.preventDefault();
			var form = $('#product4f');
			var data = form.serialize();
			$('#product4f button').text('Отправка...').attr('disabled', 'disabled');
			form.css('opacity', '.5');

			$.post("handler.php", data).done(function (response) {
				if (response == 'ok') {
					yaCounter27583617.reachGoal('LEAD');
					form.trigger('reset');
					$('#product4f').hide();
					$('#product4t').hide();

					$('#product4f button').text('Отправка').removeAttr('disabled');
					form.css('opacity', '1');
					$('#products-popup4 #success4').show();
				}
			});

			$('#callback #close').on('click', function () {
				$.fancybox.close();
			});
			$(document).on('click', '#closep1', function () {
				$.fancybox.close();
			});
			$(document).on('click', '#closep2', function () {
				$.fancybox.close();
			});
			$(document).on('click', '#closep3', function () {
				$.fancybox.close();
			});
			$(document).on('click', '#closep4', function () {
				$.fancybox.close();
			});

		});
	});
});