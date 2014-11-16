/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Index page caousel */
	$('.slider .carousel').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		auto: true,
		speed: 700,
		pager: false,
		slideWidth: 1280,
		slideMargin: 10,
		minSlides: 1,
		moveSlides: 1
	});
	$('.features .note .carousel').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		controls: false,
		slideWidth: 580,
		minSlides: 1,
		moveSlides: 1
	});
	$('.sidebar .list-top .carousel').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		controls: false,
		slideWidth: 220,
		minSlides: 1,
		moveSlides: 1
	});
});

$(window).load(function () {
	/* Filter */
	$('.sidebar').each(function () {
		$('.news', this).perfectScrollbar();
	
		});
	});

