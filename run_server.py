import socketserver
from plugin.config import CONFIG
from plugin.server import LocalAudioHandler
from plugin.db_utils import attempt_init_db
from plugin.util import attempt_init_data_dir

class DebugTCPServer(socketserver.TCPServer):
    # https://stackoverflow.com/a/42147927
    allow_reuse_address = True

if __name__ == "__main__":
    # If we're not in Anki, run the server directly and blocking for easier debugging
    attempt_init_data_dir()
    attempt_init_db()

    print("Running local audio server in debug mode...")
    httpd = DebugTCPServer((CONFIG["host"], CONFIG["port"]), LocalAudioHandler)
    httpd.serve_forever()

