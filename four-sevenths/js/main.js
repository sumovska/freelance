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
					'background': 'rgba(0, 0, 0, 0.9)'
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

});