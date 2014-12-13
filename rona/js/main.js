/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE, mcImgSlider */


/* On document ready */
$(document).ready(function () {

	$('input, select').styler();

	var sliderOptions = {
		sliderId: "slider",
		startSlide: 0,
		effect: "series1",
		effectRandom: false,
		pauseTime: 2600,
		transitionTime: 500,
		slices: 12,
		boxes: 8,
		hoverPause: 1,
		autoAdvance: true,
		captionOpacity: 0.3,
		captionEffect: "fade",
		thumbnailsWrapperId: "thumbs",
		m: false,
		license: "b6t80"
	};
	//noinspection JSPotentiallyInvalidConstructorUsage
	var imageSlider = new mcImgSlider(sliderOptions);

	$('.header .wrapper').prepend('<a href="#" class="nav-toggle"></a>');
	$('.nav-toggle').click(function () {
		$(this).toggleClass('nav-toggle-active');
		$('.nav').fadeToggle(100);
	});

	$('.sidebar').prepend('<a href="#" class="submenu-toggle"></a>');
	$('.submenu-toggle').click(function () {
		$(this).toggleClass('submenu-toggle-active');
		$('.submenu').slideToggle(200);
	});

	$('body').bind('mousedown touchstart', function (e) {
		var stgl = $('.submenu-toggle'), ntgl = $('.nav-toggle');
		if (stgl.hasClass('submenu-toggle-active')) {
			if (($(e.target).closest('.submenu').length < 1) && !($(e.target).is('.submenu-toggle'))) {
				stgl.removeClass('submenu-toggle-active');
				$('.submenu').slideUp(200);
			}
		}
		if (ntgl.hasClass('nav-toggle-active')) {
			if (($(e.target).closest('.nav').length < 1) || ($(e.target).is('.nav'))) {
				ntgl.removeClass('nav-toggle-active');
				$('.nav').fadeOut(100);
			}
		}
	});


	$('.submenu-index').each(function () {
		$(this).children('li').hover(function () {
			imageSlider.displaySlide($(this).index());
			imageSlider.switchAuto();
		}, function () {
			imageSlider.switchAuto();
		});
	});

	$(".gallery a").fancybox({
		autoSize: false,
		fitToView: false,
		padding: 0,
		helpers: {
			media: {}
		}
	});

});
