"""
Apple App Store Reviews API: A Quick Start Example
See more at: https://apify.com/johnvc/apple-app-store-reviews-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/apple-app-store-reviews-api/input-schema?fpr=9n7kx3

This script shows how to call the Apple App Store Reviews API on Apify from
Python and read its structured JSON output. Each result is one review: star
rating, title, body text, author, app version, dates, and helpfulness counts,
for any iOS or macOS app across 50+ country stores.

It exercises several input parameters so you can see what is configurable, while
keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one app, max_reviews=10) to keep this first run
# inexpensive. Raise max_reviews, add more product_ids, or set max_reviews=0
# for unlimited once you have your own API key and know your budget.
#
# You can target an app two ways:
#   1. product_ids: numeric Apple App Store IDs (found after "id" in an
#      apps.apple.com URL, e.g. .../id534220544).
#   2. app_name: a plain app name the API resolves for you (handy when you do
#      not know the numeric ID). Provide one or the other.
run_input = {
    "product_ids": ["534220544"],          # numeric App Store ID(s)
    # "app_name": "netflix",               # alternative: resolve by name instead
    "country": "us",                        # Apple country store (drives locale)
    "sort": "mostrecent",                   # mostrecent | mosthelpful | mostfavorable | mostcritical
    "max_reviews": 10,                      # small cap keeps the first run cheap; 0 = unlimited
    "start_page": 1,                        # page to start paginating from
    "include_macos": True,                  # include macOS apps as well as iOS
    "normalize_dates": True,                # also emit review_date_iso (ISO 8601)
    "parse_helpfulness": True,              # parse helpful_count / total_helpful_count integers
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/apple-app-store-reviews-api").call(run_input=run_input)

# Read structured results from the run's default dataset
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"Returned {len(items)} review(s).\n")

# Show a few key fields from each review.
for item in items:
    stars = item.get("rating")
    title = item.get("review_title") or "(no title)"
    author = item.get("author_name") or "(anonymous)"
    date = item.get("review_date_iso") or item.get("review_date") or ""
    version = item.get("reviewed_version") or ""
    platform = item.get("app_platform") or ""
    body = (item.get("review_text") or "").strip().replace("\n", " ")
    if len(body) > 140:
        body = body[:137] + "..."

    print(f"[{stars}/5] {title}  -  {author}  ({date}, {version}, {platform})")
    print(f"    {body}\n")
