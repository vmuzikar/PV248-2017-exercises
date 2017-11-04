#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer


class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        body = "You requested: {}\n\n".format(self.path)
        body += "Headers:\n{}".format(self.headers)

        self.wfile.write(bytes(body, "utf-8"))
        return


def main():
    print("Starting server...")
    server = HTTPServer(("", 8080), TestHandler)
    print("Server started!")
    server.serve_forever()


if __name__ == "__main__":
    main()
