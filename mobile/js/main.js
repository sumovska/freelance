/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();

	$('.index').each(function () {
		$('.carousel', this).slick({
			adaptiveHeight: false,
			dots: true,
			arrows: false,
			customPaging: function (slider, i) {
				return '<span data-role="none">' + (i + 1) + '</span>';
			}
		});
	});

	/* Slider carousel */
	$('.slider').each(function () {
		$('.slider-for').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			asNavFor: '.slider-nav'
		});
		$('.slider-nav').each(function () {
			$(this).slick({
				slidesToScroll: 1,
				centerPadding: '0',
				slidesToShow: 3,
				asNavFor: '.slider-for',
				arrows: false,
				centerMode: true,
				focusOnSelect: true
			});
			$('.slick-slide', this).removeClass('slick-active');
			$('.slick-slide', this).eq(0).addClass('slick-active');
		});
	});

	$('.price-slider').each(function () {
		$('.item', this).noUiSlider({
			start: [1200, 6000],
			step: 1,
			behaviour: 'drag',
			connect: true,
			range: {
				'min': 0,
				'max': 30000
			},
			format: wNumb({
				decimals: 0
			})
		});
		$('.item', this).Link('lower').to($('.from', this)).Link('upper').to($('.to', this));
	});

	function checkWidth() {
		var windowSize = $(window).width();

		if (windowSize > 768) {
			$('.catalog-small').removeClass('carousel-small');
		}
		else if (windowSize < 767) {
			$('.catalog-small').addClass('carousel-small').slick({
				slidesToScroll: 1,
				slidesToShow: 2,
				variableWidth: true,
				centerMode: true,
				focusOnSelect: true,
				arrows: false,
				responsive: [
					{
						breakpoint: 667,
						settings: {
							slidesToShow: 1,
							centerMode: true
						}
					}
				]
			});
			$('.offers').slick({
				slidesToScroll: 1,
				slidesToShow: 2,
				arrows: false,
				responsive: [
					{
						breakpoint: 667,
						settings: {
							slidesToShow: 1,
							centerMode: true
						}
					}
				]
			});
		}
	}

	// Execute on load
	checkWidth();
	// Bind event listener
	$(window).resize(checkWidth);

	/* Popup script */
	$('.fancybox-popup').fancybox({
		padding: 0
	});

	$('.filter').each(function(){
		$('.open').click(function() {
			$(this).closest('.toggle').addClass('toggle-active').siblings('form').fadeIn(200);
		});
		$('.close').click(function() {
			$(this).closest('.toggle').removeClass('toggle-active').siblings('form').fadeOut(200);
		});
		$('.h5 .switch').click(function() {
			$(this).closest('.h5').toggleClass('h5-active').siblings('.list', '.price-slider').fadeToggle(200);
		});
	});
});

