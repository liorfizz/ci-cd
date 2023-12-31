from flask import Flask, render_template
from redis import Redis
import os
import random


app = Flask(__name__)
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis = Redis(host=redis_host, port=redis_port)

# List of alpaca images
images = [
    "https://media3.giphy.com/media/QoncgdHL9TDm0ePySn/giphy.gif?cid=ecf05e47eqnn1ipow6vxu4crrsdhd46t2za1sh2bmgyvp0y6&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media2.giphy.com/media/c8pTpUed78PSg/giphy.gif?cid=ecf05e473chqondqlden75jnqclpmstfpdwqkgxlshn134oo&ep=v1_gifs_related&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/xT1XGDKwOxacd92rYI/giphy.gif?cid=ecf05e47e7yh3uq69oehvlgd2ubcycp6y0pa8c319uoxk5e0&ep=v1_gifs_related&rid=giphy.gif&ct=g"
]


@app.route("/")
def index():
    # Increment the site counter in Redis
    redis.incr("site_counter")
    # Get the current value of the site counter
    counter = redis.get("site_counter").decode("utf-8")
    url = random.choice(images)
    return render_template("index.html", url=url, counter=counter)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

