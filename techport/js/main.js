/*jslint white: true, browser: true, onevar: false, undef: true, nomen: false, eqeqeq: true, plusplus: true, bitwise: true, regexp: false, newcap: true */
/*global window, console, document, $, jQuery, PIE */

function UI() {
	var self = this;

	this.init = function () {
		initPageScroll();
		initGallery();
		initTabs();
		initFlash();
	};

	function initTabs() {
		$(".description .tabs").superSimpleTabs();
	}

	function initPageScroll() {
		$(".tech-nav a").click(function (event) {
			var where = '#' + $(this).prop("href").replace(/^.*#(.*)/, "$1");
			$.scrollTo(where, 500, {
				easing: 'swing'
			});
			return false;
		});
	}

	function initGallery() {
		$('.info-gallery').each(function () {
			var _self = this;
			$('.thumbnail a', this).click(function () {
				var id = $(this).prop("href").replace(/^.*#(.*)/, "$1") - 1;
				$(this).addClass('active').siblings('a').removeClass('active');
				$('.big img', _self).eq(id).show().siblings('img').hide();
				return false;
			});
		});
	}

	function initFlash() {
		window.flashvars = {};
		window.params = {
			menu: "false",
			scale: "noScale",
			allowFullscreen: "true",
			allowScriptAccess: "always",
			bgcolor: "",
			wmode: "direct" // can cause issues with FP settings & webcam
		};
		window.attributes = {
			id: "flash"
		};
		swfobject.embedSWF(
			"./flash/header.swf",
			"flash", "988", "500", "10.0.0",
			"./flash/expressInstall.swf",
			flashvars, params, attributes);
	}
}

$(document).ready(function () {
	window.UI = new UI();
	window.UI.init();
});