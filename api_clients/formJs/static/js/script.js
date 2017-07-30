"use strict";

// ajax app
$(document).ready(function() {
    let $button = $('button');
    $button.on('click', function() {
        $.getJSON('http://date.jsontest.com/', function(data) {
            alert(data.time + ' ' + data.date);
        });
    });
});