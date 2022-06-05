import os
from dotenv import load_dotenv

load_dotenv()

GEONAMES_KEY = os.getenv("GEONAMES_KEY")

REDDIT_URL = "https://www.reddit.com/r/EarthPorn/new.json?limit=100"
