/*jslint white: true, browser: true, onevar: false, undef: true, nomen: false, eqeqeq: true, plusplus: true, bitwise: true, regexp: false, newcap: true */
/*global window, console, document, $, jQuery */

function refreshSidebarWidgets() {
	$('.sidebarWidget').each(function () {
		var list = '', temp;
		if ($('input:checked', this).length > 0) {
			$('input:checked', this).each(function () {
				temp = $(this).siblings('span').text();
				list = list + temp + ', ';
			});
			list = list.substring(0, list.length - 2);
		}
		if ($('.slider-changed', this).length > 0) {
			$('.inputArea :input', this).each(function () {
				list = list + $(this).val() + '-';
			});
			list = list.substring(0, list.length - 1);
		}
		$('.h .list', this).remove();
		$('.h strong', this).after('<span class="list">' + list + '</span>');
	});
}

function refreshSidebar(current) {
	if (window.flex) {
		var total = $('.sidebar').outerHeight(true), win = +$(window).height() - 135, temp, widgets = $('.sidebarWidgetOpen');
		window.clearTimeout(window.int);
		if (total >= win) {
			temp = total;
			widgets.each(function () {
				if (this !== current) {
					temp = temp - ($(this).outerHeight(true) - $('.h', this).outerHeight(true));
				} else {
					temp = temp - ($(this).outerHeight(true));
				}
			});
			temp = temp - 1;
			if (temp < win) {
				widgets.each(function () {
					if (this !== current) {
						$('.h', this).click();
					}
				});
			}
		}
		window.int = window.setInterval(resize, 1000);
	}
}

