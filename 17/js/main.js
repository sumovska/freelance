/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {
	$('.catalog').each(function () {
		var _self = (this);
		$('.toggle, .js-toggle', this).click(function () {
			var item = $(this).closest('.item');
			$('.area', item).slideToggle(300, 'swing', function () {
				item.toggleClass('active');
			});
			return false;
		});
		$('.check-all', this).click(function () {
			if (this.checked) {
				$('.item input:checkbox', _self).prop("checked", true);
			} else {
				$('.item input:checkbox', _self).prop("checked", false);
			}
		});
	});
	$('.form-recommendations').each(function () {
		var _self = (this);
		$('.checkbox-toggle input', _self).click(function () {
			if (this.checked) {
				$(this).closest('.col').find('input:text').attr('disabled', 'disabled');
			} else {
				$(this).closest('.col').find('input:text').removeAttr('disabled');
			}
		});
	});
});
