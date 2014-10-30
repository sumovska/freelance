/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

$(window).load(function () {
	/* Tabs */
	$('.tabs').each(function () {
		var _self = this;
		$('a', this).click(function () {
			var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$('#' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	$('.navigation').each(function () {
		$('li', this).each(function () {
			$('.logo').append('<span class="span span-' + (+$(this).index() + 1) + '"></span>')
		});
		$('a', this).hover(function () {
			var a = $(this).closest('li').index() + 1;
			$('body').addClass('navigation-hover').addClass('navigation-hover-' + a);
		}, function () {
			var a = $(this).closest('li').index() + 1;
			$('body').removeClass('navigation-hover').removeClass('navigation-hover-' + a);
		});
	});

	$('.submenu').each(function () {
		var _self = $(this);
		$('.h3', this).click(function () {
			if ($(window).width() < 1024) {
				_self.toggleClass('submenu-open');
				$(this).siblings('.list').slideToggle(200);
			}
			return false;
		});
	});

	$('html').bind('mousedown touchstart', function (e) {
		var sbm = $('.submenu').eq(0);
		if (sbm.hasClass('submenu-open')) {
			if (($(e.target).closest('.submenu').length < 1) && !($(e.target).is('.submenu-open'))) {
				sbm.removeClass('submenu-open');
				$('.list', sbm).slideUp(200);
			}
		}
	});
});

