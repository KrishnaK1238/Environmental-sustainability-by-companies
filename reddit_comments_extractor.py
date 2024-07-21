import praw
import json

# Replace these with your own credentials
client_id = 'WC-c4C5SG4j0x9nVbG_SmQ'
client_secret = 'dRWVFQ6Q7OjR9AMnm9aRuKJQRysbrw'
user_agent = 'AgentHistorical9521'

# Initialize the Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Specify the Reddit post (replace with your desired post ID)
post_id = '1d75gqu'  # e.g., 'abcd1234'

# Fetch the submission
submission = reddit.submission(id=post_id)
submission.comments.replace_more(limit=None)  # Ensure all comments are fetched

# Extract comments
comments_data = []
for comment in submission.comments.list():
    comments_data.append({
        "comment": comment.body,
        "author": str(comment.author),
        "score": comment.score
    })

# Filter out comments that contain "[removed]", "[deleted]", or URLs
filtered_comments = [
    comment for comment in comments_data 
    if '[removed]' not in comment['comment'] 
    and '[deleted]' not in comment['comment'] 
    and 'http' not in comment['comment']
]

# Save the comments to a JSON file
with open('Honda_comments.json', 'w') as json_file:
    json.dump(filtered_comments, json_file, indent=4)

print("Comments have been extracted and saved")
