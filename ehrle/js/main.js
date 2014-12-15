/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Scrolling navigation */
	$('#nav').onePageNav({
		currentClass: 'active',
		scrollSpeed: 1000,
		easing: 'easeInOutQuad',
		xoffset: -60
	});

	/* Init forms */
	$('input, select').styler();

	/* Fixed header init */
	fixedHeader();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		easing: 'easeOutQuad',
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.8)'
				}
			}
		}
	});

	/*loadMap();*/
});

$(window).on('scroll touchmove', function () {
	fixedHeader();
});

/* Fixed header init */
function fixedHeader() {
	/* Переключение плавающего хедера */
	if ($(window).scrollTop() >= 10) {
		$('.nav').addClass('nav-fixed');
	} else {
		$('.nav').removeClass('nav-fixed');
	}
}

/* Google Map init */
function loadMap() {
	var url = './map.html';
	$.ajax({url: url, dataType: 'html', type: 'GET'}).done(function (resp) {
		$('#map-container').html(resp);
	});
}

