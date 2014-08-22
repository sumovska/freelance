/*jslint nomen: true, regexp: true, unparam: true, sloppy: true, white: true */
/*global window, console, document, $, jQuery, PIE */

/* Tabs-nav */
    $('.tabs-nav').each(function () {
        var _self = this;
        $('a', this).click(function () {
            var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
            $(this).closest('li').addClass('active').siblings('li').removeClass('active');
            $(_self).siblings('.' + where).removeClass('tab-hidden').siblings('.tab-nav').addClass('tab-hidden');
            return false;
        });
    });

/* Tabs-catalog-nav */
    $('.tabs-catalog-nav').each(function () {
        var _self = this;
        $('a', this).click(function () {
            var where = $(this).prop('href').replace(/^.*#(.*)/, "$1");
            $(this).closest('li').addClass('active').siblings('li').removeClass('active');
            $(_self).siblings('.' + where).removeClass('tab-hidden').siblings('.tab-catalog-nav').addClass('tab-hidden');
            return false;
        });
    });

