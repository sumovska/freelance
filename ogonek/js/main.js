/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Init forms */
	$('input, select').styler();

	$('.top').each(function() {
		$('.search').each(function() {
			$('.toggle', this).click(function() {
				$(this).addClass('toggle-active').siblings('.form-in').slideDown(200);
				return false;
			});
			$('.close', this).click(function() {
				$(this).closest('.form-in').slideUp(200).siblings('.toggle-active').removeClass('toggle-active');
				return false;
			});
		})
		$('.callback').each(function() {
			$('.link', this).click(function() {
				$(this).addClass('link-active').siblings('.form-in').slideDown(200);
				return false;
			});
			$('.close', this).click(function() {
				$(this).closest('.form-in').slideUp(200).siblings('.link-active').removeClass('link-active');
				return false;
			});
		})
	});

});