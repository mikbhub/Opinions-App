'use strict';

// ajax app
$(document).ready(function () {
    let form = document.forms.feedbackform;
    console.log('script loaded;');
    let url = 'http://127.0.0.1:8120/';
    $(form).submit(function (event) {
        event.preventDefault();
        alert('sending');
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            url: url,
            data: JSON.stringify({
                "customer": {
                    "email": form.email.value,
                    "name": form.name.value
                },
                "text": form.text.value,
                "source_type": "formjs",
                "source_url": url
            }),
            dataType: 'json',
            success: function () {
                alert('Thank you for your opinion.');
            }
        });
    });
});
