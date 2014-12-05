/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	$('.next').click(function () {
		var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1");
		$.scrollTo(where, {
			duration: 700,
			easing: 'swing'
		});
		return false;
	});

	$('.h3-line').each(function () {
		$(this).wrapInner('<span class="line"></span>');
	});

	$('body').append('<div class="overlay"></div>');
	$('.overlay').click(function () {
		var _self = $(this);
		$('.popup').fadeOut(500, 'swing', function () {
			_self.fadeOut(500, 'swing');
			$('html').removeClass('body-popup');
		});
	});
	$('.popup-open').click(function () {
		var where = $('.popup-' + $(this).attr('href').replace(/^.*#(.*)/, "$1"));
		$('.overlay').fadeIn(500, 'swing', function () {
			where.css('margin-left', -Math.floor(where.outerWidth() / 2)).css('margin-top', -Math.floor(where.outerHeight() / 2));
			where.fadeIn(500, 'swing');
			$('html').addClass('body-popup');
		});
		return false;
	});
});