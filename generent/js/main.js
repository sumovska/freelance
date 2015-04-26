/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true, node: true */
/*global window, console, document, $, jQuery, PIE, initialize, styler */

function initForms() {
	$('input, select').styler();
}

/* On document ready */
$(document).ready(function () {

	/* Формы */
	initForms();

	/* Табы */
	$('.tabs').each(function () {
		$('li a', this).click(function () {
			var where = $(this).attr("href").replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$('#' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Карусель маленькая (в сайдбаре) */
	$('.slider-small').each(function () {
		$('.slider-in').slick({
			arrows: false,
			dots: true
		});
		$('.slick-dots button').remove();
		$('.slick-dots li').append('<span class="dots"></span>');
	});

	/* Выпадающее меню */
	$('.header', this).append('<span class="toggle"></span>');
	$('.toggle', this).click(function (event) {
		$(this).toggleClass('open');
		$('.nav').each(function () {
			var _self = $(this);
			$(this).toggleClass('open');
			if (_self.hasClass('open')) {
				$(document).on('click touchstart', closeMenu);
			} else {
				$(document).off('click touchstart', closeMenu);
			}
			event.preventDefault();
		});
	});

	/*  Подменю */
	$('.nav-in > li', this).each(function () {
		if ($(this).children('ul').length > 0) {
			$(this).addClass('sub');
		}
		$(this).children('a').on('click', function (event) {
			if ($(window).width() <= 999) {
				$(this).closest('li').toggleClass('open');
				event.preventDefault();
			}
		});
	});


	/*$('.clients').each(function () {
		$('.item', this).on('mouseenter', function () {
			$(this).animate(
				$(this).find('.describe').fadeIn()
			)
		}).on('mouseleave', function () {
			$(this).removeClass('visible').find('.describe').fadeOut();
		});
	});*/

	/*  Информационный список */
	$('.info-list').each(function(){
		$('.heading', this).click(function(){
			$(this).toggleClass('open').siblings('.in').slideToggle(200);
			return false;
		});
	});

});

