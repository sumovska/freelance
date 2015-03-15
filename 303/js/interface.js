/*jslint white: true, browser: true, onevar: false, undef: true, nomen: false, eqeqeq: true, plusplus: true, bitwise: true, regexp: false, newcap: true */
/*global window, console, document, $, jQuery, PIE */

function Site() {
	var self = this;

	this.init = function () {
		initCarousel();
		initGallery();
		initIE();
	};

	function initCarousel() {
		$('.catalog-carousel').bxSlider({
			mode: 'horizontal',
			slideWidth: 194,
			minSlides: 1,
			maxSlides: 5,
			moveSlides: 1,
			pager: false,
			infiniteLoop: false,
			responsive: false,
			hideControlOnEnd: true
		});
	}

	function initGallery() {
		$('.gallery').each(function () {
			var img = $(this).closest('.item').children('.img');
			$('a', this).click(function () {
				$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
				if ($(this).is('.video')) {
					window.open(this.href);
				} else {
					img.attr('src', $(this).attr('href'));
				}
				return false;
			});
		});
	}

	function initIE() {
		if ($.browser.msie && $.browser.version < 9) {
			$('.footer').append('<i class="before"></i>');
			if ($.browser.version < 8) {
				$('.wrap').append('<i class="after"></i>');
				$('.header .phone, .header .city a, .header .cart, .header .links, .block-index .deals li, .block-item .catalog li, .ul li').append('<i class="before"></i>');
			}
			if (window.PIE) {
				$('.block, .footer, .footer .before, .block-index .video, .block-description .tech li, .block-description .info .img, .block-item .icons li, .price-line .buy, .block-item .gallery li, .block-item .gallery li img').each(function () {
					PIE.attach(this);
				});
			}
		}
	}
}

$(document).ready(function () {
	window.site = new Site();
	window.site.init();
});