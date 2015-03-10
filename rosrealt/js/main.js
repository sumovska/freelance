/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Fastclick */
	FastClick.attach(document.body);

	/* Формы */
	$('input:not(.file-photo), select').styler();
	$('input.file-photo').styler({
		filePlaceholder: 'Добавить<br>фото'
	});

	/* Навигация */
	$('.nav').each(function () {
		var body = $('body');
		$('.toggle', this).click(function () {
			if ($(window).width() < 1280) {
				body.toggleClass('nav-fixed');
			} else {
				body.toggleClass('nav-closed');
			}
			return false;
		});
	});

	/* Кнопка закрытия */
	$('.note .close').click(function () {
		$(this).closest('.note').fadeOut();
	});

	/* Фильтр */
	$('.filter').each(function () {
		$('.toggle').click(function () {
			$(this).siblings('.inside').fadeToggle();
			return false;
		});
	});
});