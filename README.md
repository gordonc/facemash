## facemash website from "the social network"

#### rating algorithm:
* http://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details
* still need to tweak constants

#### dependencies:
* python
* sqlite3

#### setup:
    % sh insert.sh http://s3.amazonaws.com/crunchbase_prod_assets/assets/images/resized/0001/0688/10688v39-max-250x250.jpg
    % sh insert.sh https://github-images.s3.amazonaws.com/blog/2011/hubot.png
    % ...
    % python facemash.py
    % Serving HTTP on 0.0.0.0 port 8000 ...
