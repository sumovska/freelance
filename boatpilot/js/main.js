/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Index page caousel */
	$('.index').each(function () {
		var _self = $(this), carousel = $('.carousel', this), carouselBlur;
		carousel.wrap('<div class="main"></div>');
		carouselBlur = carousel.clone();
		carousel = carousel.bxSlider({
			speed: 600,
			easing: 'ease',
			preloadImages: 'all',
			pager: false,
			swipeThreshold: 30,
			infiniteLoop: false,
			adaptiveHeight: true,
			hideControlOnEnd: true,
			onSliderLoad: function (index) {
				var src = '', wrapper = $(carousel[0]).closest('.bx-wrapper');
				$('<div></div>').addClass('pages').text(++index + ' / ' + carousel.getSlideCount()).prependTo($('.bx-controls-direction', wrapper));
				$('li', carousel[0]).each(function () {
					src = $('.img', this).prop('src');
					$('<div></div>').addClass('bg').css('background-image', "url('" + src + "')").prependTo(this);
				});
				carouselBlur = carouselBlur.appendTo(_self);
				carouselBlur = carouselBlur.wrap('<div class="additional"></div>');
				carouselBlur = carouselBlur.bxSlider({
					speed: 800,
					easing: 'ease',
					touchEnabled: false,
					pager: false,
					controls: false,
					captions: true,
					adaptiveHeight: true,
					infiniteLoop: false,
					onSliderLoad: function (index) {
						var src = '', wrapper = $(carouselBlur[0]).closest('.bx-wrapper');
						$('li', carouselBlur[0]).each(function () {
							src = $('.img', this).prop('src');
							$('<div></div>').addClass('blur').css('background-image', "url('" + src + "')").prependTo(this);
						});
						$('.img', carousel).eq(0).one("load", function () {
							_self.addClass('loaded');
							$('.preloader').remove();
						}).each(function () {
							if (this.complete) $(this).load();
						});
					}
				});
			},
			onSlideBefore: function ($slideElement, oldIndex, newIndex) {
				carouselBlur.goToSlide(newIndex);
				$(carousel[0]).closest('.bx-wrapper').find('.bx-controls-direction .pages').text(++newIndex + ' / ' + carousel.getSlideCount());
			}
		});
	});

	/* Features caousel */
	$('.features .note .carousel').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		controls: false,
		swipeThreshold: 30,
		minSlides: 1,
		moveSlides: 1
	});

	/* Top sailors caousel */
	$('.top-sailors .carousel').bxSlider({
		infiniteLoop: false,
		controls: false,
		swipeThreshold: 30,
		minSlides: 1,
		moveSlides: 1
	});

	/* Top checkins scrollbar */
	$('.top-checkins').each(function () {
		$('.list', this).perfectScrollbar();
	});

	/* Toggle search panel on mobile devices */
	$('.social .s a').click(function () {
		$('body').toggleClass('search-open');
		return false;
	});
	$('body').bind("click touchstart", function (e) {
		if ($(this).hasClass('search-open')) {
			if ((!$(e.target).is('.search')) && ($(e.target).closest('.search').length === 0)) {
				$('body').removeClass('search-open');
			}
		}
	});

	FastClick.attach(document.body);
});

