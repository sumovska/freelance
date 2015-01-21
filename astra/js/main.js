/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Index page carousel */
	$('.slider .carousel').bxSlider({
		useCSS: false,
		slideWidth: 1260
	});
	$('body').append('<div class="overlay"></div>');
	$('.overlay').click(function () {
		var _self = $(this);
		$('.popup').fadeOut(300, 'swing', function () {
			_self.fadeOut(300, 'swing');
		});
	});
	$('.js-popup').click(function () {
		var where = $('.' + $(this).attr('href').replace(/^.*#(.*)/, "$1"));
		$('.overlay').fadeIn(300, 'swing', function () {
			where.css('margin-left', -Math.floor(where.outerWidth() / 2));
			where.fadeIn(300, 'swing');
		});
		return false;
	});
	$('.news .unit .inform').each(function () {
		var _self = $(this);
		$('.link', this).click(function () {
			_self.toggleClass('inform-open');
			$('.hidden', _self).slideToggle(400);
			return false;
		});
	});

	$('.header').each(function () {
		$('.products .switch').click(function () {
			$(this).closest('li').toggleClass('active');
			return false;
		});
	});

});
