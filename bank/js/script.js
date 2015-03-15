/*jslint white: true, browser: true, onevar: false, undef: true, nomen: false, eqeqeq: true, plusplus: true, bitwise: true, regexp: false, newcap: true */
/*global window, console, document, $, jQuery, PIE */

function Site() {
	this.initInterface = function () {
		var maxCol = 0;
		$('.profile-page:not(.create-page)').each(function () {
			$('.block-col', this).each(function () {
				var h = $(this).height();
				if (h > maxCol) {
					maxCol = h;
				}
			});
			$('.block-col', this).each(function () {
				$('.form-grey', this).css('min-height', maxCol - $('.form-grey', this).siblings().outerHeight(true) - 28);
			});
		});
		$('.multiply').click(function () {
			$(this).prevAll(":input").eq(0).clone(true, true).css('margin-top', '7px').val('').insertBefore(this);
		});
		$('select').each(function () {
			$(this).selectbox("detach");
			$(this).selectbox({
				effect: "fade",
				speed: 100,
				onOpen: function (inst) {
					$(inst.input).nextAll('.sbHolder').eq(0).addClass('sbHolderOpen');
				},
				onClose: function (inst) {
					$(inst.input).nextAll('.sbHolder').eq(0).removeClass('sbHolderOpen');
				}
			});
			$(this).nextAll('.sbHolder').eq(0).addClass($(this).attr('class'));
		});
		$('.container').each(function () {
			var pad = $('.footer').outerHeight(true);
			if ($('.area-fixed').length > 0) {
				pad = pad + $('.area-fixed').outerHeight(true);
			}
			pad = pad + 14;
			$(this).css('padding-bottom', pad);
		});

		$('.messages-users').each(function () {
			$('.user-list-2', this).each(function () {
				$('a', this).click(function () {
					$(this).closest('li').toggleClass('active').siblings('li.active').removeClass('active');
					return false;
				});
			});
		});

		function checkboxRedraw() {
			if ($(this).is(':checked')) {
				$(this).closest('.checkbox').addClass('checkbox-checked');
			} else {
				$(this).closest('.checkbox').removeClass('checkbox-checked');
			}
		}

		function radioboxRedraw() {
			var na = $(this).attr('name');
			$('[name="' + na + '"]').closest('label').removeClass('radiobox-checked');
			if ($(this).is(':checked')) {
				$(this).closest('.radiobox').addClass('radiobox-checked');
			} else {
				$(this).closest('.radiobox').removeClass('radiobox-checked');
			}
		}

		function checkboxChange() {
			$(this).trigger('redraw');
		}

		$('.checkbox:not(".checkbox-inited")').each(function () {
			$(':checkbox', this).live('change', checkboxChange).live('redraw', checkboxRedraw);
			if ($(':checkbox', this).is(':checked')) {
				$(this).addClass('checkbox-checked');
			}
			$(this).addClass('checkbox-inited');
		});

		$('.radiobox:not(".radiobox-inited")').each(function () {
			$(':radio', this).live('change', checkboxChange).live('redraw', radioboxRedraw);
			if ($(':radio', this).is(':checked')) {
				$(this).addClass('radiobox-checked');
			}
			$(this).addClass('radiobox-inited');
		});

		$('.index').each(function () {
			var index = $(this);
			index.masonry({
				itemSelector: '.block',
				isAnimated: true,
				animationOptions: {
					duration: 300,
					easing: 'linear',
					queue: false
				}
			});
			index.find('.block').each(function () {
				$(this).hover(function () {
					$('.close', this).show(200);
				}, function () {
					$('.close', this).hide(200);
				});
				$('.close a', this).click(function () {
					index.masonry('remove', $(this).closest('.block').remove());
					index.masonry('reload');
					return false;
				});
			});
		});

		function sortProjects() {
			var arr = [];
			$(this).find('.date').each(function () {
				var index = $(this).attr("class").replace(/^.*index-(.*)/, "$1");
				$(this).removeAttr('style');
				arr[index - 1] = $(this);
			});
			arr = $.grep(arr, function (n) {
				return(n);
			});
			console.log(arr);
			for (i = 0; i < arr.length; i = i + 1) {
				var off = 0, def = 102, fin = def - off;
				if (i > 0) {
					off = arr[i].offset().top - arr[i - 1].offset().top;
					fin = Math.abs(def - off) + 14;
					if (off === 0) {
						fin = fin - 14;
					}
					if (off < def) {
						arr[i].css('margin-top', fin);
					}
				}
			}
		}

		$('.projects').each(function () {
			var projects = $(this);
			$(this).append('<div class="vline"></div>');
			projects.find('.block').each(function () {
				$(this).hover(function () {
					$('.close', this).show(200);
				}, function () {
					$('.close', this).hide(200);
				});
				$('.close a', this).click(function () {
					$(this).closest('.block').slideUp(100, function () {
						if ($(this).siblings('.block').length === 0) {
							$(this).closest('.date').remove();
						}
						$(this).remove();
						sortProjects.call(projects);
					});
					return false;
				});
			});
			sortProjects.call(this);
		});

		$('.top-nav').each(function () {
			$('.filter', this).click(function () {
				$('.block-filter').toggle();
				return false;
			});
			/*
			 $('.cart', this).click(function () {
			 $(this).toggleClass('cart-opened');
			 $('.block-cart').toggle();
			 return false;
			 });
			 */
		});

		$('.block-cart').each(function () {
			$('.block-alert', this).each(function () {
				var w = 0;
				$(this).siblings('.block').each(function () {
					w = w + $(this).outerWidth(true);
				});
				$(this).width(895 - w);
			});
		});

		$('.overlay').each(function () {
			var over = $(this);
			$(this).animate({
				opacity: 0.8
			}, 1);
			$(this).click(function () {
				over.hide();
				$('.popup').hide();
				return false;
			});
		});

		$('.overlay-white').each(function () {
			var over = $(this);
			$(this).animate({
				opacity: 0.8
			}, 1);
			$(this).click(function () {
				over.hide();
				$('.popup').hide();
				return false;
			});
		});

		$('.popup-show').each(function () {
			$(this).click(function () {
				var attr = $(this).attr("href").replace(/^.*#(.*)/, "$1");
				$('.popup-' + attr).show();
				$('.overlay').show();
				return false;
			});
		});

		$('.popup-white-show').each(function () {
			$(this).click(function () {
				var attr = $(this).attr("href").replace(/^.*#(.*)/, "$1");
				$('.popup-' + attr).show();
				$('.overlay-white').show();
				return false;
			});
		});

		$('.popup-close').click(function () {
			$('.overlay, .overlay-white').hide();
			$('.popup').hide();
			return false;
		});

		$('.toggle-market').click(function () {
			$(this).hide();
			$('.block-market').toggle();
			return false;
		});

		if ($.browser.msie && $.browser.version < 9) {
			$('.header, .footer').append('<div class="shadow"></div>');
			$('.block-filters, .nav-section').each(function () {
				$(this).append('<div class="before"></div><div class="after"></div>');
			});
			if ($.browser.msie && $.browser.version < 8) {
				$('.header').append('<div class="before"></div>');
			}
			if (window.PIE) {
				$('.nav li, .user-list .online, .social-small a, .block, input[type="text"], input[type="password"], textarea, .sbHolder, input[type="submit"], button, .submit, .user-list-2 .count, .projects .tags a, .projects .prices a, .projects .date .numbers, .block-user p.price').each(function () {
					PIE.attach(this);
				});
			}
		}
	};
	this.init = function () {
		this.initInterface();
	};
}

$(document).ready(function () {
	window.site = new Site();
	window.site.init();
});