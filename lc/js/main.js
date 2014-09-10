/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */


/* On document ready */
$(document).ready(function () {
	$('.carousel .catalog').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		pager: false,
		slideWidth: 219,
		minSlides: 4,
		maxSliders: 4,
		moveSlides: 1
	});
	$('.submenu a.open-list').click(function () {
		$(this).closest('li').toggleClass('active');
		return false;
	});
	$('.catalog .item .sale .new-price').prepend('<i class="before"></i>');
	$('').append('<i class="after"></i>');
	$('.community-group .member-link:nth-child(3n)').addClass('nth-child-3n');
});

