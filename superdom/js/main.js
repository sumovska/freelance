/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

$.wait = function (callback, seconds) {
	return window.setTimeout(callback, seconds * 1000);
}

$(document).ready(function () {

	/* Carousel */
	$('.gallery .carousel').bxSlider({
		mode: 'fade',
		speed: 1500,
		infiniteLoop: true,
		easing: 'ease',
		adaptiveHeight: true,
		useCSS: false,
		preloadImages: 'all',
		pager: false,
		controls: false,
		auto: true
	});

	/* Form Range Slider */
	function updateSlider() {
		var arr = [], all = $(this).closest('.form-slider-space').find('input.form-range');
		arr = $(this).val().split(',');
		all.eq(0).val(arr[0]);
		all.eq(1).val(arr[1]);
	}

	$('.form-slider').slider({
		tooltip: 'hide'
	}).each(function () {
			$(this).on('slide', updateSlider).on('slideEnabled', updateSlider).slider('enable');
		});


	/* Form Custom Selectbox */
	$('.form-select').selectpicker();
	if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
		$('.form-select').selectpicker('mobile');
	}


	/* Form Datepicker */
	var today = new Date(), dd = today.getDate(), mm = today.getMonth() + 1, yyyy = today.getFullYear();
	if (dd < 10) {
		dd = '0' + dd;
	}
	if (mm < 10) {
		mm = '0' + mm;
	}
	today = dd + '.' + mm + '.' + yyyy;
	$('.form-datepicker, .input-daterange').datepicker({
		format: "dd.mm.yyyy",
		language: "ru",
		autoclose: true,
		startDate: today,
		todayHighlight: true
	});


	/* IE Fixes */
	if ($.browser.msie) {
		if ($.browser.versionNumber < 9) {
			/* Fix :after elements */
			$('.gallery, .filter > .container > .row').append('<i class="after"></i>');

			/* CSS3 for IE8 */
			if (window.PIE) {
				$('.recentWidget .btn, .appeal, .slider-handle, .appeal .photo img').each(function () {
					PIE.attach(this);
				});
			}
		}
		if ($.browser.versionNumber < 10) {
			/* Fix iframe bugs in IE */
			$('.video iframe').each(function () {
				$(this).attr("frameborder", "0").attr("src", $(this).attr("src") + "?wmode=transparent").clone().appendTo($(this).parent());
				$(this).remove();
			});
		}
	}

});


$(window).load(function () {

	/* Browser-specific classes for CSS */
	if ('WebkitAppearance' in document.documentElement.style) {
		$('body').addClass('browser-webkit');
	}
	if (window.navigator.msPointerEnabled) {
		$('body').addClass('browser-ie10');
	}

	/* Fix dropdown in navbar */
	$('.navbar-nav > li').each(function () {
		var _self = $(this);
		$('.dropdown-menu', this).each(function () {
			_self.addClass('dropdown');
			$(this).width($(_self).outerWidth() - 1);
			if (_self.is(':last-child')) {
				$(this).width($(_self).outerWidth() - 2);
			}
		});
	});

});