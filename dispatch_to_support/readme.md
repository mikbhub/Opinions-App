# Dispatch to support
*This app provides tasks queue to be consumed by customer support (human or bot)*.

## Features

### Priority queue
- holds tasks prioritized by metrics computed by **get_metrics** app.
- TODO: replace PriorityQueue with `Celery`

### Interface for human customer support
* request next task
* see opened tasks
* take action on a task:
    * write a response to customer complaint