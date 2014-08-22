$(window).load(function() {
	var carousel = $(".slider ul");
		carousel.carouFredSel({
			responsive: true,
			//width: '100%',
			//height: "auto",
			items: {
				visible: 1,
				//width: 940,
				height: "auto"
			},
			pagination: {
				container: ".pager"
			},
			scroll: {
				items: 1,
				duration: 700,
				timeoutDuration: 3000,
				pauseOnHover: false,
				fx: "fade"
			},
			auto: true,
			swipe: {
	        	onTouch: true
	    	}
	});
});

$(document).ready(function () {
    updateContainer();
    $(window).resize(function() {
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

jQuery(document).ready(function($) {

	$(".respons_img").responsiveImg({
		breakpoints: {
			"_small":780,
		},
		srcAttribute : "src",
		pathToPHP : "js",
		createNewImages : true,
		jpegQuality : 95,
		callback:false
	});

	if(!Modernizr.svg) {
	  $('img[src*="svg"]').attr('src', function() {  
	    return $(this).attr('src').replace('.svg', '.png');
	  });
	}

	$(".blog_list li img").width($(".date_item").width());
	/*$(".viewport_block").height($(".viewport_block img").height());*/

	$('.bar').each(function() {
     var bar = $(this);
     setTimeout( function() { bar.find('.progress').addClass('easing-long').css('width', bar.attr('data-percent') + '%' ); });
    }); 
	$('.bar').each(function() {
	     var bar = $(this);
	     bar.find('.progress').removeClass('easing-long').css('width', 0 ); 
	});

    $(".btn-vacansy").click(function() {
    	$(".top_vacansy").slideToggle("slow");
    	$(this).toggleClass("active"); return false;
    });
    $(".btn-lang").click(function() {
    	$(".top_lang").slideToggle("slow");
    	$(this).toggleClass("active"); return false;
    });
	
	$(".work_pairs").masonry({
		itemSelector: ".pair_box",
		"isFitWidth": true
	});

    /* Вешаем событие прокрутки на все якоря (#) на странице
    https://gist.github.com/Neolot/3964361 */
    $('a[href^="#"]').bind('click.smoothscroll', function (e) {
        e.preventDefault();
        var target = this.hash,
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop':$target.offset().top
        }, 900, 'swing', function () {
            window.location.hash = target;
        });
    });

});

(function($) {  
	$(function() {  
		$('.styled').styler();  
	})  
})(jQuery)

//  The function to change the class
var changeClass = function (r,className1,className2) {
    var regex = new RegExp("(?:^|\\s+)" + className1 + "(?:\\s+|$)");
    if( regex.test(r.className) ) {
        r.className = r.className.replace(regex,' '+className2+' ');
    }
    else{
        r.className = r.className.replace(new RegExp("(?:^|\\s+)" + className2 + "(?:\\s+|$)"),' '+className1+' ');
    }
    return r.className;
};  
//  Creating our button for smaller screens
var menuElements = document.getElementById('menu');
menuElements.insertAdjacentHTML('beforeBegin','<button type="button" id="menutoggle" class="navtoogle" aria-hidden="true"></button>');
//  Toggle the class on click to show / hide the menu
document.getElementById('menutoggle').onclick = function() {
    changeClass(this, 'navtoogle active', 'navtoogle');
}
// document click to hide the menu
// http://tympanus.net/codrops/2013/05/08/responsive-retina-ready-menu/comment-page-2/#comment-438918
document.onclick = function(e) {
    var mobileButton = document.getElementById('menutoggle'),
        buttonStyle =  mobileButton.currentStyle ? mobileButton.currentStyle.display : getComputedStyle(mobileButton, null).display;
 
    if(buttonStyle === 'block' && e.target !== mobileButton && new RegExp(' ' + 'active' + ' ').test(' ' + mobileButton.className + ' ')) {
        changeClass(mobileButton, 'navtoogle active', 'navtoogle');
    }
}

// Bind normal buttons
Ladda.bind( '.ladda-button', { timeout: 2000 } );

// Bind progress buttons and simulate loading progress
Ladda.bind( '.progress-ladda button', {
    callback: function( instance ) {
        var progress = 0;
        var interval = setInterval( function() {
            progress = Math.min( progress + Math.random() * 0.1, 1 );
            instance.setProgress( progress );

            if( progress === 1 ) {
                instance.stop();
                clearInterval( interval );
            }
        }, 200 );
    }
} );

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
        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
    });
});
jQuery(document).ready(function($) {
    var className = $(".name_block_wr").attr("class");
    $("#scrollUp").addClass(className);
});