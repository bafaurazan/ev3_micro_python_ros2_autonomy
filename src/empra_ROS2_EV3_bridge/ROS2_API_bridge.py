from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8082
COMMAND = "20"  # Możesz zmieniać "A" lub "B"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/command":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(COMMAND.encode())
        else:
            self.send_response(404)
            self.end_headers()

with HTTPServer(("", PORT), Handler) as server:
    print("Serwer gotowy na porcie", PORT)
    server.serve_forever()
