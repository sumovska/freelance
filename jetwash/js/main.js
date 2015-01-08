/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Init forms */
	$('input, select').styler();

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
		},
		afterClose: function () {
			$('#callback #form').show();
			$('#callback #success').hide();
		}
	});

	$('#callback .form').on('submit', function (e) {
		e.preventDefault();
		var form = $('#callback form');
		var data = form.serialize();
		$('#callback form button').text('Отправка...').attr('disabled', 'disabled');
		form.css('opacity', '.5');
	});

	$('#callback #close').on('click', function () {
		$.fancybox.close();
	});

	$(".gallery .list a").fancybox({
		autoSize: false,
		fitToView: false,
		padding: 0,
		helpers: {
			media: {}
		}
	});

});