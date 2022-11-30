import webbrowser

firefox_path = "/usr/bin/firefox-nightly"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
