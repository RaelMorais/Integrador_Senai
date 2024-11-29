import http.server
import socketserver
import ssl
import os

PORT = 5050
DIRECTORY = "."  # O diretório onde o servidor irá procurar arquivos

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Se a requisição for para a raiz, redireciona para /ecommerce/index.html
        if self.path == '/':
            self.path = 'index.html'
        
        # Chama o método original para servir o arquivo
        return super().do_GET()

# Configura o contexto SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="../serverpjt.crt", keyfile="../pojeto.key")

# Define a raiz do diretório onde o servidor irá procurar os arquivos
os.chdir(DIRECTORY)

# Inicia o servidor com SSL e Threading
with socketserver.ThreadingTCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Servidor iniciado na porta {PORT}. Acesse https://localhost:{PORT}")
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
