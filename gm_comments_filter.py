import json

# Function to filter comments based on score
def filter_comments(comments, min_score=5):
    filtered_comments = [comment for comment in comments if comment['score'] >= min_score]
    return filtered_comments

# Load input data from JSON file
input_file = "gm_comments.json"  # Replace with your input JSON file path
with open(input_file, 'r', encoding='utf-8') as f:
    input_data = json.load(f)

# Filter the input data
filtered_data = filter_comments(input_data)

# Save filtered data back to the same file
with open(input_file, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=4)

print(f"Filtered comments with score >= {5} saved to {input_file}")
