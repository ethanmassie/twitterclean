# twitterclean
Simple python script for blocking followers, unfollowing, and deleting all statuses for a twitter account. 

Requires:
- python
- tweepy
- twitter api credentials

Add your credentials to the credentials.ini file.

```
usage: twitterclean.py [-h] [--no-block] [--no-unfollow] [--no-delete-tweets]
                       [--quiet]

Clean up twitter account

optional arguments:
  -h, --help          show this help message and exit
  --no-block          disable blocking followers
  --no-unfollow       disable unfollowing accounts you follow
  --no-delete-tweets  disable deleting tweets
  --quiet, -q         silence output
```
