$(window).load(function () {
	/* Tabs */
	$('.tabs').each(function () {
		var _self = this;
		$('a', this).click(function () {
			var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
			$(this).closest('li').addClass('active').siblings('li').removeClass('active');
			$(_self).siblings('.' + where).removeClass('tab-hidden').siblings('.tab').addClass('tab-hidden');
			return false;
		});
	});
});

