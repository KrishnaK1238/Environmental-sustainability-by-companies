import praw
import json

# Initialize the Reddit instance
reddit = praw.Reddit(client_id='WC-c4C5SG4j0x9nVbG_SmQ',
                     client_secret='dRWVFQ6Q7OjR9AMnm9aRuKJQRysbrw',
                     user_agent='AgentHistorical9521')

# Specify the post you want to scrape (example post ID)
post_id = 'q2n618'  # Replace with the actual post ID

# Fetch the post
submission = reddit.submission(id=post_id)

# Print the post details
print(f'Title: {submission.title}')
print(f'Author: {submission.author}')
print(f'Score: {submission.score}')
print(f'URL: {submission.url}')
print(f'Selftext: {submission.selftext}')
print(f'Number of comments: {submission.num_comments}')

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

# Save the post and comments to a JSON file
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
output_file = 'reddit_post_data.json'

# Save data to JSON file
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f'Data has been saved to {output_file}')
