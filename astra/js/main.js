/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Index page carousel */
	$('.slider .carousel').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		auto: true,
		speed: 700,
		slideWidth: 1260,
		minSlides: 1,
		moveSlides: 1
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
	$('.news .unit .text').each(function () {
		var _self = $(this);
		$('.link', this).click(function () {
			_self.toggleClass('text-open');
			$('.hidden', _self).slideToggle(400);
			return false;
		});
	});
});
