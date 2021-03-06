/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();

	/* Index carousel */
	$('.index').each(function () {
		$('.carousel', this).bxSlider({
			infiniteLoop: false,
			responsive: false,
			controls: false,
			pagerCustom: '.pager',
			mode: 'vertical',
			pause: 10000
		});
	});

	/* Staff carousel */
	$('.block-staff').each(function () {
		$('.carousel', this).bxSlider({
			infiniteLoop: false,
			responsive: false,
			pager: false,
			slideWidth: 388,
			minSlides: 2,
			maxSlides: 2,
			moveSlides: 1
		});
	});

	/* Gallery carousel */
	$('.gallery').each(function () {
		$('.carousel', this).bxSlider({
			infiniteLoop: false,
			responsive: false,
			pager: false,
			slideWidth: 208,
			minSlides: 4,
			maxSlides: 4,
			moveSlides: 1
		});
	});

	/* Scroll top */
	$('.up').click(function () {
		$('html, body').animate({scrollTop: 0}, 600, 'swing');
		return false;
	});

	/* Consult form submit */
	$(".service form").bind("submit", function () {
		$.ajax({
			type: "POST",
			cache: false,
			url: $(this).prop('action'),
			data: $(this).serializeArray(),
			success: function (data) {
				$.fancybox(data, {
					padding: 0,
					wrapCSS: 'fancybox-red',
					helpers: {
						overlay: {
							speedIn: 250,
							css: {
								'background': 'rgba(255, 255, 255, 0.84)'
							}
						}
					}
				});
			}
		});
		return false;
	});

	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.84)'
				}
			}
		}
	});
});