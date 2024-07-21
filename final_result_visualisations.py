import json
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
from docx import Document

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# File path for the JSON input
input_file = 'Honda_sentiment.json'

# Load the data from the JSON file
data = load_json(input_file)

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Count the total number of positive and negative comments
total_comments = df['sentiment'].value_counts().to_dict()

# Ensure the dictionary contains both sentiments
if 'POSITIVE' not in total_comments:
    total_comments['POSITIVE'] = 0
if 'NEGATIVE' not in total_comments:
    total_comments['NEGATIVE'] = 0

# Calculate percentages
total_count = sum(total_comments.values())
percentages = {sentiment: (count / total_count) * 100 for sentiment, count in total_comments.items()}

# Convert to DataFrame for easy plotting
percentage_df = pd.DataFrame(list(percentages.items()), columns=['sentiment', 'percentage'])

# Plotting
plt.figure(figsize=(10, 6))

# Colors and explode settings for the pie chart
colors = ['red', 'green']
explode = (0.1, 0)  # explode the first slice (i.e., 'POSITIVE')

# Pie Chart for Comment Percentages
patches, texts, autotexts = plt.pie(percentage_df['percentage'], labels=percentage_df['sentiment'],
                                    autopct='%1.1f%%', colors=colors, explode=explode,
                                    startangle=140, wedgeprops={'edgecolor': 'black'})

# Styling the text and auttext
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('white')
    autotext.set_weight('bold')

# Add title and legend
plt.title("Honda 2024 Business Briefing - Honda's plans for electric vehicles and hybrids: How did reddit users react to this initiative?", fontsize=14)
plt.legend(patches, ['Percentage of users who reacted negatively to this initiative',
                     'Percentage of users who reacted positively to this initiative'],
           loc='upper right', fontsize=9, bbox_to_anchor=(1.5, 1))

# Display the plot
plt.tight_layout()
plt.show()