import json
from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to perform sentiment analysis on comments
def perform_sentiment_analysis(comments):
    sentiment_results = []

    for entry in comments:
        comment = entry['comment']
        sentiment_analysis = sentiment_pipeline(comment)
        sentiment_label = sentiment_analysis[0]['label']
        sentiment_score = sentiment_analysis[0]['score']

        result_entry = {
            "comment": comment,
            "sentiment": sentiment_label,
            "score": sentiment_score,
        }
        sentiment_results.append(result_entry)

    return sentiment_results

# Path to the input JSON file containing comments
input_file = "Honda_comments.json"

# Read comments from the input JSON file
with open(input_file, 'r') as f:
    comments = json.load(f)

# Perform sentiment analysis on comments
sentiment_results = perform_sentiment_analysis(comments)

# Output file path for storing sentiment analysis results
output_file = "Honda_sentiment.json"

# Save sentiment analysis results to a JSON file
with open(output_file, 'w') as f:
    json.dump(sentiment_results, f, indent=4)

print(f"Sentiment analysis results saved to {output_file}")