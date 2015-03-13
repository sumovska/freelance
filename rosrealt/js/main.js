/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Fastclick */
	FastClick.attach(document.body);

	/* Формы */
	$('input, select').styler();

	/* Навигация */
	$('.nav').each(function () {
		var body = $('body');
		$('.toggle', this).click(function () {
			if ($(window).width() < 1280) {
				body.toggleClass('nav-fixed');
			} else {
				body.toggleClass('nav-closed');
			}
			return false;
		});
	});

	/* Кнопка закрытия */
	$('.note .close').click(function () {
		$(this).closest('.note').fadeOut();
	});

	/* Инпут с редактированием */
	$('input.secure, textarea.secure, .jq-selectbox.secure').each(function () {
		var input = $(this), space = $(this).closest('.secure-space');
		if ($(this).is('.jq-selectbox')) {
			input = $('select', this);
		}
		$('.icon-edit', space).click(function () {
			space.addClass('secure-space-enabled');
			input.prop('disabled', false).trigger('refresh');
		});
		$('.icon-save', space).click(function () {
			space.removeClass('secure-space-enabled');
			input.prop('disabled', true).trigger('refresh');
		});
	});

	/* Показывает/прячет форму добавления задачи */
	$('.add-task').click(function () {
		$('.task-create').slideToggle(300, 'swing');
		return false;
	});

	/* Новая задача */
	$('.task-create').each(function () {
		var from = $('.date-from', this), to = $('.date-to', this);
		from.datetimepicker({
			lang: 'ru',
			format: 'd.m.Y',
			closeOnDateSelect: true,
			timepicker: false,
			scrollMonth: false,
			scrollInput: false,
			onShow: function () {
				this.setOptions({
					maxDate: to.val() ? to.val() : false
				})
			}
		});
		to.datetimepicker({
			lang: 'ru',
			format: 'd.m.Y',
			closeOnDateSelect: true,
			timepicker: false,
			scrollMonth: false,
			scrollInput: false,
			onShow: function () {
				this.setOptions({
					minDate: from.val() ? from.val() : false
				})
			}
		});
	});

	/* Список задач */
	$('.task-list').each(function () {
		$('.task', this).each(function () {
			var _self = $(this), date = $('.date', this);
			date.datetimepicker({
				lang: 'ru',
				format: 'd.m.Y',
				closeOnDateSelect: true,
				timepicker: false,
				scrollMonth: false,
				scrollInput: false
			});
			$('.icon-edit', this).click(function () {
				_self.removeClass('disabled').addClass('editing');
				$(':input', _self).prop('disabled', false).trigger('refresh');
				return false;
			});
			$('.icon-save', this).click(function () {
				_self.addClass('disabled').removeClass('editing').removeClass('open');
				$(':input', _self).prop('disabled', true).trigger('refresh');
				return false;
			});
			$('.icon-delete', this).click(function () {
				_self.remove();
				return false;
			});
			$('.toggle', this).click(function () {
				$(this).toggleClass('active');
				_self.toggleClass('open');
				return false;
			});
		});
	});

	/* Статистика задач */
	$('.stats .date').each(function () {
		var from = $('.date-from', this), to = $('.date-to', this);
		from.datetimepicker({
			lang: 'ru',
			format: 'd.m.Y',
			closeOnDateSelect: true,
			timepicker: false,
			scrollMonth: false,
			scrollInput: false,
			onShow: function () {
				this.setOptions({
					maxDate: to.val() ? to.val() : false
				})
			}
		});
		to.datetimepicker({
			lang: 'ru',
			format: 'd.m.Y',
			closeOnDateSelect: true,
			timepicker: false,
			scrollMonth: false,
			scrollInput: false,
			onShow: function () {
				this.setOptions({
					minDate: from.val() ? from.val() : false
				})
			}
		});
	});

	$('.footer').each(function () {
		$('.help', this).each(function () {
			var _help = $(this);
			$('.toggle', this).click(function () {
				_help.toggleClass('active');
				$('.sub', _help).click(function () {
					$(this).closest('li').toggleClass('open').siblings('li.open').removeClass('open');
					return false;
				});
				return false;
			});
			$('body').bind("click", function (event) {
				var target = $(event.target);
				if ((target.closest('.tooltip-help').length === 0)) {
					_help.removeClass('active');
				}
			});
		});
	});

	/* Фильтр */
	$('.filter').each(function () {
		$('.toggle').click(function () {
			$(this).siblings('.inside').fadeToggle();
			return false;
		});
	});
});