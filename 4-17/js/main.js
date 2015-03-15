/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Init forms */
	$('input, select').styler();
	
	/* Gallery */
	$('.gallery').each(function () {
		$('.fancybox-gallery', this).fancybox({
			autoSize: false,
			fitToView: false,
			padding: 0,
			helpers: {
				media: {}
			}
		});
	});

	/* Fancybox script */
	$('.fancybox, .fancybox-popup').fancybox({
		margin: 40,
		nextEffect: 'fade',
		prevEffect: 'fade',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.7)'
				}
			}
		}
	});

	$('.block-item .triggers').each(function () {
		$('li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	$('.block-item .tab').each(function () {
		$('.link', this).click(function () {
			$(this).siblings('.in').fadeToggle(400).closest('.size').toggleClass('size-active');
			return false;
		});
	});

	$('.additional').each(function () {
		$('.carousel', this).bxSlider({
			pager: false,
			minSlides: 3,
			maxSlides: 3
		});
	});

	$('.slider').each(function() {
		$('.carousel', this).bxSlider ({
			controls: false,
			adaptiveHeight: true
		});
	});

	$('.table-order').each(function () {
		$('.number').each(function() {
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
				if (+input.val() < 99) {
					input.val(+input.val() + 1);
				}
			});
			down.click(function () {
				if (+input.val() > 0) {
					input.val(+input.val() - 1);
				}
			});
		});
		$('.close', this).click(function() {
			$(this).closest('tr').fadeToggle(300);
		})
			
	});

});