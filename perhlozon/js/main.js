/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* On document ready */
$(document).ready(function () {

	/* Tabs */
	$('.block-explore').each(function () {
		$('.triggers li a', this).click(function () {
			$(this).closest('li').addClass('active').siblings('li.active').removeClass('active');
			$('.tab-' + $(this).attr("href").replace(/^.*#(.*)/, "$1")).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});

	/* Popup script */
	$('.fancybox-popup').fancybox({
		padding: 0,
		margin: 80,
		helpers: {
			media: {},
			overlay: {
				speedIn: 250,
				css: {
					'background': 'rgba(0, 0, 0, 0.8)'
				}
			}
		}
	});

});