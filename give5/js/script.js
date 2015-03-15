/*jslint white: true, browser: true, onevar: false, undef: true, nomen: false, eqeqeq: true, plusplus: true, bitwise: true, regexp: false, newcap: true */
/*global window, console, document, $, jQuery, PIE */

(function($){
	$.fn.disableSelection = function() {
		return this
			.attr('unselectable', 'on')
			.css('user-select', 'none')
			.on('selectstart', false);
	};
})(jQuery);

function Site() {
	this.initInterface = function () {
		$('.header .city .l a').click(function () {
			var li = $(this).closest('li'), ul = li.closest('ul');
			if (ul.toggleClass('l-opened').not('.l-opened')) {
				li.addClass('active').clone(true).prependTo(ul).siblings('.active').removeClass('active');
				li.remove();
			}
			return false;
		});

		$('.header .search input:text').focus(function () {
			if ($(this).val() === 'ПОИСК') {
				$(this).val('');
			}
		}).blur(function () {
				if ($(this).val() === '') {
					$(this).val('ПОИСК');
				}
			});

		$('.footer .subscribe input:text').focus(function () {
			if ($(this).val() === 'Укажите Ваш E-mail') {
				$(this).val('');
			}
		}).blur(function () {
				if ($(this).val() === '') {
					$(this).val('Укажите Ваш E-mail');
				}
			});

		$('.header .nav-category').find('li:last-child').addClass('last');

		$('.nav-section .list').each(function () {
			$(this).children('li').children('.toggle').click(function () {
				var li = $(this).closest('li');
				if (!li.is('.open')) {
					li.siblings('.open').find('ul').slideUp(200);
					$(this).siblings('ul').slideDown(200);
					li.addClass('open').siblings('li.open').removeClass('open');
				} else {
					$(this).siblings('ul').slideUp(200);
					li.removeClass('open');
				}
				return false;
			});
			$(this).children('.active').addClass('open').children('ul').show();
		});

		$('.gallery').each(function () {
			$('.carousel .list', this).jcarousel({
				scroll: 1,
				wrap: 'both',
				buttonNextHTML: '<p></p>',
				buttonPrevHTML: '<p></p>',
				initCallback: function (carousel) {
					$('.list a', carousel.container).click(function () {
						var attr = $(this).attr('href').replace(/^.*#(.*)/, "$1");
						$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
						$(this).closest('.gallery').find('.pic img').attr('src', attr).end().find('.pic a').attr('href', attr);
						return false;
					});
					$(carousel.container).disableSelection();
				}
			});
			$('.pic a', this).fancybox();
		});

		$('select').each(function () {
			$(this).selectbox();
		});

		$('.item-description').each(function () {
			$('.tabs', this).find('a').click(function () {
				var attr = $(this).attr('href').replace(/^.*#(.*)/, "$1");
				$(this).closest('li').addClass('active').siblings('.active').removeClass('active');
				$(this).closest('.item-description').find('.' + attr).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
				return false;
			});
		});

		$('.catalog-block').each(function () {
			$('.catalog', this).find('li:last-child').addClass('last-child');
			$('.carousel .catalog', this).jcarousel({
				scroll: 1,
				wrap: 'both',
				buttonNextHTML: '<p></p>',
				buttonPrevHTML: '<p></p>',
				initCallback: function (carousel) {
					$(carousel.container).disableSelection();
				}
			});
		});

		$('.nav-items').each(function () {
			$('.plus', this).click(function () {
				$(this).closest('li').addClass('active').siblings('li.active').find('.tooltip').fadeOut(200);
				$(this).siblings('.tooltip').fadeIn(200);
				return false;
			});
			$('.tooltip .close', this).click(function () {
				$(this).closest('li').removeClass('active');
				$(this).closest('.tooltip').fadeOut(200);
				return false;
			});
		});

		/* Checkboxes */
		$('label.checkbox:not(".checkbox-inited")').each(function () {
			$(':checkbox', this).live('change',function () {
				$(this).trigger('redraw');
			}).on('redraw', function () {
					if ($(this).is(':checked')) {
						$(this).closest('.checkbox').addClass('checkbox-checked');
					} else {
						$(this).closest('.checkbox').removeClass('checkbox-checked');
					}
				});
			if ($(':checkbox', this).is(':checked')) {
				$(this).addClass('checkbox-checked');
			}
			$(this).addClass('checkbox-inited');
		});

		$('.block-filters').each(function () {
			$('label.checkbox :checkbox', this).live('redraw', function () {
				if ($(this).is(':checked')) {
					$(this).closest('li').addClass('active');
				} else {
					$(this).closest('li').removeClass('active');
				}
			});
			$('label.checkbox-checked', this).each(function () {
				$(this).closest('li').addClass('active');
			});
		});

		$('.index-slider').each(function () {
			$('.carousel .list', this).jcarousel({
				scroll: 1,
				auto: 5,
				wrap: 'both',
				buttonNextHTML: '<p></p>',
				buttonPrevHTML: '<p></p>',
				initCallback: function (carousel) {
					var current = $(carousel.container);
					$(current).append('<ul class="pages"></ul>');
					var pager = $('.pages', current);
					for (var i = carousel.size(); i >= 1; i = i - 1) {
						pager.prepend("<li><a href='#" + i + "'>" + i + "</a></li>");
					}
					$('li a', pager).click(function () {
						carousel.scroll($.jcarousel.intval($(this).text()));
						carousel.stopAuto();
						return false;
					});
					$(carousel.container).disableSelection();
				},
				itemLoadCallback: function (carousel) {
					var current = $(carousel.container);
					$('.pages', current).find('li.active').removeClass('active').end().find('li').eq(carousel.first - 1).addClass('active');
				}
			});
		});

		$('.gallery-slider').each(function () {
			$('.carousel .list', this).jcarousel({
				scroll: 1,
				wrap: 'both',
				buttonNextHTML: '',
				buttonPrevHTML: '',
				initCallback: function (carousel) {
					$(carousel.container).append('<div class="prevnext"><a class="prev" href="#prev"></a><span class="count"><var class="counter">1</var> из ' + carousel.size() + '</span><a class="next" href="#next"></a></div>');
					$('.prev', carousel.container).click(function () {
						carousel.prev();
						return false;
					});
					$('.next', carousel.container).click(function () {
						carousel.next();
						return false;
					});
					$(carousel.container).disableSelection();
				},
				itemLoadCallback: function (carousel) {
					$('.prevnext .counter', carousel.container).text(carousel.first);
				}
			});
		});

		$('.cart .link a.tool').click(function () {
			var attr = $(this).attr('href').replace(/^.*#(.*)/, "$1");
			$('.overlay').show();
			$('.tooltip-' + attr).show();
			return false;
		});
		$('.fav a.tool').click(function () {
			var attr = $(this).attr('href').replace(/^.*#(.*)/, "$1");
			$('.tooltip-' + attr).toggle();
			return false;
		});
		$('.overlay').click(function () {
			$('.tooltip').hide();
			$('.overlay').hide();
			return false;
		});
		$('.tooltip-cart').each(function () {
			$('.catalog .remove').click(function () {
				$(this).closest('li').remove();
				return false;
			});
		});

		$('.fav').each(function () {
			$('li a').click(function () {
				$(this).closest('li').toggleClass('active').siblings('.active').removeClass('active');
			});
		});

		if ($.browser.msie && $.browser.version < 9) {
			$('.block-filters, .nav-section').each(function () {
				$(this).append('<div class="before"></div><div class="after"></div>');
			});
			if (window.PIE) {
				$('.sbHolder, .header .nav-brands, .header .search input[type="text"], .footer .subscribe fieldset, .footer .subscribe input[type="text"], .block, .catalog-block .heading, .catalog .buy, .nav-items > .list .tooltip, .item-form .submit, .three-blocks > li, .quote').each(function () {
					PIE.attach(this);
				});
			}
		}

		$('.brands-list li:last-child').addClass('last');
	};
	this.init = function () {
		this.initInterface();
	};
}

$(document).ready(function () {
	window.site = new Site();
	window.site.init();
});