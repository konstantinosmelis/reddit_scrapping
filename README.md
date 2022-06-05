# Reddit Scrapping Flask app

This is a simple flask application that takes images from the r/EarthPorn subreddit, using the [Reddit API](https://www.reddit.com/dev/api), and places them on a map.

## Install and run

```bash
git clone https://github.com/konstantinosmelis/reddit_scrapping.git flask_app && \
cd flask_app && \
pip install -r requirements.txt && \
spacy download en_core_web_md && \
```

You should also add a `.env` file where the `GEONAMES_KEY` key would be present.

Then open your browser and go to: [http://localhost:5000/](http://localhost:5000)