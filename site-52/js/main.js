/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Phone toggle */
	$('.top .call').each(function() {
		var _self = this;
		$('.triggers a', this).click(function() {
			var where = $(this).attr('href').replace(/^.*#(.*)/, "$1");
			$('.' + where, _self).addClass('active').siblings().removeClass('active');
			$(this).closest('li').toggleClass('active').siblings('li').removeClass('active');
			return false;
		});
	});
	/* Index carousel */
	$('.index .carousel').bxSlider({
		auto: false,
		controls: false,
		pagerCustom: '.pager'
	});
	/* Block-features carousel */
	$('.block-features .carousel').bxSlider({
		auto: false,
		pager: false
	});
	/* Block-recent-projects carousel */
	$('.block-recent-projects .slider .carousel').bxSlider({
		auto: false,
		pager: false
	});
	/* Block-partners carousel */
	$('.block-partners .slider .carousel').bxSlider({
		infiniteLoop: true,
		auto: false,
		pager: false,
		controls: false,
		minSlides: 6
	});
	$('.block-services').each(function () {
		var _self = $(this);
		$('.show', this).click(function () {
			$(this).hide();
			$('.list', _self).css({'height': 'auto'});
			return false;
		});
	});
});

$(window).on('scroll touchmove', function () {
	return scrollEvent();
});

/* Обработчики скролла */
function scrollEvent() {
	var current = $(window).scrollTop(), body, h = 0;
	/* Переключение плавающего хедера */
	if (current > 62) {
		$('.header').addClass('header-fixed');
	} else {
		$('.header').removeClass('header-fixed');
	}
}
