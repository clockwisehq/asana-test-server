from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import pkce

class handler(BaseHTTPRequestHandler):
  def do_GET(self):

    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    code_verifier = pkce.generate_code_verifier(length=128)
    code_challenge = pkce.get_code_challenge(code_verifier)
    print(code_verifier)

    message = '''
	<a href="https://app.asana.com/-/oauth_authorize
	?client_id=1199633622740714
	&redirect_uri=https://localhost:8080/app
	&response_type=code
	&state=thisIsARandomString
	&code_challenge_method=S256
	&code_challenge={}
	&scope=default">Authenticate with Asana</a>'''.format(code_challenge)
    self.wfile.write(bytes(message, "utf8"))
httpd = HTTPServer(('localhost', 8080), handler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
