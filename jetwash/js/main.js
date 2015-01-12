/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Init forms */
	$('input, select').styler();

	/* Fastclick for mobile devices */
	FastClick.attach(document.body);

	/* Popup script */
	$(".fancybox-popup").fancybox({
		padding: 0,
		wrapCSS: 'fancybox-red',
		helpers: {
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(255, 255, 255, 0.8)'
				}
			}
		},
		afterClose: function () {
			$('.form', '.form-callback').show();
			$('.success', '.form-callback').hide();
		}
	});

	$('.form-callback').each(function () {
		var _self = $(this);
		$('form', this).on('submit', function (e) {
			e.preventDefault();
			var form = $(this), data = form.serialize();
			$('button', this).text('Отправка...').attr('disabled', 'disabled');
			form.css('opacity', '.5');

			$.post("./handler.php", data).done(function (response) {
				if (response == 'ok') {
					/*yaCounter27583617.reachGoal('LEAD');*/
					form.trigger('reset');
					$('.form', _self).hide();
					$('button', form).text('Отправка').removeAttr('disabled');
					form.css('opacity', '1');
					$('.success', _self).show();
				}
			});
			return false;
		});
		$('.close', this).on('click', function () {
			$.fancybox.close();
			return false;
		});
		$('.hide', this).on('click', function () {
			$('.form', '.form-callback').show();
			$('.success', '.form-callback').hide();
			return false;
		});
	});


	$(".gallery .list a").fancybox({
		autoSize: false,
		fitToView: false,
		padding: 0,
		helpers: {
			media: {}
		}
	});

	$('.timer .account').countdown('2015/03/05', function (event) {
		$(this).html(event.strftime('<div class="col col-days"><span class="time">%D</span><span class="type">дни</span></div><div class="col col-hours"><span class="time">%H</span><span class="type">часы</span></div><div class="col col-minutes"><span class="time">%M</span><span class="type">мин</span></div><div class="col col-seconds"><span class="time red">%S</span><span class="type">сек</span></div>'));
	});

});