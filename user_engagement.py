import json
import matplotlib.pyplot as plt

# Function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load the JSON data
comments_data = load_json('combination_of_comments.json')

# Initialize variables for score categories
high_engagement = 0
medium_engagement = 0
low_engagement = 0

# Process each comment
for comment in comments_data:
    score = comment['score']
    if score >= 100:
        high_engagement += 1
    elif 25 <= score < 100:
        medium_engagement += 1
    else:
        low_engagement += 1

# Data for the bar chart
categories = ['High Engagement (>= 100)', 'Medium Engagement (25-100)', 'Low Engagement (< 25)']
values = [high_engagement, medium_engagement, low_engagement]
colors = ['#ff9999','#66b3ff','#99ff99']

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=colors)
plt.xlabel('Engagement Level (Scores)')
plt.ylabel('Number of Comments')
plt.title('User Engagement Analysis')
plt.show()

# Print the calculated engagement counts
print(f"High Engagement: {high_engagement}")
print(f"Medium Engagement: {medium_engagement}")
print(f"Low Engagement: {low_engagement}")