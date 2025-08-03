from flask import Flask, render_template

import redis

import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def index():
    count = r.incr("visit_count")
    return render_template("count.html", count=count)

@app.route("/hello")
def hello():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
