#!/usr/bin/env python3
import http.server
from logging import Handler
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("" , 80),Handler) as httpd:
    httpd.serve_forever()