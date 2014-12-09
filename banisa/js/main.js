/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
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
			where.css('margin-left', -Math.floor(where.outerWidth() / 2)).css('margin-top', -Math.floor(where.outerHeight() / 2));
			where.fadeIn(300, 'swing');
		});
		return false;
	});

	$('.header .toggle').click(function () {
		$('html').toggleClass('body-menu');
		return false;
	});

	$('.index').each(function () {
		$('.carousel', this).bxSlider({
			controls: false,
			pagerCustom: '.pager',
			responsive: true,
			minSlides: 1,
			adaptiveHeight: true
		});
		$('.item .about').each(function () {
			var _self = $(this);
			$('.more', this).click(function () {
				$(this).next('.toggle').fadeToggle(400);
				return false;
			});
		});
	});

	$('.slider-index').each(function () {
		$(this).fullpage({
			menu: '#nav',
			easing: 'swing',
			scrollOverflow: true,
			verticalCentered: true,
			resize: false
		});
		$('.bottom', this).click(function () {
			$.fn.fullpage.moveSectionDown();
			return false;
		});
	});

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	$(".fancybox-popup").fancybox({
		autoSize: true,
		fitToView: true,
		width: 'auto',
		height: 'auto',
		padding: 0,
		wrapCSS: 'fancybox-blue'
	});
});