function initForms() {
	function checkStrength(password) {
		var strength = 0;
		if (password.length < 6) {
			return 'Too short'
		}
		//if length is 8 characters or more, increase strength value
		if (password.length > 7) {
			strength = strength + 1;
		}
		//if password contains both lower and uppercase characters, increase strength value
		if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) {
			strength = strength + 1;
		}
		//if it has numbers and characters, increase strength value
		if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) {
			strength = strength + 1;
		}
		//if it has one special character, increase strength value
		if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) {
			strength = strength + 1;
		}
		//if it has two special characters, increase strength value
		if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) {
			strength = strength + 1;
		}
		if (strength < 2) {
			return 'Weak';
		} else if (strength === 2) {
			return 'Good';
		} else {
			return 'Strong';
		}
	}

	$('.form').each(function () {
		$(this).attr('autocomplete', 'off');
		$('.counter').each(function () {
			var target = $(this).prevAll('label:has(.counting)').find('.counting').eq(0), self = this;
			$('var', this).text(target.attr('maxlength'));
			target.on('keyup', function () {
				$('var', self).text(+target.attr('maxlength') - target.val().length);
			});
		});
		jQuery.validator.addMethod("requiredNew", function(value, element) {
			if($(element).val() === $(element).attr('title')) {
				$(element).val('')
			}
			return $(element).val().length > 0;
		}, "This field is required.");
		$(this).validate({
			errorElement: "em",
			ignoreTitle: true,
			errorPlacement: function(error, element) {
				var to = $(element).closest("label");
				if (to.nextAll().filter('.counter, .small').length > 0) {
					to = to.next('.counter, .small')
				}
				if (element.is('select')) {
					element.siblings('.sbHolder').addClass('sbHolderError');
				}
				if (element.closest('.select-leasing').length > 0) {
					to = element.closest('.select-leasing').nextAll('.select-leasing').eq(0);
				}
				element.siblings('.fake').css('z-index', 1).siblings(':input').css('z-index', 2);
				error.insertAfter(to);
			},
			success: function(label) {
				label.siblings('.selectbox').find('.sbHolderError').removeClass('sbHolderError');
			},
			groups: {
				glease: "cbuy clease"
			},
			rules: {
				ctitle: {
					requiredNew: true,
					maxlength: 75
				},
				cname: {
					requiredNew: true,
					minlength: 10
				},
				cdescription: {
					requiredNew: true
				},
				ccategory: {
					requiredNew: true
				},
				carea: {
					requiredNew: true
				},
				clocation: {
					requiredNew: true
				},
				ccountry: {
					requiredNew: true
				},
				cstate: {
					requiredNew: true
				},
				cemail: {
					requiredNew: true,
					email: true
				},
				cemailconfirm: {
					requiredNew: true,
					email: true,
					equalTo: "#cemail"
				},
				cpassword: {
					requiredNew: true
				},
				cpasswordconfirm: {
					requiredNew: true,
					equalTo: "#cpassword"
				},
				cphone: {
					requiredNew: true,
					digits: true
				},
				cwarr: {
					requiredNew: true,
					digits: true,
					maxlength: 2
				},
				ctype: {
					requiredNew: true
				},
				cownership: {
					requiredNew: true
				},
				csource: {
					requiredNew: true
				},
				cmake: {
					requiredNew: true
				},
				cmodel: {
					requiredNew: true
				},
				ctrans: {
					requiredNew: true
				},
				cyear: {
					requiredNew: true,
					digits: true,
					maxlength: 4,
					minlength: 4
				},
				ckm: {
					requiredNew: true
				},
				cduration: {
					requiredNew: true
				},
				cextra: {
					requiredNew: true
				},
				coverage: {
					requiredNew: true
				},
				clease: {
					required: true
				},
				cbuy: {
					required: true
				}
			},
			messages: {
				ctitle: {
					requiredNew: "Enter your ad title."
				},
				cname: {
					requiredNew: "Enter your name.",
					minlength: "Must be 10+ characters in length."
				},
				cdescription: {
					requiredNew: "Enter a description for your ad."
				},
				ccategory: {
					requiredNew: "Select a category."
				},
				carea: {
					requiredNew: "Select an area."
				},
				clocation: {
					requiredNew: "Enter a location."
				},
				ccountry: {
					requiredNew: "Select a country."
				},
				cstate: {
					requiredNew: "Select a state."
				},
				cemail: {
					requiredNew: "Enter your email address.",
					email: "Enter a valid email address."
				},
				cemailconfirm: {
					requiredNew: "Confirm your email address.",
					email: "Enter a valid email address.",
					equalTo: "Emails doesn't match."
				},
				cpassword: {
					requiredNew: "Enter a password."
				},
				cpasswordconfirm: {
					requiredNew: "Confirm password.",
					equalTo: "Passwords doesn't match."
				},
				cphone: {
					requiredNew: "Enter a phone number.",
					digits: "Enter a valid phone number."
				},
				cwarr: {
					requiredNew: "Enter warranty.",
					maxlength: "Please enter no more than 2 digits."
				},
				ctype: {
					requiredNew: "Select business or personal."
				},
				cownership: {
					requiredNew: "Select ownership."
				},
				csource: {
					requiredNew: "Select your primary source of sales."
				},
				cmake: {
					requiredNew: "Select make."
				},
				cmodel: {
					requiredNew: "Select model."
				},
				ctrans: {
					requiredNew: "Select trans."
				},
				cyear: {
					requiredNew: "Enter year."
				},
				ckm: {
					requiredNew: "Select KM range."
				},
				cduration: {
					requiredNew: "Select duration."
				},
				cextra: {
					requiredNew: "Select extra km."
				},
				coverage: {
					requiredNew: "Select overage $."
				},
				clease: {
					required: "Select at least one listing type and optionally enter the cost."
				},
				cbuy: {
					required: "Select at least one listing type and optionally enter the cost."
				}
			}
		});
	});

	/* Selectboxes */
	$('.selectbox select').each(function () {
		$(this).selectbox({
			onOpen: function (e) {
				$(e.input).css('z-index', 1000).closest('.row').css('z-index', 1000);
			},
			onClose: function (e) {
				$(e.input).css('z-index', 100).closest('.row').css('z-index', 0);
			},
			effect: "fade",
			speed: 100
		});
		if ($(this).is(':disabled')) {
			$(this).selectbox('disable');
		}
	});

	/* File */
	$('.file-input input:file').fileInput();

	/* Checkboxes */
	$('label.checkbox:not(".checkbox-inited")').each(function () {
		$(':checkbox', this).live('change',function () {
			$(this).trigger('redraw');
		}).live('redraw', function () {
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

	/* Radioboxes */
	$('label.radiobox:not(".radiobox-inited")').each(function () {
		var name = $(':radio', this).attr('name');
		$(':radio', this).live('change',function () {
			var self = this;
			$(this).trigger('redraw');
			$('.radiobox input:radio[name="' + name + '"]').each(function () {
				if (self !== this) {
					$(this).trigger('redraw');
				}
			});
		}).live('redraw', function () {
				if ($(this).is(':checked')) {
					$(this).closest('.radiobox').addClass('radiobox-checked');
				} else {
					$(this).closest('.radiobox').removeClass('radiobox-checked');
				}
			});
		if ($(':radio', this).is(':checked')) {
			$(this).addClass('radiobox-checked');
		}
		$(this).addClass('radiobox-inited');
	});

	$('.loginform').each(function () {
		$('.login-user-new :radio').change(function () {
			var pass = $('.login-user-password :password'), text = $('.login-user-password :text');
			if ($(this).val() === 'false') {
				text.show();
				if (window.PIE) {
					text.each(function () {
						PIE.attach(this);
					});
					pass.each(function () {
						PIE.detach(this);
					});
				}
				pass.attr('disabled', 'disabled').hide();
			} else {
				if (window.PIE) {
					text.each(function () {
						PIE.detach(this);
					});
				}
				text.hide();
				pass.show().removeAttr('disabled').focus();
				if (window.PIE) {
					pass.each(function () {
						PIE.attach(this);
					});
				}
			}
		});
	});
	$('.select-leasing').each(function () {
		var self = this;
		$(':checkbox', this).change(function () {
			var text = $('input:text', self);
			if ($(this).is(':checked')) {
				if (window.PIE) {
					text.each(function () {
						PIE.detach(this);
					});
				}
				text.removeAttr('disabled');
				if (window.PIE) {
					text.each(function () {
						PIE.attach(this);
					});
				}
			} else {
				if (window.PIE) {
					text.each(function () {
						PIE.detach(this);
					});
				}
				text.attr('disabled', 'disabled');
				if (window.PIE) {
					text.each(function () {
						PIE.attach(this);
					});
				}
			}
		});
		if ($(':checkbox', this).is(':checked')) {
			$('input:text', self).removeAttr('disabled');
		} else {
			$('input:text', self).attr('disabled', 'disabled');
		}
	});
	$('.field-password').each(function () {
		var self = this;
		$(':text', this).on('focus', function () {
			$(this).css('z-index', 1);
			$(this).siblings(':password').css('z-index', 2).focus();
		});
		$(':password', this).on('keyup', function () {
			var v = $(this).val(), c = $('.strength i', self);
			if (v.length > 0) {
				v = checkStrength(v);
				c.text(v);
				if (v === 'Too short') {
					c.addClass('strength-1');
				} else if (v === 'Weak') {
					c.addClass('strength-2');
				} else if (v === 'Good') {
					c.addClass('strength-3');
				} else if (v === 'Strong') {
					c.addClass('strength-4');
				}
			} else {
				c.text('').removeAttr('class');
			}
		});
	});
}

$(document).ready(function () {
	/* Sidebar widget clicks */
	$('.sidebar .sidebarWidget:last-child').addClass('sidebarWidgetLast');
	$('.sidebarWidget').each(function () {
		var self = this, box = $('.sidebarBox', self), scroll = $('.scroll', box);
		$('.h', this).click(function () {
			var current = $(this).closest('.sidebarWidget'), box = $('.sidebarBox', current), scroll = $('.scroll', box);
			if (current.hasClass('sidebarWidgetOpen')) {
				box.slideUp(300, function () {
					current.removeClass('sidebarWidgetOpen');
					if (scroll.data('jsp') !== undefined) {
						scroll.data('jsp').destroy();
					}
				});
			} else {
				box.slideDown(300, function () {
					current.addClass('sidebarWidgetOpen');
					refreshSidebar(self);
					if ($('ul', box).outerHeight() > 119) {
						scroll.bind('jsp-initialised', function () {
							if ($.browser.msie && $.browser.version < 9 && $.browser.version > 7) {
								if (window.PIE) {
									$('.jspDrag').each(function () {
										PIE.attach(this);
									});
								}
							}
						});
						scroll.jScrollPane({
							contentWidth: 176,
							verticalGutter: 0,
							horizontalGutter: 0,
							autoReinitialise: true
						});
					}
				});
			}
			refreshSidebarWidgets();
			return false;
		});
		if ($.browser.msie && $.browser.version < 9) {
			$('.h', this).append('<span class="after"></span>');
		}
		if ($(self).hasClass('sidebarWidgetOpen')) {
			if ($('ul', box).outerHeight() > 119) {
				scroll.bind('jsp-initialised', function () {
					if ($.browser.msie && $.browser.version < 9 && $.browser.version > 7) {
						if (window.PIE) {
							$('.jspDrag').each(function () {
								PIE.attach(this);
							});
						}
					}
				});
				scroll.jScrollPane({
					contentWidth: 176,
					verticalGutter: 0,
					horizontalGutter: 0,
					autoReinitialise: true
				});
			}
		}
	});

	$(function () {
		/*PriceRange slider*/
		var priceRange = $("#PriceRange");
		priceRange.slider({
			range: true,
			min: 0,
			max: 1000,
			values: [0, 1000],
			slide: function (event, ui) {
				$("#pricemin").val("$" + ui.values[0]);
				$("#pricemax").val("$" + ui.values[1]);
				$(this).addClass('slider-changed');
			}
		});
		$("#pricemin").val("$" + priceRange.slider("values", 0));
		$("#pricemax").val("$" + priceRange.slider("values", 1));

		/*Year slider*/
		var yearRange = $("#year");
		yearRange.slider({
			range: true,
			min: 1901,
			max: 2012,
			values: [1901, 2012],
			slide: function (event, ui) {
				$("#yearmin").val(+ui.values[0]);
				$("#yearmax").val(+ui.values[1]);
				$(this).addClass('slider-changed');
			}
		});
		$("#yearmin").val(+yearRange.slider("values", 0));
		$("#yearmax").val(+yearRange.slider("values", 1));

		/*Traier slider*/
		var trailerLength = $("#TrailerLength");
		trailerLength.slider({
			range: true,
			min: 1.1,
			max: 9.9,
			values: [1.1, 9.9],
			slide: function (event, ui) {
				$("#minvalue").val(+ui.values[0]);
				$("#maxvalue").val(+ui.values[1]);
				$(this).addClass('slider-changed');
			}
		});
		$("#minvalue").val(+trailerLength.slider("values", 0));
		$("#maxvalue").val(+trailerLength.slider("values", 1));
	});

	if ($.browser.msie && $.browser.version < 9) {
		$('.gallery .pic img').each(function () {
			$(this).click(function () {
				$(this).closest('.checkbox').find(':checkbox').trigger('click').trigger('change');
			});
		});
	}

	refreshSidebarWidgets();
	initForms();
});

function picHover(num) {
	var self = this, delay = 250;
	window.clearTimeout(window.picTimeout);
	$(this).find('.pic').stop();
	if (num !== undefined) {
		delay = 0;
	}
	$(this).find('.pic-active').animate({
		opacity: 0
	}, delay, function () {
		var next, area = $(this).closest('.main');
		if (num === undefined) {
			window.picTimeout = setTimeout(function () {
				picHover.call(self);
			}, 2000);
			if ($(this).next('.pic').length > 0) {
				next = $(this).next('.pic');
			} else {
				next = area.find('.pic').eq(0);
			}
		} else {
			next = area.find('.pic').eq(num);
		}
		$(this).removeClass('pic-active');
		next.addClass('pic-active');
		$('.heading .photos', area).text((next.index() + 1) + '/' + ($(this).siblings('.pic').length + 1));
		if ($.browser.msie && $.browser.version < 8) {
			next.css('display', 'inline-block');
		} else {
			next.css('display', 'table');
		}
		next.animate({
			opacity: 1
		}, delay);
	});
}

function resize() {
	var sidebar = $('.sidebar'), winH = +$(window).height() - 115, temp, body = $('body');
	/* Resizing fixed elements */
	if ($(window).width() <= 1100) {
		window.area.width($('.rightcolumn').width());
		if ($.browser.msie && $.browser.version < 9) {
			body.addClass('media-ie');
		}
	} else {
		window.area.width('auto');
		if ($.browser.msie && $.browser.version < 9) {
			body.removeClass('media-ie');
		}
	}
	/* Initializing scrollbar */
	temp = $('form', sidebar).outerHeight(true) + 6;
	if (temp >= winH) {
		if (sidebar.data('jsp') != undefined) {
			$('.jspContainer', sidebar).height(winH);
			sidebar.height(winH).data('jsp').reinitialise();
		} else {
			sidebar.height(winH);
			sidebar.bind('jsp-initialised', function (event, isScrollable) {
				if ($.browser.msie && $.browser.version < 9 && $.browser.version > 7) {
					if (window.PIE) {
						$('.jspDrag').each(function () {
							PIE.attach(this);
						});
					}
				}
			});
			sidebar.jScrollPane({
				contentWidth: 212,
				verticalGutter: 0,
				horizontalGutter: 0,
				autoReinitialise: true
			});
		}
	} else {
		if (sidebar.data('jsp') != undefined) {
			sidebar.data('jsp').destroy();
		} else {
			sidebar.height('auto');
		}
	}
	/* Initializing catalog width */
	var w;
	$('.catalog').each(function () {
		w = Math.floor($(this).outerWidth() / 239);
		if (w !== window.cols) {
			$('.item', this).width(100 / w + '%').removeClass('last');
			$('.item:nth-child(' + w + 'n)', this).addClass('last');
		}
	});
	window.cols = w;
}

$(window).load(function () {
	/* Flexible page flag */
	window.flex = $('.wrapper').hasClass('wrapper-flex');

	window.area = $('.area');
	/* Cols in the catalog */
	window.cols = 3;
	$(window).resize();

	/* Last item in the row (catalog) */
	$('.catalog .item:nth-child(' + window.cols + 'n)').addClass('last');
	/* Initializing catalog hovers */
	$('.catalog .item').each(function () {
		var se = $(this);
		$('.main', this).each(function () {
			var self = this;
			$('.pic:not(.pic-active)', this).animate({
				opacity: 0
			}, 0);
			$(this).hover(function () {
				window.picTimeout = setTimeout(function () {
					picHover.call(self);
				}, 750);
			}, function () {
				picHover.call(self, 0);
			});
		});
		$(this).hover(function () {
			se.addClass('item-hover');
		}, function () {
			se.removeClass('item-hover');
			picHover.call($('.main', self), 0);
		});
	});

	/* Toggle catalog visible after page load */
	$('.contentArea').css('visibility', 'visible');

	/* Fix to avoid 'jumps' on bolded hover in nvaigation */
	$('.navigation li, .region li').each(function () {
		$(this).width($(this).width());
	});
	/* IE fixes */
	if ($.browser.msie && $.browser.version < 9) {
		if ($.browser.version < 8) {
			$('.region, .breadcrumbs, .footer').append('<i class="after"></i>');
			$('.catalog .item .pic a').prepend('<span></span>');
		}
		if (window.PIE) {
			$('.wrapper, input[type="text"], input[type="password"], textarea, .block, .sidebar .h, .catalog .main, .catalog .heading, .catalog .location, .row-grey, .form .ed, .pager > li, .manage-ads .pic').each(function () {
				PIE.attach(this);
			});
		}
	}
});

$.validator.setDefaults({ ignore: ':disabled, .ignore' });

$(window).resize(function () {
	/* Resize function only in flexible pages */
	if (window.flex) {
		resize();
	}
});
