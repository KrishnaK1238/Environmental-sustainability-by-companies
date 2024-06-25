import praw
from transformers import pipeline

# Reddit API credentials
reddit = praw.Reddit(
    client_id='WC-c4C5SG4j0x9nVbG_SmQ',
    client_secret='dRWVFQ6Q7OjR9AMnm9aRuKJQRysbrw',
    user_agent='AgentHistorical9521',  # Example: 'Mozilla/5.0 (compatible; YOUR_APP_NAME/1.0)'
    username='AgentHistorical9521',
    password='Vin123cius1238$'
)

# Function to extract comments from a Reddit post
def extract_comments(submission_url):
    try:
        submission = reddit.submission(url=submission_url)
        submission.comments.replace_more(limit=None)
        comments = [comment.body for comment in submission.comments.list()]
        return comments
    except praw.exceptions.PRAWException as e:
        print(f"An error occurred: {e}")
        return []

# Perform sentiment analysis using Hugging Face Transformers
def analyze_sentiments(comments):
    sentiment_pipeline = pipeline("sentiment-analysis")
    sentiment_results = []
    
    for comment in comments:
        sentiment = sentiment_pipeline(comment)[0]
        sentiment_results.append({'comment': comment, 'sentiment': sentiment['label'], 'score': sentiment['score']})
    
    return sentiment_results

# Example Reddit post URL
submission_url = 'https://www.reddit.com/r/cars/comments/pgipsn/genesis_to_become_evonly_brand_from_2025_carbon/'

# Extract comments
comments = extract_comments(submission_url)

# Perform sentiment analysis
if comments:
    sentiment_results = analyze_sentiments(comments)

    # Output the sentiment analysis results
    for result in sentiment_results:
        print(f"Comment: {result['comment']}")
        print(f"Sentiment: {result['sentiment']}, Score: {result['score']:.2f}")
        print()

    # Save results to a JSON file (optional)
    import json
    with open('genesis_senti_res.json', 'w') as f:
        json.dump(sentiment_results, f, indent=2)
else:
    print("No comments found or an error occurred.")