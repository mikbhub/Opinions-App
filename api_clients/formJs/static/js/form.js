'use strict';

// ajax app
$(document).ready(function () {

    let endpoint = 'http://127.0.0.1:8110/collect_opinions/api/feedbacks/new/';
    let form = document.forms.feedbackform;

    // set notification timeout in microseconds. 1000 ms = 1 s
    let notification_timeout = 4000;

    $(form).submit(function (event) {
        event.preventDefault();
        Materialize.toast('Sending!', notification_timeout);
        let request = $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: endpoint,
            data: JSON.stringify({
                'customer': {
                    'email': form.email.value,
                    'first_name': form.first_name.value,
                    'last_name': form.last_name.value
                },
                'text': form.text.value,
                'source_type': 'formjs',
                'source_url': 'http://127.0.0.1:8120/'
            }),
            dataType: 'json',
        });
        request.done(function (xhr, status) {
            // Materialize.toast(message, displayLength, className, completeCallback);
            Materialize.toast('Thank you for your opinion!', notification_timeout, 'green'); // 4000 is the duration of the toast
            // alert('Thank you for your opinion.');
            $('button').prop('disabled', true);
        });
        request.fail(function (xhr, status, errorThrown) {
            Materialize.toast(`Sorry, there was a problem!: ${errorThrown} Status: ${xhr.status}`, notification_timeout, 'red darken-1'); // 4000 is the duration of the toast
            let json_error = xhr.responseText;
            Materialize.toast(`Response: ${json_error}`, notification_timeout); // 4000 is the duration of the toast
        });
    });
});