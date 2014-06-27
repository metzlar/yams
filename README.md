yams
====

Yet Another Monitoring Service

Work in progress.

## Clients

The client (monitored computer) runs a 'collector' 
process continuously. An example can be found in the bin folder:

    bin/example_collector

The collector process creates a file
containing a metric's value for each metric being collected. And
puts the file in the /tmp/yams folder and keeps its contents as
much up to date as possible.

a second process reads out all files in /tmp/yams and
creates a JSON formatted UDP message containing all 
metrics and send it to the server every 2 seconds.

The process can be found in the bin folder:

    bin/client <file> <host> <port>

## Server

A process on the server listens for incoming UDP JSON messages from
monitored computers and stores the contents in
a memcache value under the "YAMS" key.

The process can be found in the bin folder:

    bin/server <port>

## Web page

A twisted wsgi server, invoke with:

    bin/wsgi

and visit http://localhost:8080

The web page queries the wsgi application every 1.9 seconds.

The wsgi application 'serves' the contents of the memcache "YAMS"
value.

## Thresholds

Set thresholds by defining `window.thresholds` in `yams/threshold_conf.js`. 
This variable must contain a list of objects, each object representing a threshold:

    [{q:JQUERY_QUERY, lt:LESS_THEN, gt:GREATER_THEN}, ...]
   
So to have a threshold for cpu_usage of 80%:

    ... {
	    q: 'dd[data=cpu_usage]',
	    gt: 80
    }, ...
    
A threshold for at least one memcached proces:

    ... {
	    q: 'dd[data=count_of_memcached]',
	    lt: 1
    }, ...

A threshold for less then 8 apached processes for server `1.2.3.4`:

    ... {
	    q: 'dd[data=1.2.3.4] dd[data=count_of_apached]',
	    lt: 8
    }, ...

While metrics exceed (or fall short in case of `lt`) their threshold 
their `<dd>` tag will have the `gt-alert` or `.lt-alert` css class. 

TODOs

A little javascript for the web page that checks queried properties
and alerts the user by changing styling based on 'treshold' rules.

Styling
