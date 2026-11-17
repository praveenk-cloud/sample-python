from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Listening on port 80!")

server = HTTPServer(("0.0.0.0", 80), SimpleHandler)
print("Server running on port 80...Hello World")
server.serve_forever()
