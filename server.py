from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import pkce

class handler(SimpleHTTPRequestHandler):
  def do_GET(self):
    """
    code_verifier = pkce.generate_code_verifier(length=128)
    code_challenge = pkce.get_code_challenge(code_verifier)
    print(code_verifier)
    """
    self.path = 'index.html'
    return SimpleHTTPRequestHandler.do_GET(self)


httpd = HTTPServer(('localhost', 8080), handler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
