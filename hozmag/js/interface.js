/*jslint white: true, browser: true, onevar: false, undef: true, nomen: false, eqeqeq: true, plusplus: true, bitwise: true, regexp: false, newcap: true */
/*global window, console, document, $, jQuery, PIE */

function Site() {
	var self = this;

	this.search = $('.search');
	this.tabs = $('.tabs');
	this.popup = $('.popup');
	this.tooltip = $('.tooltip');
	this.linkPopup = $('.link-popup');
	this.linkTooltip = $('.link-tooltip');

	this.init = function () {
		initMenu();
		initSearch();
		initCarousel();
		initGallery();
		initPopup();
		initTooltip();
		initClueTip();
		initTabs();
		initForms();
		initIE();
	};

	function initMenu() {
		$('.header .nav').each(function () {
			var _self = $(this);
			$('.drop', this).click(function () {
				var ed = _self.find('.list-more').eq(0);
				if (ed.is(':visible')) {
					ed.hide();
					$(this).removeClass('drop-active');
				} else {
					ed.show();
					$(this).addClass('drop-active');
				}
				return false;
			});
		});
	}

	function initSearch() {
		self.search.each(function () {
			$('input:text', this).focus(function () {
				if ($(this).val() === 'Поиск по каталогу') {
					$(this).val('');
				}
			});
			$('input:text', this).blur(function () {
				if ($(this).val() === '') {
					$(this).val('Поиск по каталогу');
				}
			});
		});
	}

	function initCarousel() {
		$('.catalog-list-carousel-horizontal').bxSlider({
			mode: 'horizontal',
			slideWidth: 130,
			minSlides: 4,
			maxSlides: 4,
			moveSlides: 4,
			easing: 'swing',
			pager: false,
			infiniteLoop: false
		});
		$('.catalog-list-carousel-vertical').bxSlider({
			mode: 'vertical',
			pager: false,
			minSlides: 2,
			maxSlides: 2,
			moveSlides: 1,
			infiniteLoop: false
		});
	}

	function initGallery() {
		$(".fancybox").fancybox({
			openEffect: 'none',
			closeEffect: 'none'
		});
	}

	function initTooltip() {
		self.linkTooltip.on('click', function () {
			self.toggleTooltip.call(this);
			return false;
		});
		self.tooltip.each(function () {
			var _this = this;
			$('.close', this).click(function () {
				$(_this).hide();
				self.linkTooltip.filter('.dropdown').removeClass('dropdown-active');
				return false;
			});
		});
	}

	function initClueTip() {
		$('a.cluetip').cluetip({
			width: 435,
			showTitle: false,
			attribute: 'data-url',
			cluetipClass: 'tooltip tooltip tooltip-item',
			cluezIndex: 120,
			dropShadow: false,
			cursor: 'pointer',
			sticky: true,
			mouseOutClose: 'both',
			ajaxCache: false,
			ajaxSettings: {
				dataType: 'json'
			},
			ajaxProcess: function(data) {
				var html = '<div class="catalog-list"><div class="item"><div class="cell-pic"><p class="pic"><img src="' + data.pic_url + '" alt="' + data.pic_alt + '"></p></div><div class="cell-info"><p class="title"><a href="' + data.uri + '">' + data.name + '</a></p><div class="both"><p class="rating rating-' + data.rating + '"></p></div><p class="info">' + data.info + '</p><p class="price"><var>' + data.price + ' руб</var> за шт.</p><p class="amount">кол-во<input type="text" value="1"></p><div class="both"><p class="add"><a href="#">В корзину</a></p><p class="go"><a href="' + data.uri + '">На страницу <br>товара</a>&nbsp;<span class="red">&raquo;</span></p></div></div></div></div>';
				return html;
			}
		});
	}

	this.toggleTooltip = function () {
		var link = $(this), where = $(this).attr("href").replace(/^.*#(.*)/, "$1"), target = $('#' + where);
		if (target.is(':visible')) {
			link.removeClass('dropdown-active');
			self.hideTooltips();
		} else {
			target.animate({
				opacity: 0
			}, 0).show();
			target.toggle(0, function () {
				$(this).css('margin-left', 10 - Math.floor($('.area').eq(0).width() / 2 - (link.offset().left - ($('body').eq(0).width() - $('.area').eq(0).width()) / 2)));
				$(this).css('left', '50%');
				$(this).css('top', Math.floor(link.offset().top));
			});
			target.animate({
				opacity: 1
			}, 0).show();
			if ($.browser.msie) {
				if (window.PIE) {
					target.each(function () {
						PIE.attach(this);
					});
				}
			}
			link.addClass('dropdown-active');
			$('body').bind('mousedown', function (e) {
				if (($(e.target).closest('.tooltip').length < 1) && (!$(e.target).is('.tooltip')) && ($(e.target).get(0) != link.get(0))) {
					link.removeClass('dropdown-active');
					self.hideTooltips();
					$(this).unbind('mousedown');
				}
			});
		}
	};

	this.hideTooltips = function () {
		if ($.browser.msie) {
			if (window.PIE) {
				self.tooltip.filter(':visible').each(function () {
					PIE.detach(this);
				});
			}
		}
		self.tooltip.filter(':visible').not('.tooltip-item').hide();
		return false;
	};

	function initPopup() {
		self.popup.each(function () {
			var _this = this;
			$('.close', this).click(function () {
				$(_this).hide();
				self.linkPopup.filter('.dropdown').removeClass('dropdown-active');
				return false;
			});
		});
		self.linkPopup.on('click', function () {
			var link = $(this), where = $(this).attr("href").replace(/^.*#(.*)/, "$1"), target = $('#' + where);
			target.toggle(1, function () {
				if ($(this).is(':visible')) {
					link.addClass('dropdown-active');
					if ($.browser.msie) {
						if (window.PIE) {
							PIE.attach(this);
						}
						if ($.browser.version < 8) {
							$('.popup-cart .cart-form .line-submit').each(function () {
								$(this).width($(this).closest('.popup').width());
							});
						}
					}
				} else {
					link.removeClass('dropdown-active');
					if ($.browser.msie) {
						if (window.PIE) {
							PIE.detach(this);
						}
					}
				}
			});
			return false;
		});
	}

	function initTabs() {
		self.tabs.each(function () {
			$('li a', this).click(function () {
				var where = $(this).attr("href").replace(/^.*#(.*)/, "$1"), space = $(this).closest('.tabs-space');
				$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
				space.find('.' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
				return false;
			});
		});
	}

	function initForms() {
		$('.radiobox-colors').each(function () {
			$('.radiobox:not(".radiobox-inited")', this).each(function () {
				var self = $(this);
				$(':radio', this).live('change',function () {
					$(this).trigger('redraw');
				}).live('redraw', function () {
						$(this).closest('.color').addClass('color-active').siblings('.color-active').removeClass('color-active');
					});
				self.wrapInner('<span class="radiobox-colors-space"></span>').append('<span class="hint">' + self.attr('title') + '</span>');
				self.addClass('radiobox-inited').removeAttr('title');
			});
		});
		$('.radiobox-group').each(function () {
			$('.radiobox:not(".radiobox-inited")', this).each(function () {
				var self = $(this);
				$(':radio', this).live('change',function () {
					$(this).trigger('redraw');
				}).live('redraw', function () {
						$(this).closest('.radiobox').addClass('radiobox-active').removeClass('radiobox-inactive').siblings('.radiobox-active').removeClass('radiobox-active').addClass('radiobox-inactive');
						if ($.browser.msie) {
							if (window.PIE) {
								$(this).closest('.radiobox').each(function () {
									PIE.detach(this);
								}).siblings('.radiobox-inactive').each(function () {
										PIE.attach(this);
									});
							}
						}
					});
				if ($(':radio', this).prop('checked', true)) {
					$(this).closest('.radiobox').addClass('radiobox-active').removeClass('radiobox-inactive').siblings('.radiobox-active').removeClass('radiobox-active').addClass('radiobox-inactive');
				}
				self.addClass('radiobox-inited');
			});
		})
	}

	function initIE() {
		if ($.browser.msie && $.browser.version < 9) {
			if (window.PIE) {
				$('.banners img, .block, .title-red, .promo, .promo .text, .promo .pic img, .promo .side .free .title, input[type="submit"], .block-tabs .tabs li a, .cart-form .line-submit, .form-cart-contents .tab, .form-cart input[type="text"], .form-cart textarea, .form-cart .pink, .radiobox-group').each(function () {
					PIE.attach(this);
				});
			}
			if ($.browser.version < 9) {
				$('.header .links li:first, .header .nav .list > li:first, .footer .nav > li:first').addClass('first-child');
				$('.header .nav .list > li:nth-child(2)').addClass('nth-child-2');
				$('.catalog-list-2col .item:nth-child(2n)').addClass('nth-child-2n');
				$('.catalog-list-4col .item:nth-child(4n)').addClass('nth-child-4n');
				$('.header .nav .list > li:last-child, .ui-range-slider .ui-slider-handle:last-child, .range-slider .range-steps li:last-child, .header .sub-col .sub-list:last-child').addClass('last-child');
				$('.header .nav .list > li.sub, .hint').append('<i class="before"></i>');
			}
			if ($.browser.version < 8) {
				$('.header, .header > .space, .header .login a, .header .cart a, .header .small li, .promo .side .regions, a.dropdown, .promo .side .fit, .title-red, .header .nav .list > li > a, .cart-form .title, .form-cart-contents .tab .delete, .item-info .pic .big a, .catalog-list .title .size, .filter .clear-filters, .header .sub-list li.strong, .radiobox-group .radiobox').append('<i class="before"></i>');
				$('.header, .header > .space, .header .nav .drop, .title-red').append('<i class="after"></i>');
				$('.wrap').append('<i class="wrap-before"></i><i class="wrap-after"></i>');
			}
		}
	}
}

function buildSliderRange(rangeMin, rangeMax, rangeStep) {
	var steps = (rangeMax - rangeMin) / rangeStep, step = 100 / steps;
	var list = $('<ul class="range-steps"></ul>'), line;
	for (var i = 0; i < steps + 1; i = i + 1) {
		line = $('<li style="left:' + step * i + '%"></li>');
		if (i % 2 === 0) {
			line.append('<span class="var">' + (rangeMin + rangeStep * i) + '</span>');
		}
		list.append(line);
	}
	$(this).prepend(list);
}

$(document).ready(function () {
	window.site = new Site();
	window.site.init();
});