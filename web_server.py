import http.server
import socketserver
import ssl
import os
#com a chave SSL E RSA
# PORT = 5050
# DIRECTORY = "." 

# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = 'index.html'
        
#         return super().do_GET()

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain(certfile="../serverpjt.crt", keyfile="../pojeto.key")

# os.chdir(DIRECTORY)

# with socketserver.ThreadingTCPServer(("", PORT), MyHttpRequestHandler) as httpd:
#     print(f"Servidor iniciado na porta {PORT}. Acesse https://localhost:{PORT}")
#     httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
#     httpd.serve_forever()


PORT = 5050
DIRECTORY = "." 

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'home.html'
        
        return super().do_GET()
os.chdir(DIRECTORY)

# Inicia o servidor sem SSL e com Threading
with socketserver.ThreadingTCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Servidor iniciado na porta {PORT}. Acesse http://localhost:{PORT}")
    httpd.serve_forever()