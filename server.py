from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

	def do_GET(self): # Trata a requisição do tipo GET feita pelo navegador
		if self.path == '/': # Verifica o caminho da requisição
			self.path = '/index.html' # Define o arquivo index.html como homepage
		try: 
			file_to_open = open(self.path[1:]).read() # Abre o arquivo e carrega as informações na variável file_to_open
			self.send_response(200) #Responde 200 quando Funciona
		except: 
			file_to_open = "Error 404: File not found" # Atribui o texto à variável
			self.send_response(404) #Responde 404 quando não tem acesso
		self.end_headers() # Fim da respota do servidor
		self.wfile.write(bytes(file_to_open, 'utf-8')) # Escreve a informação na tela

httpd = HTTPServer(('0.0.0.0', 8080), Serv) # Cria o servidor
httpd.serve_forever() # Faz o servidor rodar pra sempre



