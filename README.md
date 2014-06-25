yams
====

Yet Another Monitoring Service

Work in progress.

## Clients

Basically we have a process running on each monitored computer
the process reads out some text file and sends the contents to 
the server every 2 seconds. The file is supposed to be a JSON
encoded structure containing key-value properties that are 
monitored.

The process can be found in the bin folder:

    bin/client <file> <host> <port>

## Server

A process on the server listens for incoming JSON messages from
monitored computers and stores the contents (as it was read from
the file on the client machine using the bin/client process) in
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


TODOs

A little javascript for the web page that checks queried properties
and alerts the user by changing styling based on 'treshold' rules.

Styling