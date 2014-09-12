$(window).load(function () {
	$(".post_slider ul").each(function () {
		$(this).carouFredSel({
			responsive: true,
			width: '100%',
			height: "variable",
			items: {
				visible: 1,
				//width: 940,
				height: "variable"
			},
			pagination: {
				container: ".pager"
			},
			scroll: {
				items: 1,
				duration: 700,
				timeoutDuration: 3000,
				pauseOnHover: false
			},
			auto: true,
			swipe: {
				onTouch: true
			}
		});
	});
});

$(window).scroll(function () {
	var tabs = $('.tabs-fixed'), space = $('.tabs-space');
	if (!tabs.hasClass('tabs-fixed-on') && ($(window).scrollTop() > (tabs.offset().top))) {
		space.height(tabs.height()).show();
		tabs.width(tabs.width()).height(tabs.height()).addClass('tabs-fixed-on');
	}
	if (tabs.hasClass('tabs-fixed-on') && ($(window).scrollTop() < (space.offset().top))) {
		space.height('auto').hide();
		tabs.width('auto').height('auto').removeClass('tabs-fixed-on');
	}
});
$(window).resize(function () {
	$('tabs-fixed-on').width($('.content').width());
});

$(document).ready(function () {
	updateContainer();
	$(window).resize(function () {
		updateContainer();
	});
});
function updateContainer() {
	var $containerWidth = $(window).width();
	if ($containerWidth <= 767) {
		var cw = $('.pair_box').width();
		$('.pair_box').css({
			'height': cw + 'px'
		});
	}
}

