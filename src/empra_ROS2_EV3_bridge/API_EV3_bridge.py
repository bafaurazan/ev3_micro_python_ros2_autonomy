from http.server import BaseHTTPRequestHandler, HTTPServer
import requests  # biblioteka do wysyłania zapytań HTTP

PORT = 8081

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/command":
            try:
                # wysyłamy GET do drugiego serwera
                r = requests.get("http://192.168.74.64:8082/command", timeout=3)

                # przygotowujemy odpowiedź (np. treść odpowiedzi tamtego serwera)
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(r.text.encode())

            except Exception as e:
                # obsługa błędów (np. drugi serwer nie działa)
                self.send_response(500)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(f"Błąd połączenia z serwerem: {e}".encode())

        else:
            self.send_response(404)
            self.end_headers()


with HTTPServer(("", PORT), Handler) as server:
    print("Serwer gotowy na porcie", PORT)
    server.serve_forever()
