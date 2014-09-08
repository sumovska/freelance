/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */


/* On document ready */
$(document).ready(function () {
	/* Index page caousel */
	$('.image-carousel .image').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		speed: 700,
		auto: true,
		slideWidth: 1108,
		slideMargin: 22,
		minSlides: 1,
		moveSlides: 1,
		onSliderLoad: function () {
			if (window.PIE && $.browser.msie && ($.browser.versionNumber > 7)) {
				$('.image-carousel .bx-pager .bx-pager-link').each(function () {
					PIE.attach(this);
				});
			}
		}
	});

	/* Catalog caousel */
	$('.parts-carousel .parts').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		pager: false,
		slideWidth: 272,
		minSlides: 4,
		maxSliders: 4,
		moveSlides: 1
	});

	/* FAQ script */
	$('.faq .heading').click(function () {
		$(this).closest('.line').toggleClass('active');
		return false;
	});

	/* IE Fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			/* CSS3 for IE8 */
			$('.image-carousel .callback input[type="text"]').each(function () {
				$(this).val('mail@mail.com').css('color', '#aea9a9').focus(function () {
					if ($(this).val() === 'mail@mail.com') {
						$(this).val('').css('color', '#000');
					}
				}).blur(function () {
						if ($(this).val() === '') {
							$(this).val('mail@mail.com').css('color', '#aea9a9');
						}
					});
			});
			$('.image-carousel .callback textarea').css('color', '#aea9a9').each(function () {
				$(this).val('Мне нужно напечатать...').focus(function () {
					if ($(this).val() === 'Мне нужно напечатать...') {
						$(this).val('').css('color', '#000');
					}
				}).blur(function () {
						if ($(this).val() === '') {
							$(this).val('Мне нужно напечатать...').css('color', '#aea9a9');
						}
					});
			});
			$('.img-link, .block-catalog .item .name, .catalog-equipment .item .text,.header .contacts .mail, .header .contacts .address, .link-description .description, .header, .footer, .h-line, .faq .heading, .block-service .list li').prepend('<i class="before"></i>');
			$('.header, .footer, .block-catalog .item .name, .catalog-equipment .item .text').append('<i class="after"></i>');
			$('.block-catalog .item:nth-child(4n)').addClass('nth-child-4n');
			if (window.PIE) {
				$('.header .order, .header .nav li, .image-carousel .callback :input, .block-news .item .links .btn').each(function () {
					PIE.attach(this);
				});
			}
		}
	}
});


