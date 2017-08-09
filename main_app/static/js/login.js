$(function () {
    let form = $("form");
    form.find( "input[name='username']" ).autocomplete({
        data: {
            "customer_support_person": null,
        },
        limit: 20, // The max amount of results that can be shown at once. Default: Infinity.
        onAutocomplete: function (val) {
            // Callback function when value is autcompleted.
        },
        minLength: 0, // The minimum length of the input for the autocomplete to start. Default: 1.
    });
    form.find( "input[name='password']" ).autocomplete({
        data: {
            "OpinionsAppDemo": null,
        },
        limit: 20, // The max amount of results that can be shown at once. Default: Infinity.
        onAutocomplete: function (val) {
            // Callback function when value is autcompleted.
        },
        minLength: 0, // The minimum length of the input for the autocomplete to start. Default: 1.
    });
});