jQuery(document).ready(function ($) {

	$('.radiobox-group').each(function () {
		$('.radiobox:not(".radiobox-inited")', this).each(function () {
			var self = $(this);
			$(':radio', this).live('change',function () {
				$(this).trigger('redraw');
			}).live('redraw', function () {
					$(this).closest('.radiobox').addClass('radiobox-checked').siblings('.radiobox-checked').removeClass('radiobox-checked');
				});
			if ($(':radio', this).is(':checked')) {
				$(this).closest('.radiobox').addClass('radiobox-checked').siblings('.radiobox-checked').removeClass('radiobox-checked');
			}
			self.addClass('radiobox-inited');
		});
	});

	$('.default-slider', this).each(function () {
		var _self = $(this);
		var item = $('.item', this).noUiSlider({
			start: [ 2000, 8000 ],
			step: 1000,
			behaviour: 'drag',
			connect: true,
			range: {
				'min': 0,
				'max': 15000
			},
			format: wNumb({
				decimals: 0,
				postfix: '&nbsp;Р',
				encoder: function (value) {
					return Math.round(value);
				}
			})
		});
		item.Link('lower').to('-inline-<div class="tp"></div>', function (value) {
			$(this).html(value);
		});
		item.Link('upper').to('-inline-<div class="tp"></div>', function (value) {
			$(this).html(value);
		});
	});

	$(".scroll_top").click(function () {
		$("html, body").animate({ scrollTop: 0 }, 800);
		return false;
	});

	$(".respons_img").responsiveImg({
		breakpoints: {
			"_small": 780
		},
		srcAttribute: "src",
		pathToPHP: "js",
		createNewImages: true,
		jpegQuality: 95,
		callback: false
	});

	if (!Modernizr.svg) {
		$('img[src*="svg"]').attr('src', function () {
			return $(this).attr('src').replace('.svg', '.png');
		});
	}

	$(".work_pairs").masonry({
		itemSelector: ".pair_box",
		"isFitWidth": true
	});

	$('.bar').each(function () {
		var bar = $(this);
		setTimeout(function () {
			bar.find('.progress').addClass('easing-long').css('width', bar.attr('data-percent') + '%');
		});
	});
	$('.bar').each(function () {
		var bar = $(this);
		bar.find('.progress').removeClass('easing-long').css('width', 0);
	});

	$(".btn-vacansy").click(function () {
		$(".top_vacansy").slideToggle("slow");
		$(this).toggleClass("active");
		return false;
	});
	$(".btn-lang").click(function () {
		$(".top_lang").slideToggle("slow");
		$(this).toggleClass("active");
		return false;
	});

	$(".blog_list li img").width($(".date_item").width());
	/*$(".viewport_block").height($(".viewport_block img").height());*/
	/*$(".timeline-img").height($(".timeline-block").height());*/

	$(".fancybox").fancybox({
		fitToView: true,
		autoResize: true,
		autoCenter: true,
		scrolling: 'no',
		width: '95%',
		maxWidth: '95%',
		autoSize: true,
		closeClick: false,
		closeBtn: true,
		padding: 0,
		margin: 0,
		wrapCSS: 'fancymod',
		helpers: {
			title: {
				type: 'inside',
				position: 'top'
			},
			overlay: {
				locked: false
			}
		},
		tpl: {
			closeBtn: '<a title="Close" class="fancybox-item fancybox-close close_modal" href="javascript:;">&times;</a>'
		}
	});

	$(".fancybox-thumb").fancybox({
		fitToView: false,
		padding: [50, 75, 50, 200],
		margin: 20,
		topRatio: 0,
		wrapCSS: 'fancybox-gallery',
		prevEffect: 'none',
		nextEffect: 'none',
		helpers: {
			media: {},
			title: {
				type: null
			},
			thumbs: {
				width: 60,
				height: 40,
				position: 'top'
			},
			overlay: {
				css: {
					'background': 'rgba(0, 0, 0, 0.9)'
				}
			}
		},
		afterShow: function () {
			var fancy = $('body > #fancybox-thumbs');

			function checkDOMChange() {
				fancy = $('body > #fancybox-thumbs');
				if (fancy.length > 0) {
					fire();
				} else {
					setTimeout(checkDOMChange, 100);
				}
			}

			function fire() {
				var current, vid;
				fancy = $('body > #fancybox-thumbs');
				current = fancy.clone().prependTo('.fancybox-gallery .fancybox-skin');
				current.removeProp('id').addClass('fancybox-thumbs').wrap('<div class="fancybox-sidebar"></div>');
				$('li', current).eq(fancyCurrent).addClass('active').siblings('li.active').removeClass('active');
				$("img[src*='video.jpg']", current).closest('li').addClass('video');
				if ($('.video', current).length > 0) {
					vid = current.clone().insertAfter(current);
					vid.addClass('fancybox-video').find('ul').empty().append($('.video', current).clone());
					$('.video', current).remove();
				}
			}

			if (fancy.length > 0) {
				fire();
			} else {
				setTimeout(checkDOMChange, 100);
			}
		},
		afterLoad: function (current) {
			window.fancyCurrent = current.index;
			$('html, body').animate({
				scrollTop: 0
			}, 300, 'swing');
		}
	});

	$(".vacancy_block .pure-g").wrap("<div class='vacancy_wrap' />");

	/* Вешаем событие прокрутки на все якоря (#) на странице
	 https://gist.github.com/Neolot/3964361 */
	$('a[href^="#"]').bind('click.smoothscroll', function (e) {
		e.preventDefault();
		var target = this.hash,
			$target = $(target);
		$('html, body').stop().animate({
			'scrollTop': $target.offset().top
		}, 900, 'swing', function () {
			window.location.hash = target;
		});
	});

	$('.star_raty').raty({
		number: 5,
		readOnly: true,
		path: 'img',
		starOff: 'star-off.png',
		starOn: 'star-on.png',
		size: 26,
		score: function () {
			return $(this).attr('data-score');
		}
	});

	/*$('.pure-form .form_checkout-payment_method .pure-radio').click(function(e) {
	 e.preventDefault();
	 $(this).toggleClass('checked')
	 });*/

	$(".pinned").pin({
		containerSelector: ".container"
		//minWidth: 940
	});

});

(function ($) {
	$(function () {
		$('.styled').styler({
			browseReadText: 'Файл в формате doc, docx. pdf'
		});
	})
})(jQuery)

//  The function to change the class
var changeClass = function (r, className1, className2) {
	var regex = new RegExp("(?:^|\\s+)" + className1 + "(?:\\s+|$)");
	if (regex.test(r.className)) {
		r.className = r.className.replace(regex, ' ' + className2 + ' ');
	}
	else {
		r.className = r.className.replace(new RegExp("(?:^|\\s+)" + className2 + "(?:\\s+|$)"), ' ' + className1 + ' ');
	}
	return r.className;
};
//  Creating our button for smaller screens
var menuElements = document.getElementById('menu');
menuElements.insertAdjacentHTML('beforeBegin', '<button type="button" id="menutoggle" class="navtoogle" aria-hidden="true"></button>');
//  Toggle the class on click to show / hide the menu
document.getElementById('menutoggle').onclick = function () {
	changeClass(this, 'navtoogle active', 'navtoogle');
}
// document click to hide the menu
// http://tympanus.net/codrops/2013/05/08/responsive-retina-ready-menu/comment-page-2/#comment-438918
document.onclick = function (e) {
	var mobileButton = document.getElementById('menutoggle'),
		buttonStyle = mobileButton.currentStyle ? mobileButton.currentStyle.display : getComputedStyle(mobileButton, null).display;

	if (buttonStyle === 'block' && e.target !== mobileButton && new RegExp(' ' + 'active' + ' ').test(' ' + mobileButton.className + ' ')) {
		changeClass(mobileButton, 'navtoogle active', 'navtoogle');
	}
}

