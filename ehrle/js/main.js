/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	scrollEvent();
});

$(window).on('scroll touchmove', function () {
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