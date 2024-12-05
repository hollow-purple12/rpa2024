from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

os.chdir("C:/Users/shreya v/Desktop/rpa_project2024")

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
