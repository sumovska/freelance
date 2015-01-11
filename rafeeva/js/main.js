/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Retina images */
	$('.gallery .list img, .posts .list img').dense();

	/* Posts carousel */
	$('.posts-carousel').each(function () {
		window.slider = $('.list', this);
		window.slider.bxSlider({
			infinteLoop: false,
			responsive: true,
			swipeThreshold: 20,
			preloadImages: 'all',
			pager: false,
			controls: false,
			onSliderLoad: function () {
				var temp;
				$('li.bx-clone:last-of-type', window.slider).remove();
				temp = $('li:not(.bx-clone)', window.slider).clone().addClass('bx-clone');
				temp.appendTo(window.slider);
				window.slider.width($('li', window.slider).length * 100 + '%');
			}
		});
	});

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Navigation toggle */
	$('.toggle-navigation').click(function () {
		$('html').toggleClass('navigation-open').removeClass('contacts-open');
		return false;
	});

	/* Contacts toggle */
	$('.toggle-contacts').click(function () {
		$('html').toggleClass('contacts-open').removeClass('navigation-open');
		return false;
	});

});