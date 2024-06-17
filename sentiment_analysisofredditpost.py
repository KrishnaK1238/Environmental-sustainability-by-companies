import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

# Initialize the Reddit instance
reddit = praw.Reddit(client_id='WC-c4C5SG4j0x9nVbG_SmQ',
                     client_secret='dRWVFQ6Q7OjR9AMnm9aRuKJQRysbrw',
                     user_agent='AgentHistorical9521')

# Specify the post you want to scrape (example post ID)
post_id = 'tl3r2u'  # Replace with the actual post ID

# Fetch the post
submission = reddit.submission(id=post_id)

# Fetch comments
comments = []
submission.comments.replace_more(limit=0)  # Replace "More comments" placeholders
for comment in submission.comments.list():
    comments.append({
        'author': str(comment.author),
        'score': comment.score,
        'body': comment.body,
        'created_utc': comment.created_utc
    })

# Perform sentiment analysis using VADER
analyzer = SentimentIntensityAnalyzer()
for comment in comments:
    sentiment = analyzer.polarity_scores(comment['body'])
    comment['sentiment'] = sentiment

# Save the post and comments with sentiment analysis to a JSON file
data = {
    'post': {
        'title': submission.title,
        'author': str(submission.author),
        'score': submission.score,
        'url': submission.url,
        'selftext': submission.selftext,
        'num_comments': submission.num_comments
    },
    'comments': comments
}

# Specify the output file path
output_file = 'reddit_post_sentiment_analysis_audi.json'

# Save data to JSON file
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f'Data with sentiment analysis has been saved to {output_file}')
