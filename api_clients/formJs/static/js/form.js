'use strict';

// ajax app
$(document).ready(function () {
    console.log('script loaded');

    let endpoint = 'http://127.0.0.1:8110/collect_opinions/api/feedbacks/new/';
    let form = document.forms.feedbackform;

    $(form).submit(function (event) {
        event.preventDefault();
        Materialize.toast('Sending!', 10000);;
        let request = $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: endpoint,
            data: JSON.stringify({
                "customer": {
                    "email": form.email.value,
                    "name": form.name.value
                },
                "text": form.text.value,
                "source_type": "formjs",
                "source_url": "http://127.0.0.1:8120/"
            }),
            dataType: 'json',
        });
        request.done(function (xhr, status) {
            // Materialize.toast(message, displayLength, className, completeCallback);
            Materialize.toast('Thank you for your opinion!', 10000); // 4000 is the duration of the toast
            // alert('Thank you for your opinion.');
            $("button").prop('disabled', true);
        });
        request.fail(function (xhr, status, errorThrown) {
            Materialize.toast(`Sorry, there was a problem!: ${errorThrown} Status: ${xhr.status}`, 10000); // 4000 is the duration of the toast
            let json_error = xhr.responseText;
            Materialize.toast(`Response: ${json_error}`, 10000); // 4000 is the duration of the toast
            console.log("Error: " + errorThrown);
            console.log("Status: " + status);
            console.dir(xhr);
        });
    });
});
