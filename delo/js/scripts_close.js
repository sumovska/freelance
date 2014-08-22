jQuery(document).ready(function($) {

    if(!Modernizr.svg) {
      $('img[src$="svg"]').attr('src', function() {  
        return $(this).attr('src').replace('.svg', '.png');
      });
    }

    $(".btn-vacansy").click(function() {
    	$(".top_vacansy").slideToggle("slow");
    	$(this).toggleClass("active"); return false;
    });
    $(".btn-lang").click(function() {
    	$(".top_lang").slideToggle("slow");
    	$(this).toggleClass("active"); return false;
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