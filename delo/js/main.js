/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* Tabs-nav */
$('.tabs-nav').each(function () {
	var _self = this;
	$('a', this).click(function () {
		var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
		$(this).closest('li').addClass('active').siblings('li').removeClass('active');
		$(_self).siblings('.' + where).removeClass('tab-hidden').siblings('.tab-nav').addClass('tab-hidden');
		return false;
	});
});

/* Tab-sample */
$('.legend_tabs').each(function () {
	var _self = this;
	$('a', this).click(function () {
		var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
		$(this).closest('li').addClass('current').siblings('li').removeClass('current');
		$(_self).siblings('.' + where).removeClass('tab-hidden').siblings('.tab-sample').addClass('tab-hidden');
		return false;
	});
});

/* Tabs_leg */
$('.legend_tabs').each(function () {
	var _self = this;
	$('a', this).click(function () {
		var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
		$(this).closest('li').addClass('current').siblings('li').removeClass('current');
		$(_self).siblings('.' + where).removeClass('tab-hidden').siblings('.tab-catalog').addClass('tab-hidden');
		return false;
	});
});

