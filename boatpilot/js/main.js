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


	$('.map-main .info .scroll').perfectScrollbar({
		suppressScrollX: true
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

	$('.social .nt a').click(function () {
		$('.header .navigation').slideToggle(100);
		return false;
	});

	$('.link-scroll').click(function () {
		var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1");
		$.scrollTo(where, {
			duration: 2000,
			easing: 'swing'
		});
		return false;
	});

	FastClick.attach(document.body);

	/* Submenu */
	$('.submenu').each(function () {
		var _self = $(this);
		window.submenu = {};
		submenu.self = $(this);
		submenu.sidebar = $('.sidebar');
		submenu.floating = false;
		submenu.anchor = false;
		submenu.anchors = [];
		submenu.active = 1;
		$(this).append('<a class="toggle" href="#"></a>');
		$('.toggle', this).click(function () {
			submenu.self.addClass('submenu-open')
			$('body').addClass('body-submenu-open')
			return false;
		});
		$(this).children('li').children('ul').each(function () {
			$(this).parent('li').addClass('sub');
		});
		$(this).find('a').click(function () {
			submenu.active = 0;
			$(this).parents('li').each(function () {
				submenu.active = submenu.active + $(this).index() + 1
			});
		});
		$(this).find('.sub').children('a').click(function () {
			$(this).siblings('ul').slideToggle(function () {
				$(this).closest('li.sub').toggleClass('open');
			});
			return false;
		});
		if (_self.hasClass('submenu-floating')) {
			submenu.floating = true;
			$(this).find('a').click(function () {
				submenuRefresh();
			});
		}
		if (_self.hasClass('submenu-anchor')) {
			submenu.anchor = true;
			$(this).find('a').click(function () {
				var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1"), d = 500, off = 0;
				d = Math.floor(Math.abs((+$(window).scrollTop() - +$(where).offset().top) * .6));
				if (d < 400) {
					d = 300;
				}
				if (d > 2000) {
					d = 2000;
				}
				if (+$(where).css('padding-top').split('px')[0] < 10) {
					off = -20;
				}
				$.scrollTo(where, {
					duration: d,
					easing: 'swing',
					offset: {top: off}
				});
				return false;
			});
		}
	});
	submenuRefresh();
});

/* Refresh floating submenu */
function submenuRefresh() {
	submenuResize();
	submenuScroll();
}

/* Refresh floating submenu on resize */
function submenuResize() {
	if (typeof window.submenu != 'undefined') {
		if (submenu.floating === true) {
			if ($(window).width() > 1024) {
				submenu.self.width($('.sidebar').outerWidth());
			} else {
				submenu.self.removeProp('style');
			}
			submenu.triggerTop = +submenu.sidebar.offset().top;
			submenu.offsetBottom = +$('.footer').outerHeight() + 23;
			submenu.triggerBottom = +$('body').outerHeight() - submenu.offsetBottom - +submenu.self.outerHeight(true);
		}
		if (submenu.anchor === true) {
			submenu.anchors = [];
			$('a:not(.toggle)', submenu.self).each(function () {
				var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1"), pos = 0;
				pos = Math.floor($(where).offset().top);
				if (+$(where).css('padding-top').split('px')[0] < 10) {
					pos = pos - 25;
				}
				submenu.anchors.push(pos);
			});
		}
	}
}

/* Refresh floating submenu on scroll */
function submenuScroll() {
	if (typeof window.submenu != 'undefined') {
		var y = $(window).scrollTop();
		if (submenu.floating === true) {
			if (y >= submenu.triggerTop) {
				submenu.self.addClass('submenu-fixed');
			} else {
				submenu.self.removeClass('submenu-fixed');
			}
			if (y >= submenu.triggerBottom) {
				submenu.self.addClass('submenu-fixed-bottom').css('bottom', submenu.offsetBottom);
			} else {
				submenu.self.removeClass('submenu-fixed-bottom').css('bottom', 'auto');
			}
		}
		if (submenu.anchor === true) {
			var i = 0;
			do {
				i = i + 1;
			} while ((i < submenu.anchors.length) && (submenu.anchors[i] <= y));
			if (submenu.active != i) {
				$('li.active', submenu.self).removeClass('active');
				$('li', submenu.self).eq(i - 1).addClass('active').parents('li').addClass('active');
				submenu.active = i;
			}
		}
	}
}

/* Page resize */
$(window).resize(function () {
	submenuResize();
});

/* Page scroll */
$(window).scroll(function () {
	submenuScroll();
});