/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Tabs */
	$('.block-explore').each(function () {
		$('.triggers li a', this).click(function () {
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + $(this).attr("href").replace(/^.*#(.*)/, "$1")).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	$('.anchors .list').onePageNav({
		currentClass: 'active',
		scrollSpeed: 1000,
		easing: 'easeInOutQuad',
		xoffset: -20
	});

	/* Popup script */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 80,
		helpers: {
			media: {},
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.8)'
				}
			}
		}
	});

	/* Fade on scroll */
	$('.scrolled').viewportChecker({
		offset: 150
	});

	$('.laps > li').hover(function () {
		$('.fn', this).stop().fadeIn(150);
	}, function () {
		$('.fn', this).stop().fadeOut(50);
	});

	$('.research .cards').each(function () {
		$('a', this).click(function () {
			$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
			return false;
		});
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