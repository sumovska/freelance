/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

var newsBlock = $('.index .news');
var newsBlockCollapsed = false;

function resizeWindow() {
	console.log(newsBlockCollapsed);
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
	$('.special .carousel').addClass('carousel-inited').find('.catalog').bxSlider({
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

	/* IE Fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 10) {
			$('.header .search input:text').val('Поиск по сайту').focus(function () {if ($(this).val() === 'Поиск по сайту') {$(this).val('');}}).blur(function () {if ($(this).val() === '') {$(this).val('Поиск по сайту');}});
			$('.index .searchbox .searchbox-article').val('Поиск по артикулу').focus(function () {if ($(this).val() === 'Поиск по артикулу') {$(this).val('');}}).blur(function () {if ($(this).val() === '') {$(this).val('Поиск по артикулу');}});
			$('.index .searchbox .searchbox-name').val('Поиск по наименованию').focus(function () {if ($(this).val() === 'Поиск по наименованию') {$(this).val('');}}).blur(function () {if ($(this).val() === '') {$(this).val('Поиск по наименованию');}});
		}
	}
});

$(window).resize(function () {
	resizeWindow();
});
