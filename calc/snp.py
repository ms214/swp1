from cgi import parse_qs
from snptem import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]
	htmltem ='' 
	try:	
		a, b = int(a), int(b)
		htmltem="sum= "+str(a+b)+", multi= "+str(a*b)		
	except ValueError:
		htmltem='Please Input a, b'
	response_body = html % (htmltem)
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]
