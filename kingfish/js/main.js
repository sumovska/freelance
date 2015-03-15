/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	/* Cart refresh */
	function refreshCart() {
		$('.form-cart').each(function () {
			var t = 0;
			$('.line:not(.deleted)', this).each(function () {
				var c = $('.c', this), p = $('.p', this), n = $('.n', this), tt = +c.text() * +n.val();
				p.text(tt);
				t = t + tt;
				if (+n.val() === 0) {
					$(this).addClass('deleted');
				}
			});
			$('.t', this).text(t);
		});
	}

	/* Init forms */
	$('input, select').styler();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Header init */
	$('.header').each(function () {
		var _self = $(this);
		$('.toggle', _self).click(function () {
			$('html').toggleClass('html-nav-visible');
			return false;
		});
	});

	/* Filter init */
	$('.filter').each(function () {
		$('.header').addClass('header-filter');
		$('.checkbox, .radio', this).each(function () {
			var _self = $(this);
			$(':checkbox:disabled, :radio:disabled', this).each(function () {
				_self.addClass('disabled');
			});
			$(':checkbox', this).on('change', function () {
				if ($(this).is(':checked')) {
					_self.addClass('checked');
				} else {
					_self.removeClass('checked');
				}
			});
		});
	});

	/* Actions init */
	$('.actions .list .item .h2 span.pre').wrapInner('<span><span></span></span>');

	/* Contacts init */
	$('.contacts').each(function () {
		var _self = $(this);
		$('.toggle', _self).click(function () {
			_self.toggleClass('contacts-hidden');
			return false;
		});
	});

	/* Counter init */
	$('.counter').each(function () {
		var input = $('input:text', this);
		$('.minus', this).click(function () {
			var v = input.val();
			if (v > 0) {
				input.val(+input.val() - 1);
			}
			return false;
		});
		$('.plus', this).click(function () {
			input.val(+input.val() + 1);
			return false;
		});
		input.focus(function () {
			$(this).blur();
			return false;
		});
	});

	/* Cart add init */
	$('.cart-add').each(function () {
		var _self = $(this);
		$('.link', this).click(function () {
			$('input', _self).val(1);
			_self.addClass('cart-add-counter');
			return false;
		});
		$('.minus', this).click(function () {
			var v = +$('input', _self).val();
			if (v === 0) {
				_self.removeClass('cart-add-counter');
			}
		});
	});

	/* Cart init */
	$('.form-cart').each(function () {
		$('.line .plus,.line .minus', this).click(function () {
			refreshCart();
		});
		$('.line .delete', this).click(function () {
			$(this).closest('.line').addClass('deleted');
			refreshCart();
			return false;
		});
		$('.line .revert, .line .restore', this).click(function () {
			var item = $(this).closest('.line');
			item.removeClass('deleted');
			if (+$('.n', item).val() === 0) {
				$('.n', item).val(1);
			}
			refreshCart();
			return false;
		});
	});

	refreshCart();
});