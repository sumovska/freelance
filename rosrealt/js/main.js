/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Сокраещние интервала по клику для тач-девайсов */
	FastClick.attach(document.body);

	/* Формы */
	$('input, select').styler();
	/* input:file с подгрузкой превью */
	$('input.file-photo').change(function () {
		if ($(this).prop('files') && $(this).prop('files')[0]) {
			var reader = new FileReader(), img = $(this).closest('.jq-file').find('.jq-file__img');
			reader.onload = function (e) {
				img.attr('src', e.target.result);
			};
			if (img.length === 0) {
				$(this).closest('.jq-file').append('<img class="jq-file__img" alt=""/>');
				img = $(this).closest('.jq-file').find('.jq-file__img');
			}
			reader.readAsDataURL($(this).prop('files')[0]);
		}
	});

	/* Навигация */
	$('.nav').each(function () {
		var body = $('body');
		/* Кнопка 'Зафиксировать/показать меню' */
		$('.toggle', this).click(function () {
			if ($(window).width() < 1280) {
				body.toggleClass('nav-fixed');
			} else {
				body.toggleClass('nav-closed');
			}
			return false;
		});
		/* Кнопка 'Вверх' - перемотка наверх сайта */
		$('.top', this).click(function () {
			$("html, body").animate({scrollTop: 0}, "slow");
			return false;
		});
		/* Появление/исчезновение кнопки 'Вверх' */
		$(window).on('scroll touchmove', function () {
			if ($(window).scrollTop() > 49) {
				body.addClass('nav-top');
			} else {
				body.removeClass('nav-top');
			}
		});
		$(window).scroll();
	});

	/* Кнопка закрытия */
	$('.note .close').click(function () {
		$(this).closest('.note').slideUp(100);
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

	/* Подвал */
	$('.footer').each(function () {
		var _buttons = $('.help, .messages', this);
		_buttons.each(function () {
			var _self = $(this);
			$('.toggle', this).click(function () {
				console.log(_buttons.filter('.active'));
				$(this).parent().siblings('.active').removeClass('active').find('.tooltip').hide().removeAttr('style');
				$('.tooltip', _self).fadeToggle(100, function () {
					_self.toggleClass('active');
				});
				return false;
			});
			$('.sub', this).click(function () {
				$(this).closest('li').toggleClass('open').siblings('li.open').removeClass('open');
				return false;
			});
			$('body').bind("click", function (event) {
				var target = $(event.target);
				if (target.closest('.tooltip').length === 0) {
					_self.removeClass('active');
					$('.tooltip', _self).hide();
				}
			});
		});
	});

	/* Фильтр */
	$('.filter-space').each(function () {
		function cbChange(event) {
			$('.check-top', _self).toggleClass('visible', $(this).is(':checked'));
			if (typeof event != "undefined") {
				event.stopPropagation();
			}
		}

		var _self = $(this);
		/* Разворачивание/сворачивание формы */
		$(this).on('click', '.toggle', function () {
			$(this).closest('.filter').find('.inside').slideToggle(200, function () {
				$(this).closest('.filter').toggleClass('open');
				return false;
			});
		});
		/* Увеличение карты по клику */
		$(this).on('click', '.magnify', function () {
			$(this).toggleClass('minify');
			$('.block-owners').toggleClass('block-owners-full');
			$('.map').eq(0).toggleClass('small');
			if (typeof(mapCenter) == "function") {
				mapCenter();
			}
			return false;
		});
		/* 'Больше не показывать' уведомления */
		$(this).on('click', '.notice .link', function () {
			$(this).closest('.entry').slideToggle(200);
			return false;
		});
		/* Закрытие уведомлений */
		$(this).on('click', '.notice .close', function () {
			$(this).closest('.entry').slideToggle(200);
			return false;
		});
		/* Разворачивание/сворачивание формы */
		$(this).on('change', '.checkbox-top', cbChange);
		cbChange.call($('.checkbox-top'));
	});

	$('.table-owners').each(function () {
		/* Иконка 'добавить в закладки' */
		$(this).on('click', '.link-pin', function () {
			$(this).toggleClass('icon-pinhover').toggleClass('active').closest('.tr').toggleClass('active');
			return false;
		});
	});

	/* Всплывающее окно */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 50
	});
});