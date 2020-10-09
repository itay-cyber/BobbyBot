import os
import webview
htmlFile = os.path.dirname(os.path.abspath(__file__)).replace("app.py", "index.html")
webview.create_window('Bobby Settings', 'file://index.html')
webview.start()