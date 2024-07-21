import praw
from transformers import pipeline
import json
import re

# Initialize Reddit instance
reddit = praw.Reddit(client_id='WC-c4C5SG4j0x9nVbG_SmQ',
                     client_secret='dRWVFQ6Q7OjR9AMnm9aRuKJQRysbrw',
                     user_agent='AgentHistorical9521')

# Fetch comments from a specific Reddit post
def fetch_comments(post_url):
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)
    comments = []
    for comment in submission.comments.list():
        comments.append(comment.body)
    return comments

# Example URL of a Reddit post
post_url = "https://www.reddit.com/r/cars/comments/l70yaw/general_motors_plans_to_exclusively_offer/"

# Fetch comments
comments = fetch_comments(post_url)

# Initialize sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Perform sentiment analysis on each comment
sentiments = []
for comment in comments:
    result = sentiment_pipeline(comment)
    sentiment_label = result[0]['label']
    sentiment_score = result[0]['score']
    sentiments.append({
        "comment": comment,
        "sentiment": sentiment_label,
        "score": sentiment_score
    })

# Save results to a JSON file
output_file = "sentiment_analysis_results.json"
with open(output_file, 'w') as f:
    json.dump(sentiments, f, indent=4)

print(f"Sentiment analysis results saved to {output_file}")

# Function to check if a comment should be filtered
def should_filter_comment(comment):
    if "[deleted]" in comment or "[removed]" in comment:
        return True
    # Check if comment contains URLs using regex
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if re.search(url_pattern, comment):
        return True
    return False

# Filter out unwanted comments
filtered_sentiments = [entry for entry in sentiments if not should_filter_comment(entry["comment"])]

# Save filtered results to a new JSON file
filtered_output_file = "gm_sentiment.json"
with open(filtered_output_file, 'w') as f:
    json.dump(filtered_sentiments, f, indent=4)

print(f"Filtered sentiment analysis results saved to {filtered_output_file}")
