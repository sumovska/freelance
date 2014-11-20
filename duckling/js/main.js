/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Прелоад */
	$('.index').each(function () {
		var _self = $(this);
		$("<img />").attr("src", "img/index.jpg").one("load",function () {
			_self.addClass('index-loaded');
		}).each(function () {
				if (this.complete) {
					$(this).load()
				}
			});
	});

	/* Прокрутка */
	$('.anchor').click(function () {
		var where = '#' + $(this).attr('href').replace(/^.*#(.*)/, "$1");
		d = Math.floor(Math.abs((+$(window).scrollTop() - +$(where).offset().top) * .8));
		if (d < 500) {
			d = 500;
		}
		if (d > 2000) {
			d = 2000;
		}
		/*history.pushState(null, null, where);*/
		$.scrollTo(where, {
			duration: d,
			easing: 'swing'
		});
		return false;
	});

	/* Лайтбокс */
	$(".gallery .list .link").fancybox({
		padding: 0,
		prevEffect: 'fade',
		nextEffect: 'fade',
		closeBtn: false
	});

	/* Дропдаун */
	$('.header .profile').each(function () {
		var _self = $(this);
		$('.link', _self).click(function () {
			$('.sub', _self).fadeToggle(200, function () {
				_self.toggleClass('profile-open');
			});
			return false;
		});
	});
});