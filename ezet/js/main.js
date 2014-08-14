/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

var newsBlock = $('.index .news');
var newsBlockCollapsed = false;

function resizeWindow() {
	if (!newsBlockCollapsed) {
		newsBlock.attr('data-height', newsBlock.removeAttr('style').height());
		if ($(window).width() < 1024) {
			newsBlock.closest('.index').addClass('index-collapsed');
			newsBlockCollapsed = true;
		}
	}
}

/* On document ready */
$(document).ready(function () {
	$('.featured .carousel').addClass('carousel-inited').find('.catalog').bxSlider({
		infiniteLoop: false,
		useCSS: false,
		pager: false,
		speed: 300,
		slideWidth: 220,
		slideMargin: 20,
		minSlides: 1,
		maxSlides: 4,
		moveSlides: 1
	});
});

$(window).load(function () {
	/* Navigation toggle */
	$('.navigation').each(function () {
		var _self = this;
		$('.toggle', this).click(function () {
			$(_self).toggleClass('navigation-toggle');
			return false;
		});
		/* Hide dropdown */
		$('body').click(function (event) {
			var target = $(event.target);
			if ($(target).closest('.navigation').length === 0) {
				$(_self).removeClass('navigation-toggle');
			}
		});
	});

	/* Searchbox toggle */
	$('.searchbox').each(function () {
		var _self = this;
		$('.triggers a', this).click(function () {
			var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$('input:text', _self).attr('disabled', true).filter('.' + where).removeAttr('disabled');
			return false;
		});
	});

	resizeWindow();
	/* Indexpage news toggle */
	$('.index').each(function () {
		var _self = this;
		$('.news', this).each(function () {
			var _news = this;
			$('.toggle', this).click(function () {
				$(_news).height($(_news).attr('data-height'));
				if ($(_self).hasClass('index-collapsed')) {
					$(_self).removeClass('index-collapsed');
					newsBlockCollapsed = false;
				} else {
					$(_news).height($(_news).attr('data-height'));
					$(_self).addClass('index-collapsed');
					newsBlockCollapsed = true;
				}
				return false;
			});
			$(_news).height($(_news).attr('data-height'));
		});
	});

	/* Forms */
	$('input, select').styler();

	/* Sidebar toggle */
	$('.sidebar-toggle').each(function () {
		$('a', this).click(function () {
			var where = $(this).prop('href').replace(/^.*#(.*)/, "$1"), li = $(this).closest('li');
			li.toggleClass('active').siblings('.active').removeClass('active');
			$('.submenu,.filter').removeClass('visible');
			if (li.hasClass('active')) {
				$('.' + where, '.sidebar').addClass('visible');
			} else {
				$('.' + where, '.sidebar').removeClass('visible');
			}
			return false;
		});
	});

	/* Filter */
	$('.filter').each(function () {
		$('.checkbox-list', this).perfectScrollbar();
		$('.slider', this).each(function () {
			var _self = $(this);
			var item = $('.item', this).noUiSlider({
				start: [ 5000, 80000 ],
				step: 100,
				behaviour: 'drag',
				connect: true,
				range: {
					'min': 0,
					'max': 100000
				},
				serialization: {
					lower: [
						$.Link({
							target: $(".from var", _self)
						})
					],
					upper: [
						$.Link({
							target: $(".to var", _self)
						})
					],
					format: {
						// Set formatting
						thousand: ' ',
						decimals: 0
					}
				}
			});
		});
	});

	/* Gallery */
	$('.gallery').each(function () {
		var _self = $(this);
		$('.list a', this).click(function () {
			$('.img', _self).attr('src', $(this).attr('href'));
			$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
			return false;
		});
	});

	/* Tabs */
	$('.tabs').each(function () {
		var _self = this;
		$('a', this).click(function () {
			var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$(_self).siblings('.' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Popups */
	$(".fancybox").fancybox({
		wrapCSS: 'fancybox-ezet',
		autoResize: false
	});

	/* IE Fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 10) {
			$('.header .search input:text').val('Поиск по сайту').focus(function () {
				if ($(this).val() === 'Поиск по сайту') {
					$(this).val('');
				}
			}).blur(function () {
					if ($(this).val() === '') {
						$(this).val('Поиск по сайту');
					}
				});
			$('.index .searchbox .searchbox-article').val('Поиск по артикулу').focus(function () {
				if ($(this).val() === 'Поиск по артикулу') {
					$(this).val('');
				}
			}).blur(function () {
					if ($(this).val() === '') {
						$(this).val('Поиск по артикулу');
					}
				});
			$('.index .searchbox .searchbox-name').val('Поиск по наименованию').focus(function () {
				if ($(this).val() === 'Поиск по наименованию') {
					$(this).val('');
				}
			}).blur(function () {
					if ($(this).val() === '') {
						$(this).val('Поиск по наименованию');
					}
				});
		}
	}
});

$(window).resize(function () {
	resizeWindow();
});
