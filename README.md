# PollPoster

PollPoster was an attempt at automating Twitter polls that I created (and never used) back in 2019, when I got [really](https://twitter.com/kerokerobotnito), [really](https://twitter.com/DailyGrips), [really](https://github.com/Nathansbud/TuningFork/blob/master/lyricbot.py) into [polls](https://github.com/Nathansbud/PollExtracter) and [bots](https://github.com/Nathansbud/Wikipedaily) and [social media APIs](https://github.com/Nathansbud/KeywordStreamer) and...[data](https://github.com/Nathansbud/MessageAnalysis)?

Reviving this 4 years later as a means of playing around with [instagrapi](https://adw0rd.github.io/instagrapi/), which wraps private Instagram API to expose things like story polls. I'd given up on creating daily Instagram polls, but now I am reinspired. 

Or I would be, if making new accounts didn't get me autoflagged with "The IP address you are using has been flagged as an open proxy. If you believe this to be incorrect, please visit https://help.instagram.com/"

# Installation

I use `requirements.in` to only lock immediate dependencies (rather than their transient dependencies). To install, run `pip-compile requirements.in`, then install requirements normally!

`pip-compile` requires `pip-tools`, which can be installed (shockingly) via `pip` (i.e. `pip install pip-tools`).
