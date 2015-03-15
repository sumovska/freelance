/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Forms */
	$('input, select').styler();

	/* Tabs */
	$('.block-explore').each(function () {
		$('.triggers li a', this).click(function () {
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + $(this).attr("href").replace(/^.*#(.*)/, "$1")).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Anchors nav */
	$('.anchors .list').onePageNav({
		currentClass: 'active',
		scrollSpeed: 1000,
		easing: 'easeInOutQuad',
		xoffset: -20
	});

	/* Recommend carousel */
	$('.recommend').each(function () {
		$('.tooltip', this).append('<i class="arrow"></i>');
		$('.carousel', this).slick({
			infinite: true,
			swipeToSlide: true,
			centerMode: true,
			slidesToShow: 5,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed: 3000,
			prevArrow: '<span class="slick-prev"></span>',
			nextArrow: '<span class="slick-next"></span>'
		});
	});

	/* Popup script */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 80,
		fitToView: false,
		scrolling: 'no',
		helpers: {
			media: {},
			overlay: {
				speedIn: 300,
				speedOut: 300,
				css: {
					'background': 'rgba(0, 0, 0, 0.8)'
				}
			}
		}
	});

	/* Tooltips */
	$('.laps > li').hover(function () {
		$('.fn', this).stop().fadeIn(150);
	}, function () {
		$('.fn', this).stop().fadeOut(50);
	});

	/* Cards carousel */
	$('.research .cards').each(function () {
		$('a', this).click(function () {
			$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
			return false;
		});
	});

	/* Fade on scroll */
	$('.scrolled').viewportChecker({
		offset: 150
	});
});

$(window).on('scroll touchmove', function () {
	/* Переключение плавающего хедера */
	if ($(window).scrollTop() > 123) {
		$('html').addClass('header-fixed');
	} else {
		$('html').removeClass('header-fixed');
	}
});