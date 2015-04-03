/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Init forms */
	$('input:not(:radio):not(:checkbox), select').styler();

	/* Gallery */
	$('.fancybox-gallery', this).fancybox({
		autoSize: false,
		fitToView: false,
		padding: 0,
		cyclic: false,
		helpers: {
			media: {}
		}
	});

	/* Fancybox script */
	$('.fancybox, .fancybox-popup').fancybox({
		margin: 40,
		nextEffect: 'fade',
		prevEffect: 'fade',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.7)'
				}
			}
		}
	});

	$('.additional').each(function () {
		$('.carousel', this).bxSlider({
			pager: false,
			minSlides: 3,
			maxSlides: 3
		});
	});

	$('.slider').each(function () {
		$('.carousel', this).bxSlider({
			controls: false,
			adaptiveHeight: true
		});
	});

	$('.form-item').each(function () {
		var _self = $(this), _total = $('.t', _self), _triggers = $('.triggers', _self), _amount = $('.amount .n', _self);
		_triggers.each(function () {
			$('a', this).click(function () {
				var closest = $(this).closest('li'), where = $('.tab-' + $(this).attr("href").replace(/^.*#(.*)/, "$1")), current = $('.radio input:radio:checked', _self).eq(0), active, m = 0, l = 0;
				if (closest.is(':not(.active)')) {
					m = +_amount.val() * +current.attr('data-mass');
					l = +closest.attr('data-min');
					if ((m <= l)) {
						_amount.val(Math.ceil(l / +current.attr('data-mass'), 0));
					} else {
						_amount.val(Math.ceil(+closest.siblings('.active').attr('data-min') / +current.attr('data-mass'), 0) - 1);
					}
					closest.addClass('active').siblings('li.active').removeClass('active');
					where.removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
					where.find('.radio input:radio[data-item=' + current.attr('data-item') + ']').trigger('click').closest('.size').addClass('size-active').siblings('.size-active').removeClass('size-active');
				}
				return false;
			});
		});
		$(_self).on('change', '.radio input:radio', function () {
			_self.trigger('refresh');
		});
		_self.on('refresh', function () {
			$('.tab:visible').each(function () {
				var current = $('.radio input:radio:checked', _self).eq(0), amount = +$('.amount .n', _self).val(), price = +current.val(), mass = +current.attr('data-mass'), unit = +current.attr('data-unit'), currentMass = mass * amount;
				if (currentMass >= $('li.active', _triggers).attr('data-max')) {
					$('li:not(.active)', _triggers).filter(function () {
						return ((currentMass < $(this).attr("data-max") && (currentMass >= $(this).attr("data-min"))) || ($(this).attr("data-max") === 'max'));
					}).filter(':first').find('a').trigger('click');
				} else if (currentMass < $('li.active', _triggers).prev().attr('data-max')) {
					$('li.active', _triggers).prevAll().filter(function () {
						return ((currentMass < $(this).attr("data-max")) || ($(this).attr("data-max") === 'max'));
					}).filter(':last').find('a').trigger('click');
				}
				_total.text(price * amount);
			});
		});
		$('.size', _self).each(function () {
			var _size = $(this);
			$('.link', this).click(function () {
				_size.toggleClass('size-active');
				return false;
			});
		});
		$('.amount', _self).each(function () {
			var input = $('input', this), up = $('.up', this), down = $('.down', this);
			input.keydown(function (e) {
				if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 || (e.keyCode == 65 && e.ctrlKey === true) || (e.keyCode >= 35 && e.keyCode <= 39)) {
					return;
				}
				if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
					e.preventDefault();
				}
			});
			input.keyup(function () {
				_self.trigger('refresh');
			});
			up.click(function () {
				if (+input.val() < 9999) {
					input.val(+input.val() + 1);
					_self.trigger('refresh');
				}
			});
			down.click(function () {
				if (+input.val() > 1) {
					input.val(+input.val() - 1);
					_self.trigger('refresh');
				}
			});
		});
	});

	$('.block-type').each(function () {
		var _self = this;
		$('.colors', this).each(function () {
			$('a', this).click(function () {
				$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
				$(_self).find('.big').attr("src", $('img', this).attr('data-src'));
				return false;
			})
		});
		$('.amount', this).each(function () {
			var input = $('input', this), up = $('.up', this), down = $('.down', this);
			input.keydown(function (e) {
				if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
					(e.keyCode == 65 && e.ctrlKey === true) ||
					(e.keyCode >= 35 && e.keyCode <= 39)) {
					return;
				}
				if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
					e.preventDefault();
				}
			});
			up.click(function () {
				if (+input.val() < 99) {
					input.val(+input.val() + 1);
				}
			});
			down.click(function () {
				if (+input.val() > 0) {
					input.val(+input.val() - 1);
				}
			});
		});
		$('.close', this).click(function () {
			$(this).closest('tr').fadeToggle(300);
		})
	});

	$('.link-more', this).click(function () {
		$(this).fadeToggle(200).siblings('.in').slideDown(200);
		return false;
	});

	/* Tabs */
	$('.tabs-content').each(function () {
		var _self = this;
		$('a', this).click(function () {
			var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$(_self).siblings('.tab-content-' + where).removeClass('tab-content-hidden').siblings('.tab-content').addClass('tab-content-hidden');
			return false;
		});
	});
});