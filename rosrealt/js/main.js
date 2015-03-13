/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Fastclick */
	FastClick.attach(document.body);

	/* Формы */
	$('input:not(.file-photo), select').styler();
	$('input.file-photo').styler({
		filePlaceholder: 'Добавить<br>фото'
	});

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

	/* Список задач */
	$('.task-list').each(function () {
		$('.task', this).each(function () {
			var _self = $(this);
			$('.toggle', this).click(function () {
				$(this).toggleClass('active');
				$('.space', _self).slideToggle(300, function () {
					_self.toggleClass('open');
				});
				return false;
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