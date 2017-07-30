'use strict';
// $(document).ready(function() {
//     console.log('script loaded');
//     let $button = $('button');
//     $button.on('click', function() {
//         $.getJSON('http://date.jsontest.com/', function(data) {
//             alert(data.time + ' ' + data.date);
//         });
//     });
// });
// ajax app
$(document).ready(function () {
    console.log('script loaded;');
    let url = 'http://127.0.0.1:8110/collect_opinions/api/feedbacks/new/';
    $('#submit').on('click', function (event) {
        event.preventDefault();
        alert('sending');
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: url,
            data: JSON.stringify({
                "customer": {
                    "email": "formjs@mail.com",
                    "name": "formjs"
                },
                "text": "formjs",
                "source_type": "formjs",
                "source_url": "http://127.0.0.1:8110/collect_opinions/api/feedbacks/new/"
            }),
            dataType: 'json',
            success: function () {
                alert('Thank you for your opinion.');
            }
        });
    });
});
