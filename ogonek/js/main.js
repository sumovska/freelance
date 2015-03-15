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

	$('.index .carousel').slick({
		infinite: false,
		slidesToShow: 3,
		slidesToScroll: 1,
		slideWidth: '295px',
		centerPadding: '50px',
		adaptiveHeight: true,
		variableWidth: true,
		prevArrow: '<span class="slick-prev"></span>',
		nextArrow: '<span class="slick-next"></span>'
	});

	$('.slider').each(function() {
		$('.slider-for').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			asNavFor: '.slider-nav'
		});
		$('.slider-nav').slick({
			slidesToShow: 3,
			slidesToScroll: 1,
			slideWidth: '80px',
			centerPadding: '0',
			slidesToShow: 4,
			vertical: true,
			asNavFor: '.slider-for',
			arrows: false,
			centerMode: true,
			focusOnSelect: true
		});
	});

	/* Cart */
	$('.table-cart').each(function () {
		$('.number').each(function () {
			var input = $('input', this), up = $('.up', this), down = $('.down', this);
			input.keydown(function (e) {
				if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
					(e.keyCode == 65 && e.ctrlKey === true) ||
					(e.keyCode >= 35 && e.keyCode <= 39)) {
					return;
				}
				if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
					e.preventDefault();
				}
			});
			up.click(function () {
				if (+input.val() < 10) {
					input.val(+input.val() + 1);
				}
			});
			down.click(function () {
				if (+input.val() > 0) {
					input.val(+input.val() - 1);
				}
			});
		});
		$('.td-delete .delete', this).click(function() {
			$(this).closest('tr').fadeToggle(200);
			return false;
		});
	});
});