# if the name isn't plugin, it's likely LocalAudioDev or 1045800357
# (meaning it was ran by Anki!)
# This if statement prevents the functions from automatically running
# and essentially starting the server again
if __name__ != "plugin":
    from aqt import mw

    from .consts import PORT
    from .server import run_server
    from .gui import init_gui

    addon_config = mw.addonManager.getConfig(__name__) or {}
    server_port = addon_config.get("port", PORT)

    run_server(port=server_port)
    init_gui()
