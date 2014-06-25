from cgi import parse_qs
import os
import yams.store


static_html = open(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'static.html'
    )
).read()

threshold_config = open(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'threshold_conf.js'
    )
).read()

def query_status():
    return yams.store.get('YAMS')
    
def application(environ, start_response):

    parameters = parse_qs(environ.get('QUERY_STRING', ''))

    if 'query' in parameters:
        result = query_status()
        ct = 'text/json'
    else:
        result = static_html.replace(
            '<!--//TRESHOLD_CONFIG//-->',
            threshold_config
        )
        ct = 'text/html'        
    
    start_response('200 OK', [('Content-type', ct)])
    
    return [result]