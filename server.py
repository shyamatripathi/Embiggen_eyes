import os
import subprocess
import http.server
import socketserver

PORT = 10000  

if not os.path.exists("simple_test.html"):
    print("⚙️ Running create_tiles.py to generate tiles and viewer...")
    subprocess.run(["python", "create_tiles.py"], check=True)
else:
    print("✅ Tiles and HTML already exist, skipping generation.")


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Serving at port {PORT}")
    print("🌐 Visit your site on Render after deployment.")
    httpd.serve_forever()
