/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	var imageCarousel = $('.image-carousel .carousel');
	imageCarousel.bxSlider({
		controls: false,
		auto: true,
		pause: 5000,
		speed: 700,
		useCSS: false,
		onSliderLoad: function (currentIndex) {
			$(imageCarousel).closest('.bx-wrapper').append('<i class="mask-top"></i><i class="mask-left"></i><i class="mask-right"></i><i class="mask-bottom"></i>');
		}
	});
	$('.block-partners .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 115,
		minSlides: 6,
		maxSlides: 6,
		slideMargin: 5
	});
	$('.slider-photo .screen .carousel').bxSlider({
		auto: true,
		pager: false,
		pause: 5000,
		speed: 700,
		useCSS: false
	});
	$('.slider-photo .scroll .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 115,
		minSlides: 14,
		maxSlides: 14,
		slideMargin: 5
	});
})