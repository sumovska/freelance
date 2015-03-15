/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Index page gallery */
	$('.index').each(function () {
		$('li', this).addClass('loaded');
		$('a', this).focus(function () {
			$(this).parent().addClass('focus');
		}).blur(function () {
			$(this).parent().removeClass('focus');
		});
	});

	/* Toggling mobile feedback form */
	$('.block-feedback .form-toggle').click(function () {
		$('.block-feedback .form-feedback').slideToggle();
		return false;
	});

	/* Toggling mobile menu */
	$('.nav').each(function () {
		var _self = $(this);
		$('ul', this).wrap('<div class="nav-space"><div class="nav-in"></div></div>');
		$('.nav-in', this).append('<a class="nav-close" href="#"></a>');
		$('.nav-toggle', _self).click(function () {
			$('.nav-space', _self).fadeToggle(500);
			return false;
		});
		$('.nav-close', _self).click(function () {
			$('.nav-space', _self).fadeOut(500);
			return false;
		});
	});
});


/* On window scroll */
$(window).scroll(function () {
	/* Toggling fixed header */
	if ($(window).scrollTop() > 150) {
		$(".nav:not('.nav-fixed')").addClass('nav-fixed');
	} else {
		$('.nav.nav-fixed').removeClass('nav-fixed');
	}
});