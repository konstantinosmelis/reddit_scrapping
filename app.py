from flask import Flask
import mapgenerator
import os
import time
import threading

app = Flask(__name__)

def thread_functions():
    mapgenerator.generate_map()
    time.sleep(3600)


@app.route("/")
def main():
    html_file = open(os.path.abspath("./templates/map.html"), "r")
    content = html_file.read()
    html_file.close()
    return content


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_functions)
    t1.start()
    app.run(host="0.0.0.0")
