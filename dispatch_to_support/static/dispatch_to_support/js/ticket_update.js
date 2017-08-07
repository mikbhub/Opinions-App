$(document).ready(function () {
    const response_menu = $('#response-create');
    const close_menu = $('#ticket-close');
    response_menu.click(function () {
        $( this ).find('form').submit();
    });
    close_menu.click(function () {
        $( this ).find('form').submit();
    });
});