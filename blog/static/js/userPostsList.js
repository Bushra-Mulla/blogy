$(function () {
    e.preventDefault();
    // Menu Tabular
    var $menu_tabs = $('.menu__tabs li a');
    $menu_tabs.on('click', function (e) {
        e.preventDefault();
        $menu_tabs.removeClass('active');
        $(this).addClass('active');

        $('.menu__item').fadeOut(300);
        $(this.hash).delay(300).fadeIn();
    });

});
