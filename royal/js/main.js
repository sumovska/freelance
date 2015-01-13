/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Init forms */
	$('input, select').styler();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Scroll top button */
	$('.scroll-top').append('<span></span>').click(function () {
		$('html, body').animate({scrollTop: 0}, 600, 'swing');
		return false;
	});

	/* Nav initialization */
	$('.nav').each(function () {
		var _self = $('nav');
		$(this).after('<a class="nav-toggle" href="#"></a>');
		$('.nav-toggle').click(function () {
			$('html').toggleClass('body-nav-open');
			return false;
		});
	});

	/* Searchbox initialization */
	$('.search').each(function () {
		function openSearch() {
			if (!$('html').hasClass('body-search-open')) {
				_self.velocity({'width': '100%', leaveTransforms: true}, 400, 'swing', function () {
					$('html').addClass('body-search-open');
				});
			}
			return false;
		}

		function closeSearch() {
			if ($('html').hasClass('body-search-open')) {
				$('html').removeClass('body-search-open');
				_self.velocity({'width': '40px', leaveTransforms: true}, 400, 'swing');
			}
			return false;
		}

		var _self = $(this);
		$(this).append('<a href="#" class="search-toggle"></a>');
		$('.search-toggle', _self).click(openSearch);
		$('input[type="text"]', _self).focus(openSearch);
		$('html').bind("click touchstart", function (e) {
			if ($(this).hasClass('body-search-open')) {
				if ((!$(e.target).is('.search')) && ($(e.target).closest('.search').length < 1)) {
					closeSearch();
				}
			}
		});
	});

	/* Index */
	$('.index').each(function () {
		var carousel = $('.carousel', this), index = $(this);
		carousel.bxSlider({
			infinteLoop: false,
			responsive: true,
			adaptiveHieght: true,
			swipeThreshold: 20,
			speed: 800,
			preloadImages: 'all',
			auto: true,
			autoControls: true,
			pause: 5000,
			onSliderLoad: function (currentIndex) {
				$('.bx-controls', index).wrap('<div class="bx-controls-space"></div>');
				carousel.find('.item:not(.bx-clone)').eq(1).clone().addClass('bx-clone').appendTo(carousel);
				carousel.width($('.item').length * 100 + '%');
				$('.bx-wrapper', index).append('<span class="forward"></span>');
				$('.forward', index).click(function () {
					carousel.goToNextSlide();
					carousel.stopAuto()
				});
			}
		});
	});

	/* Rewards */
	$('.rewards').each(function () {
		$('.scroll', this).mCustomScrollbar({
			axis: "x",
			scrollInertia: 100,
			scrollButtons: {enable: false},
			autoHideScrollbar: false,
			mouseWheel: {invert: true},
			theme: "rounded-dark",
			autoExpandScrollbar: true
		});
	});

	/* Footer */
	$('.footer').each(function () {
		$('.phone', this).clone().addClass('phone-mobile').appendTo('body');
	});
	scrollEvent();

	/* Block-item */
	$('.block-item .info').each(function () {
		$('.colors li a').click(function () {
			$(this).closest('li').toggleClass('active').siblings('.active').removeClass('active');
		});
	});
});

$(window).on('scroll touchmove', function () {
	return scrollEvent();
});
function scrollEvent() {
	/* Переключение плавающего хедера */
	if ($(window).scrollTop() > 60) {
		$('html').addClass('header-fixed');
	} else {
		$('html').removeClass('header-fixed');
	}
}