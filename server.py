from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/':
			self.path = '/index.html'
		try: 
			file_to_open = open(self.path[1:]).read()
			self.send_response(200) #Responde 200 quando Funciona
		except: 
			file_to_open = "Error 404: File not found"
			self.send_response(404) #Responde 404 quando não tem acesso
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('0.0.0.0', 8080), Serv)
httpd.serve_forever()



