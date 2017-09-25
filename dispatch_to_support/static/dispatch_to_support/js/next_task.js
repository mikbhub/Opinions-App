const api_endpoint = 'https://mikolajbabiak.pythonanywhere.com/dispatch_to_support/queue/next_task';
const notification_timeout = 6000;

const limi_reached = "Reached limit of open tickets";
const no_more_tickets = "There are no more tasks for now";

$(document).ready(function () {
    const next_button = $('#next-task');
    next_button.click(function (event) {
        event.preventDefault();

        let next_task_request = $.ajax({
            type: 'GET',
            url: api_endpoint,
            dataType: 'json',
        });
        next_task_request.done(function (json) {
            switch (json[0]) {
            case limi_reached:
                Materialize.toast(limi_reached, notification_timeout, 'blue');
                break;
            case no_more_tickets:
                Materialize.toast(no_more_tickets, notification_timeout, 'red');
                break;
            default:
                Materialize.toast('Fetching new task!', notification_timeout, 'green');
                $("#open-tickets").append(build_template(json));
                break;
            }
        });
        next_task_request.fail(function (xhr, status, errorThrown) {
            Materialize.toast(`Sorry, there was a problem!: ${errorThrown} Status: ${xhr.status}`, notification_timeout, 'red darken-1');
            let json_error = xhr.responseText;
            Materialize.toast(`Response: ${json_error}`, notification_timeout);
        });
    });
});

function build_template(json) {
    // building django url in javascript :(
    const newURL = window.location.protocol + "//" + window.location.host + "/" + "dispatch_to_support/ticked_update/" + json.support_ticket_pk;
    const template = `<li>
        <div class="collapsible-header">
            <span class="truncate">
                <div class="chip">
                    ${json.feedback.customer_name}
                </div>
                    ${json.feedback.text}
            </span>
        </div>
        <div class="collapsible-body">
            <div class="row">
                <p>${json.feedback.text}</p>
                <a class="waves-effect waves-light btn left" href="${newURL}">Details
                    <i class="material-icons right">visibility</i> 
                </a>
            </div>
        </div>
    </li>`;
    return template;
}