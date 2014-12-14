/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	scrollEvent();
});

$(window).on('scroll touchmove', function () {
	/* Init forms */
	$('input, select').styler();

	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 200,
				speedOut: 200,
				css: {
					'background': 'rgba(255, 255, 255, 0.75)'
				}
			}
		}
	});

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/*
	var url = './map.html';
	$.ajax({url: url, dataType: 'html', type: 'GET'}).done(function (resp) {
		$('#map-container').html(resp);
	});
	*/

	scrollEvent();
});

/* Обработчик скролла */
function scrollEvent() {
	/* Переключение плавающего хедера */
	if ($(window).scrollTop() >= 10) {
		$('.nav').addClass('nav-fixed');
	} else {
		$('.nav').removeClass('nav-fixed');
	}
}

