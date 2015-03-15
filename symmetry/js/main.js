/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Toggling mobile menu */
	$('.nav').each(function () {
		var _self = $(this);
		$('ul', this).wrap('<div class="nav-space"><div class="nav-in"></div></div>');
		$('.header').append('<a class="toggle" href="#"></a>');
		$('.nav-space', _self).append('<a class="close" href="#"></a>');
		//$('.nav-in', this).append('<a class="nav-close" href="#"></a>');
		$('.toggle').click(function () {
			_self.show();
			$('.nav-space', _self).fadeToggle(200);
			return false;
		});
		$('.close', _self).click(function () {
			$('.nav-space', _self).fadeOut(200);
			return false;
		});
	});

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Init forms */
	$('input, select').styler();

	/* Video popup script */
	$(".fancybox-video").fancybox({
		height: 450,
		padding: 0,
		margin: 30,
		openEffect: 'fade',
		openSpeed: 500,
		closeEffect: 'fade',
		closeSpeed: 250,
		easing: 'swing',
		wrapCSS: 'fancybox-video',
		helpers: {
			media: {},
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.8)'
				}
			}
		},
		beforeShow: function () {
			document.getElementById('video').pause();
		},
		afterShow: function () {
			document.getElementById('video').play();
		}
	});

	$(".fancybox-work").fancybox({
		width: 960,
		maxWidth: 960,
		height: 'auto',
		padding: 0,
		margin: 70,
		openEffect: 'fade',
		openSpeed: 500,
		closeEffect: 'fade',
		closeSpeed: 250,
		easing: 'swing',
		wrapCSS: 'fancybox-work',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.8)'
				}
			}
		}
	});

	if ($('#video').is(':visible')) {
		document.addEventListener('touchstart', function (event) {
			document.getElementById('video').play();
		}, false);
	}

	$('.form-contact').submit(function () {
		var _self = $(this), error = false;

		function send() {
			$.ajax({
				url: _self.attr('action'),
				type: "POST",
				data: {
					name: $('input[name="name"]', _self).val(),
					company: $('input[name="company"]', _self).val(),
					email: $('input[name="email"]', _self).val(),
					phone: $('input[name="phone"]', _self).val(),
					message: $('textarea[name="message"]', _self).val()
				},
				success: function () {
					$('.success', _self).remove();
					$('.submits', _self).append('<p class="success">Your message was sent successfully</p>');
				}
			});
		}

		$(':input.required', this).each(function () {
			if ($.trim($(this).val()).length === 0) {
				$(this).addClass('error');
				error = true;
			} else {
				$(this).removeClass('error');
			}
		});
		if (error) {
			$('.error', this).eq(0).focus();
		} else {
			send();
		}

		return false;
	});
});

$(window).load(function () {
	$('.works').each(function () {
		function resizeToCover() {
			$('li', _self).each(function () {
				var sx = Math.floor(_self.width() / 3), sy = Math.floor(_self.height() / 4), lx = _self.width() - sx * 2, ly = _self.height() - sy * 3;
				$(this).width(sx);
				$(this).height(sy);
				if ($(this).index() === 0) {
					$(this).css({'top': 0, 'left': 0});
				}
				if ($(this).index() === 1) {
					$(this).height(sy * 2).css({'top': 0, 'left': sx});
				}
				if ($(this).index() === 2) {
					$(this).width(lx).css({'top': 0, 'right': 'auto', 'left': sx * 2});
				}
				if ($(this).index() === 3) {
					$(this).width(Math.floor(lx / 2)).css({'top': sy, 'left': sx * 2});
				}
				if ($(this).index() === 4) {
					$(this).width(lx - Math.floor(lx / 2)).css({'top': sy, 'left': 'auto', 'right': 0});
				}
				if ($(this).index() === 5) {
					$(this).width(lx).height(sy * 2).css({'top': sy, 'left': 0});
				}
				if ($(this).index() === 6) {
					$(this).width(lx).height(ly).css({'top': 'auto', 'bottom': 0, 'left': 0});
				}
				if ($(this).index() === 7) {
					$(this).width(sx + lx).height(2 * ly).css({'top': 'auto', 'bottom': 0, 'left': sx, 'right': 'auto'});
				}
				$('.preview', this).each(function () {
					var min_w = 100;
					var vid_w_orig = 768;
					var vid_h_orig = 432;
					var scale_h = $(this).width() / vid_w_orig;
					var scale_v = $(this).height() / vid_h_orig;
					var scale = scale_h > scale_v ? scale_h : scale_v;
					if (scale * vid_w_orig < min_w) {
						scale = min_w / vid_w_orig;
					}
					$('video', this).width((scale * vid_w_orig) + 2);
					$('video', this).height((scale * vid_h_orig) + 2);
				});
			});
		}

		var _self = $(this);

		$(window).resize(function () {
			resizeToCover();
		});

		$('li', this).each(function () {
			var _li = this;
			$('.preview', this).each(function () {
				$(this).append('<video preload loop muted></video>');
				$('video', this).each(function () {
					var i = $(_li).index() + 1;
					$(this).attr('poster', './video/work/' + i + '.jpg');
					if (!$.browser.mozilla && $.browser.name != 'mozilla') {
						$(this).append('<source src="./video/work/' + i + '.mp4" type="video/mp4">');
					}
					$(this).append('<source src="./video/work/' + i + '.webm" type="video/webm">')
						.append('<source src="./video/work/' + i + '.ogv" type="video/ogg">');
					$(this)[0].load();
				});
			});
			$(this).hover(function () {
				$('.preview video', this)[0].play();
			}, function () {
				$('.preview video', this)[0].pause();
			});
		});
		$(this).addClass('loaded');
		resizeToCover();
	});
});