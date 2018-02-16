# Inspiration
We wanted to see if genome data can help us find specific Yelp listings that we may like intrinsically.

## What it does
With our heuristic, we take the genome data input it into our predictive model, which invokes a Yelp search with high ranked Yelp categories. We integrated Google Maps into our app to give the user a look at where those Yelp listings around them.

## How we built it
We built upon the Flask example app and implemented the API integration.

## Challenges we ran into
Feature confusion and low data, as well as high bias in our weights.

## Accomplishments that we're proud of
We're proud that the Yelp listings we see at least pass our sanity checks.

## What we learned
Look at the data and check the slack for more details! Always pivot sooner than later.

## What's next for TasteBuds
Improve on our full-stack and data science/engineering skills with more projects like this!

### Set up
```
$ pip install -r requirements.txt
$ export GENOMELINK_CLIENT_ID=CLOmX1sWF2BRgmSgdP8L3VZlWaLqiGQnfFmVgqRl
$ export GENOMELINK_CLIENT_SECRET=GGwsYiUDKB9ESvGYXL9a7c1vQEtPsBgDXWwBDPxph5cYtaD9QceB2PRBZc7b1OEOuSUXEVWcRG9CbwtsKxTM07YTkol010glqrp3xhaYcsmmBCv55SPNxububAMidVtm
$ export GENOMELINK_CALLBACK_URL="http://127.0.0.1:5000/callback"
$ python app.py

Windows Equivalent

pip install -r requirements.txt
SET GENOMELINK_CLIENT_ID=CLOmX1sWF2BRgmSgdP8L3VZlWaLqiGQnfFmVgqRl
SET GENOMELINK_CLIENT_SECRET=GGwsYiUDKB9ESvGYXL9a7c1vQEtPsBgDXWwBDPxph5cYtaD9QceB2PRBZc7b1OEOuSUXEVWcRG9CbwtsKxTM07YTkol010glqrp3xhaYcsmmBCv55SPNxububAMidVtm
SET GENOMELINK_CALLBACK_URL="http://127.0.0.1:5000/callback"
python app.py

```

