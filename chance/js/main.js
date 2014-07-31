/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	var imageCarousel = $('.image-carousel .carousel');
	imageCarousel.bxSlider({
		controls: false,
		auto: true,
		pause: 5000,
		speed: 700,
		useCSS: false,
		onSliderLoad: function (currentIndex) {
			$(imageCarousel).closest('.bx-wrapper').append('<i class="mask-top"></i><i class="mask-left"></i><i class="mask-right"></i><i class="mask-bottom"></i>');
		}
	});

	$('.block-partners .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 115,
		minSlides: 6,
		maxSlides: 6,
		slideMargin: 5
	});

	$('.gallery-photo .scroll .carousel').bxSlider({
		infiniteLoop: false,
		pager: false,
		slideWidth: 56,
		maxSlides: 14,
		slideMargin: 5
	});

	$('.swiper').each(function () {
		var swiper;
		if ($.browser.msie) {
			swiper = new Swiper('.swiper-container', {
				slidesPerView: 3,
				tdFlow: {
					rotate: 0,
					stretch: 110,
					depth: 200,
					modifier: 1,
					shadows: true
				}
			});
		} else {
			swiper = new Swiper('.swiper-container', {
				slidesPerView: 3,
				loop: true,
				tdFlow: {
					rotate: 0,
					stretch: 110,
					depth: 200,
					modifier: 1,
					shadows: true
				}
			});
		}
		$(this).siblings('.swiper-prev').click(function () {
			swiper.swipePrev();
		});
		$(this).siblings('.swiper-next').click(function () {
			swiper.swipeNext();
		});
	});

	/* IE Fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			/* Fix :after elements */
			$('.gallery, .filter > .container > .row').append('<i class="after"></i>');

			/* CSS3 for IE8 */
			if (window.PIE) {
				$('.partners, .link, .user-photo .pic, .header .city').each(function () {
					PIE.attach(this);
				});
			}
		}
	}
});