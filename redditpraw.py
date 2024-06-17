from os.path import isfile
import praw
import pandas as pd
from time import sleep
# Get credentials from DEFAULT instance in praw.ini
reddit = praw.Reddit()