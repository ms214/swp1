from cgi import parse_qs
from snptem import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]
	global html
	htmltem = html
	if '' not in [a, b]:
		a, b = int(a), int(b)
		htmltem+="sum= "+str(a+b)+", multi= "+str(a*b)		
	response_body = htmltem
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]