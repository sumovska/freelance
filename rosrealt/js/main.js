/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* При входе с устройства с разрешением меньше 640 пкс, сайт отображается в уменьшенном в 2 раза варианте */
(function () {
	if (Math.max(document.documentElement.clientWidth, window.innerWidth || 0) < 640) {
		document.getElementById('viewport').setAttribute("content", "width=device-width, initial-scale=0.5, minimum-scale=0.5, maximum-scale=2.0");
	}
}(document));

/* On document ready */
$(document).ready(function () {

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
	$('textarea').flexible();
	$(document).on('click touchstart', '.file-uploaded .close', function (event) {
		$(this).closest('.file').animate({opacity: 0}, function () {
			$(this).slideUp(function () {
				$(this).remove();
			});
		});
		return false;
	});

	/* Кастомный скролл */
	$('.scroll').perfectScrollbar({
		suppressScrollY: true
	});
	$('.stats .actions').perfectScrollbar({
		suppressScrollX: true
	});
	$('.aside-fixed').perfectScrollbar({
		suppressScrollX: true
	});

	/* Шапка */
	$('.header').each(function () {
		var _header = $(this);
		$(this).append('<a href="#" class="toggle"></a>');
		$('.toggle', this).click(function () {
			_header.toggleClass('open').addClass('visible');
			return false;
		});
	});

	/* Навигация */
	$('.nav').each(function () {
		var body = $('body');
		/* Кнопка 'Зафиксировать/показать меню' */
		$('.toggle', this).click(function () {
			if ($(window).width() <= 1366) {
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
			if ($(window).scrollTop() > 29) {
				body.addClass('nav-top');
			} else {
				body.removeClass('nav-top');
			}
		});
	});

	/* Кнопка закрытия */
	$('.note .close').click(function () {
		$(this).closest('.note').animate({opacity: 0}, function () {
			$(this).slideUp(300, function () {
				$(this).remove();
			});
		});
	});

	/* Инпут с редактированием */
	$('input.secure, textarea.secure, .jq-selectbox.secure').each(function () {
		var input = $(this), space = $(this).closest('.secure-space');
		if ($(this).is('.jq-selectbox')) {
			input = $('select', this);
		}
		$('.icon-edit', space).click(function () {
			space.addClass('secure-space-enabled');
			input.prop('disabled', false).trigger('refresh').focus();
			return false;
		});
		$('.icon-save', space).click(function () {
			if (input.val() === '') {
				input.addClass('error');
			} else {
				input.removeClass('error');
				space.removeClass('secure-space-enabled');
				input.prop('disabled', true).trigger('refresh');
			}
			return false;
		});
	});

	/* Показывает/прячет форму добавления задачи */
	$('.button-task').click(function () {
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
		}).click(function (event) {
			event.stopPropagation();
			return false;
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
		}).click(function (event) {
			event.stopPropagation();
			return false;
		});
	});

	/* Список задач */
	$('.task-list').each(function () {
		$('.task', this).each(function () {
			function toggleSpace(status) {
				if (typeof status === "undefined") {
					status = _self.is('.open');
				}
				_self.addClass('animating');
				if (status) {
					toggle.removeClass('active');
					$('.space', _self).slideUp(300, function () {
						_self.removeClass('open').removeClass('animating');
					});
				} else {
					toggle.addClass('active');
					$('.space', _self).slideDown(300, function () {
						_self.removeClass('animating');
					});
					_self.addClass('open');
				}
				return false;
			}

			var _self = $(this), date = $('.date', this), toggle = $('.toggle', this);
			date.datetimepicker({
				lang: 'ru',
				format: 'd.m.Y',
				closeOnDateSelect: true,
				timepicker: false,
				scrollMonth: false,
				scrollInput: false
			}).click(function (event) {
				event.stopPropagation();
				return false;
			});
			$('.input', this).click(function () {
				if (_self.is('.disabled')) {
					toggleSpace();
				}
			});
			$('.icon-edit', this).click(function () {
				_self.removeClass('disabled');
				toggleSpace(false);
				$(':input', _self).prop('disabled', false).trigger('refresh');
				return false;
			});
			$('.icon-save', this).click(function () {
				_self.addClass('disabled');
				toggleSpace();
				$(':input', _self).prop('disabled', true).trigger('refresh');
				return false;
			});
			$('.icon-delete', this).click(function () {
				_self.slideUp(300, function () {
					_self.remove();
				});
				return false;
			});
			toggle.click(function () {
				toggleSpace();
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
		}).click(function (event) {
			event.stopPropagation();
			return false;
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
		}).click(function (event) {
			event.stopPropagation();
			return false;
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

		function closeNotice() {
			$(this).closest('.entry').animate({opacity: 0}, function () {
				$(this).slideToggle(300, function () {
					$(this).remove();
				});
			});
		}

		var _self = $(this), _map = $('.map').eq(0), _height = +_map.height();

		$('.check-top', this).each(function () {
			var _check = $(this);
			$(window).on('scroll touchmove resize', function () {
				_self.toggleClass('filter-space-subhidden', (_check.offset().top - 20) > _height);
			});
		});

		/* Разворачивание/сворачивание формы */
		$(this).on('click', '.toggle', function () {
			$(this).closest('.filter').find('.inside').slideToggle(300, function () {
				$(this).closest('.filter').toggleClass('open');
				$(window).trigger('resize');
			});
			return false;
		});
		/* Увеличение карты по клику */
		$(this).on('click', '.magnify', function () {
			$(this).toggleClass('minify');
			$('.map').eq(0).toggleClass('small');
			_height = +_map.height();
			$(window).trigger('resize');
			if (typeof(mapCenter) == "function") {
				mapCenter();
			}
			return false;
		});
		/* 'Больше не показывать' уведомления */
		$(this).on('click', '.notice .link', function () {
			closeNotice.call(this);
			return false;
		});
		/* Закрытие уведомлений */
		$(this).on('click', '.notice .close', function () {
			closeNotice.call(this);
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
		$(this).on('click', '.icon-phone', function () {
			$(this).toggleClass('active');
			return false;
		});
	});

	/* Всплывающее окно */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 50
	});

	/* Пейджер */
	$('.pagination').each(function () {
		$(this).on('click', '.next', function () {
			$('.icon', this).toggleClass('icon-preloader');
			return false;
		});
	});

	/* Баг datetimepicker */
	if ($('.xdsoft_datetimepicker').length > 0) {
		$(document).on('click touchstart', function (event) {
			var target = $(event.target);
			if ($('.xdsoft_datetimepicker:visible').length > 0) {
				if ((target.closest('.xdsoft_datetimepicker').length === 0)) {
					$('.xdsoft_datetimepicker').hide();
				}
			}
		});
	}

	/* Подвал */
	$('.footer').each(function () {
		var _buttons = $('.help, .messages', this);
		_buttons.each(function () {
			var _self = $(this);
			$('.toggle', this).click(function () {
				$(this).parent().siblings('.active').removeClass('active').find('.dropdown').hide();
				$('.dropdown', _self).fadeToggle(300, function () {
					_self.toggleClass('active');
				});
				return false;
			});
			$('.sub', this).click(function () {
				$(this).siblings('ul').slideToggle(function () {
					$(this).closest('li').toggleClass('open');
				});
				return false;
			});
		});
		$(document).on('click touchstart', function (event) {
			var target = $(event.target);
			if ($('.dropdown:visible').length > 0) {
				if ((target.closest('.dropdown').length === 0) && (target.closest('.footer').length === 0)) {
					_buttons.removeClass('active');
					$('.dropdown:visible', _buttons).fadeOut(300);
				}
			}
		});
	});

	/* Тултипы раздела 'Помощь' */
	$.ajax({
		url: "help.html",
		cache: false
	}).done(function (html) {
		$('body').append('<div class="overlay"></div>').append(html);
		$('[data-tooltip-link]').each(function () {
			var _w = 415, _link = $(this), _id = +_link.attr('data-tooltip-link'), _source = $('[data-tooltip-source=' + _id + ']'), _pointer = $('[data-tooltip-pointer="' + _id + '"]');
			if (_source.is('[data-width]')) {
				_w = _source.attr('data-width');
			}
			_pointer.tooltipster({
				content: _source.html(),
				theme: 'tooltipster-help',
				minWidth: _w,
				maxWidth: _w,
				position: _source.attr('data-position'),
				offsetX: _source.attr('data-offset-x'),
				offsetY: _source.attr('data-offset-y'),
				trigger: '',
				contentAsHTML: true,
				autoClose: true,
				onlyOne: true,
				interactive: true,
				positionTracker: true,
				functionReady: function (origin, tooltip) {
					$(tooltip).attr('data-pointer', $(origin).attr('data-tooltip-pointer'));
					if (_source.is('[data-class]')) {
						$(tooltip).addClass(_source.attr('data-class'));
					}
				},
				functionBefore: function (origin, continueTooltip) {
					$('.overlay').fadeIn(200);
					continueTooltip();
				}
			});
			_link.click(function () {
				/*$(this).closest('li').toggleClass('active').siblings('li.active').removeClass('active');*/
				_pointer.tooltipster('show');
				return false;
			});
		});
		$(document).on('click touchstart', '.tooltipster-base .prev', function (event) {
			$('[data-tooltip-pointer="' + $(this).attr('data-prev') + '"]').tooltipster('show');
			return false;
		});
		$(document).on('click touchstart', '.tooltipster-base .next', function (event) {
			$('[data-tooltip-pointer="' + $(this).attr('data-next') + '"]').tooltipster('show');
			return false;
		});
		$(document).on('click touchstart', '.tooltipster-base .close', function (event) {
			$('[data-tooltip-pointer="' + $(this).closest('.tooltipster-base').attr('data-pointer') + '"]').tooltipster('hide');
			$('.overlay').fadeOut(100);
			return false;
		});
		$(document).on('click touchstart', function (event) {
			var target = $(event.target), a = $('.tooltipster-base:visible');
			if (a.length > 0) {
				if ((target.closest('.tooltipster-base').length === 0) && (!target.is('.tooltipster-base'))) {
					a.each(function () {
						$('[data-tooltip-pointer="' + $(this).attr('data-pointer') + '"]').tooltipster('hide');
						$('.overlay').fadeOut(100);
					})
				}
			}
		});
	});

	/* Баги в IE */
	if ($.browser.msie && $.browser.version < 10) {
		$(":input[placeholder]").each(function () {
			$(this).val($(this).attr('placeholder'));
			$(this).focus(function () {
				if ($(this).val() === $(this).attr('placeholder')) {
					$(this).val('');
				}
			});
			$(this).blur(function () {
				if ($(this).val() === '') {
					$(this).val($(this).attr('placeholder'));
				}
			});
		});
		$('.jq-file').each(function () {
			var _self = $(this);
			$('.jq-file__name', this).click(function () {
				$('input[type=file]', _self).trigger('click');
			});
		});
	}
});