// Bind normal buttons
Ladda.bind('.ladda-button', { timeout: 2000 });

// Bind progress buttons and simulate loading progress
Ladda.bind('.progress-ladda button', {
	callback: function (instance) {
		var progress = 0;
		var interval = setInterval(function () {
			progress = Math.min(progress + Math.random() * 0.1, 1);
			instance.setProgress(progress);

			if (progress === 1) {
				instance.stop();
				clearInterval(interval);
			}
		}, 200);
	}
});

// You can control loading explicitly using the JavaScript API
// as outlined below:

// var l = Ladda.create( document.querySelector( 'button' ) );
// l.start();
// l.stop();
// l.toggle();
// l.isLoading();
// l.setProgress( 0-1 );

$(function () {
	$.scrollUp({
		scrollName: 'scrollUp', // Element ID
		topDistance: '1200', // Distance from top before showing element (px)
		topSpeed: 300, // Speed back to top (ms)
		animation: 'fade', // Fade, slide, none
		animationInSpeed: 200, // Animation in speed (ms)
		animationOutSpeed: 200, // Animation out speed (ms)
		scrollText: "<i class='fa fa-chevron-up'></i>", // Text for element
		activeOverlay: false // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	});
});
jQuery(document).ready(function ($) {
	var className = $(".page_second").attr("class");
	$("#scrollUp").addClass(className);
});

/*
 * Graph
 */
$(function () {
	if (typeof Highcharts !== 'undefined') {
		Highcharts.setOptions({
			lang: {
				months: [ "Январь" , "Февраль" , "Март" , "Апрель" , "Май" , "Июнь" , "Июль" , "Август" , "Сентябрь" , "Октябрь" , "Ноябрь" , "Декабрь"],
				shortMonths: [ "Январь" , "Февраль" , "Март" , "Апрель" , "Май" , "Июнь" , "Июль" , "Август" , "Сентябрь" , "Октябрь" , "Ноябрь" , "Декабрь"]
			},
			plotOptions: {
				series: {
					fillOpacity: 0.5,
					lineWidth: 1
				}
			},
			credits: {
				enabled: false
			},
			xAxis: {
				labels: {
					style: {
						color: '#bcbcbc',
						fontSize: '10px'
					},
					y: 20
				}
			},
			yAxis: {
				labels: {
					style: {
						color: '#bcbcbc',
						fontSize: '10px'
					}
				},
				gridLineColor: '#ebebeb'
			}
		});

		var chart1 = new Highcharts.Chart({
			chart: {
				renderTo: 'container',
				type: 'line'
			},
			title: {
				text: 'text title',
				style: {
					display: 'none'
				}
			},
			/*subtitle: {
			 text: 'Irregular time data in Highcharts JS'
			 },*/
			legend: {
				enabled: false
			},
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: { // don't display the dummy year
					month: '%b \'%Y'
				}
			},
			yAxis: {
				title: {
					enabled: false
				},
				min: 0
			},
			tooltip: {
				formatter: function () {
					return '<b>' + this.series.name + '</b><br/>' +
						Highcharts.dateFormat('%e. %b. %Y', this.x) + ': ' + this.y + ' m';
				}
			},

			series: [
				{
					// name: 'Winter 2007-2008',
					data: [
						[Date.UTC(2013, 9, 27), 0   ],
						[Date.UTC(2013, 10, 10), 3 ],
						[Date.UTC(2013, 11, 18), 5 ],
						[Date.UTC(2013, 12, 2), 7 ],
						[Date.UTC(2014, 1, 5), 9 ]
					],
					color: '#37c0c8'
				},
				{
					// name: 'Winter 2008-2009',
					data: [
						[Date.UTC(2013, 9, 18), 0   ],
						[Date.UTC(2013, 10, 26), 2 ],
						[Date.UTC(2013, 11, 1), 4],
						[Date.UTC(2013, 12, 11), 7],
						[Date.UTC(2014, 1, 20), 8]
					],
					color: '#376ebc'
				}
			]
		});

		var chart2 = new Highcharts.Chart({
			chart: {
				renderTo: 'container2',
				type: 'area'
			},
			title: {
				text: 'text title',
				style: {
					display: 'none'
				}
			},
			/*subtitle: {
			 text: 'Irregular time data in Highcharts JS'
			 },*/
			legend: {
				enabled: false
			},
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: { // don't display the dummy year
					month: '%e. %b'
				}
			},
			yAxis: {
				title: {
					enabled: false
				},
				min: 0
			},
			tooltip: {
				formatter: function () {
					return '<b>' + this.series.name + '</b><br/>' +
						Highcharts.dateFormat('%e. %b. %Y', this.x) + ': ' + this.y + ' m';
				}
			},

			series: [
				{
					// name: 'Winter 2007-2008',
					data: [
						[Date.UTC(2013, 9, 27), 0   ],
						[Date.UTC(2013, 10, 10), 3 ],
						[Date.UTC(2013, 11, 18), 5 ],
						[Date.UTC(2013, 12, 2), 7 ],
						[Date.UTC(2014, 1, 5), 9 ]
					],
					color: '#376ebc'
				}
			]
		});

		var chart3 = new Highcharts.Chart({
			chart: {
				renderTo: 'container3',
				type: 'line'
			},
			title: {
				text: 'text title',
				style: {
					display: 'none'
				}
			},
			/*subtitle: {
			 text: 'Irregular time data in Highcharts JS'
			 },*/
			legend: {
				enabled: false
			},
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: { // don't display the dummy year
					month: '%e. %b'
				}
			},
			yAxis: {
				title: {
					enabled: false
				},
				labels: {
					format: '+{value}%'
				},
				min: 0
			},
			tooltip: {
				formatter: function () {
					return '<b>' + this.series.name + '</b><br/>' +
						Highcharts.dateFormat('%e. %b. %Y', this.x) + ': ' + this.y + ' m';
				}
			},

			series: [
				{
					// name: 'Winter 2007-2008',
					data: [
						[Date.UTC(2013, 9, 27), 0   ],
						[Date.UTC(2013, 10, 10), 100 ],
						[Date.UTC(2013, 11, 18), 150 ],
						[Date.UTC(2013, 12, 2), 200 ],
						[Date.UTC(2014, 1, 5), 300 ]
					],
					color: '#37c0c8'
				},
				{
					// name: 'Winter 2008-2009',
					data: [
						[Date.UTC(2013, 9, 18), 50   ],
						[Date.UTC(2013, 10, 26), 140 ],
						[Date.UTC(2013, 11, 1), 150],
						[Date.UTC(2013, 12, 11), 220],
						[Date.UTC(2014, 1, 20), 340]
					],
					color: '#376ebc'
				}
			]
		});
		var chart4 = new Highcharts.Chart({
			chart: {
				renderTo: 'container4',
				type: 'line'
			},
			title: {
				text: 'text title',
				style: {
					display: 'none'
				}
			},
			/*subtitle: {
			 text: 'Irregular time data in Highcharts JS'
			 },*/
			legend: {
				enabled: false
			},
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: { // don't display the dummy year
					month: '%b \'%Y'
				}
			},
			yAxis: {
				title: {
					enabled: false
				},
				min: 0
			},
			tooltip: {
				formatter: function () {
					return '<b>' + this.series.name + '</b><br/>' +
						Highcharts.dateFormat('%e. %b. %Y', this.x) + ': ' + this.y + ' m';
				}
			},

			series: [
				{
					// name: 'Winter 2007-2008',
					data: [
						[Date.UTC(2013, 9, 27), 0   ],
						[Date.UTC(2013, 10, 10), 3 ],
						[Date.UTC(2013, 11, 18), 5 ],
						[Date.UTC(2013, 12, 2), 7 ],
						[Date.UTC(2014, 1, 5), 9 ]
					],
					color: '#37c0c8'
				},
				{
					// name: 'Winter 2008-2009',
					data: [
						[Date.UTC(2013, 9, 18), 0   ],
						[Date.UTC(2013, 10, 26), 2 ],
						[Date.UTC(2013, 11, 1), 4],
						[Date.UTC(2013, 12, 11), 7],
						[Date.UTC(2014, 1, 20), 8]
					],
					color: '#376ebc'
				}
			]
		});
		var chart5 = new Highcharts.Chart({
			chart: {
				renderTo: 'container5',
				type: 'line'
			},
			title: {
				text: 'text title',
				style: {
					display: 'none'
				}
			},
			/*subtitle: {
			 text: 'Irregular time data in Highcharts JS'
			 },*/
			legend: {
				enabled: false
			},
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: { // don't display the dummy year
					month: '%b \'%Y'
				}
			},
			yAxis: {
				title: {
					enabled: false
				},
				min: 0
			},
			tooltip: {
				formatter: function () {
					return '<b>' + this.series.name + '</b><br/>' +
						Highcharts.dateFormat('%e. %b. %Y', this.x) + ': ' + this.y + ' m';
				}
			},

			series: [
				{
					// name: 'Winter 2007-2008',
					data: [
						[Date.UTC(2013, 9, 27), 0   ],
						[Date.UTC(2013, 10, 10), 3 ],
						[Date.UTC(2013, 11, 18), 5 ],
						[Date.UTC(2013, 12, 2), 7 ],
						[Date.UTC(2014, 1, 5), 9 ]
					],
					color: '#37c0c8'
				},
				{
					// name: 'Winter 2008-2009',
					data: [
						[Date.UTC(2013, 9, 18), 0   ],
						[Date.UTC(2013, 10, 26), 2 ],
						[Date.UTC(2013, 11, 1), 4],
						[Date.UTC(2013, 12, 11), 7],
						[Date.UTC(2014, 1, 20), 8]
					],
					color: '#376ebc'
				}
			]
		});
		var chart6 = new Highcharts.Chart({
			chart: {
				renderTo: 'container6',
				type: 'line'
			},
			title: {
				text: 'text title',
				style: {
					display: 'none'
				}
			},
			/*subtitle: {
			 text: 'Irregular time data in Highcharts JS'
			 },*/
			legend: {
				enabled: false
			},
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: { // don't display the dummy year
					month: '%b \'%Y'
				}
			},
			yAxis: {
				title: {
					enabled: false
				},
				min: 0
			},
			tooltip: {
				formatter: function () {
					return '<b>' + this.series.name + '</b><br/>' +
						Highcharts.dateFormat('%e. %b. %Y', this.x) + ': ' + this.y + ' m';
				}
			},

			series: [
				{
					// name: 'Winter 2007-2008',
					data: [
						[Date.UTC(2013, 9, 27), 0   ],
						[Date.UTC(2013, 10, 10), 3 ],
						[Date.UTC(2013, 11, 18), 5 ],
						[Date.UTC(2013, 12, 2), 7 ],
						[Date.UTC(2014, 1, 5), 9 ]
					],
					color: '#37c0c8'
				},
				{
					// name: 'Winter 2008-2009',
					data: [
						[Date.UTC(2013, 9, 18), 0   ],
						[Date.UTC(2013, 10, 26), 2 ],
						[Date.UTC(2013, 11, 1), 4],
						[Date.UTC(2013, 12, 11), 7],
						[Date.UTC(2014, 1, 20), 8]
					],
					color: '#376ebc'
				}
			]
		});
		var chart7 = new Highcharts.Chart({
			chart: {
				renderTo: 'container7',
				type: 'line'
			},
			title: {
				text: 'text title',
				style: {
					display: 'none'
				}
			},
			/*subtitle: {
			 text: 'Irregular time data in Highcharts JS'
			 },*/
			legend: {
				enabled: false
			},
			xAxis: {
				type: 'datetime',
				dateTimeLabelFormats: { // don't display the dummy year
					month: '%e. %b'
				}
			},
			yAxis: {
				title: {
					enabled: false
				},
				labels: {
					format: '+{value}%'
				},
				min: 0
			},
			tooltip: {
				formatter: function () {
					return '<b>' + this.series.name + '</b><br/>' +
						Highcharts.dateFormat('%e. %b. %Y', this.x) + ': ' + this.y + ' m';
				}
			},

			series: [
				{
					// name: 'Winter 2007-2008',
					data: [
						[Date.UTC(2013, 9, 27), 0   ],
						[Date.UTC(2013, 10, 10), 100 ],
						[Date.UTC(2013, 11, 18), 150 ],
						[Date.UTC(2013, 12, 2), 200 ],
						[Date.UTC(2014, 1, 5), 300 ]
					],
					color: '#37c0c8'
				},
				{
					// name: 'Winter 2008-2009',
					data: [
						[Date.UTC(2013, 9, 18), 50   ],
						[Date.UTC(2013, 10, 26), 140 ],
						[Date.UTC(2013, 11, 1), 150],
						[Date.UTC(2013, 12, 11), 220],
						[Date.UTC(2014, 1, 20), 340]
					],
					color: '#376ebc'
				}
			]
		});
	}
});
