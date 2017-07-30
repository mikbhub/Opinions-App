'use strict';

// ajax app
$(document).ready(function () {
    console.log('script loaded');

    let endpoint = 'http://127.0.0.1:8110/collect_opinions/api/feedbacks/new/';
    let form = document.forms.feedbackform;

    $(form).submit(function (event) {
        event.preventDefault();
        alert('sending');
        $.ajax({
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
            success: function () {
                alert('Thank you for your opinion.');
            }
        });
    });
});