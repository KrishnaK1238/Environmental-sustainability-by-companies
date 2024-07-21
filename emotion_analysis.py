import json
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import pipeline

# Load the JSON data
with open('porsche_post_comments.json', 'r') as file:
    data = json.load(file)

# Extract comments
comments = [entry['comment'] for entry in data]

# Preprocess the comments
def preprocess(text):
    text = re.sub(r'\n', ' ', text)  # Remove newline characters
    text = re.sub(r'\W', ' ', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text

cleaned_comments = [preprocess(comment) for comment in comments]

# Load the emotion analysis model
emotion_analyzer = pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base')

# Predict emotions and filter based on score
results = []
emotion_counts = {}

for comment in cleaned_comments:
    emotion = emotion_analyzer(comment)
    filtered_emotion = [e for e in emotion if e['score'] >= 0.6]
    if filtered_emotion:
        results.append({
            "comment": comment,
            "emotion": filtered_emotion
        })
        # Count emotions
        for e in filtered_emotion:
            label = e['label']
            if label in emotion_counts:
                emotion_counts[label] += 1
            else:
                emotion_counts[label] = 1

# Save the results to a JSON file
with open('porsche_emotion_analysis_results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

# Convert emotion counts to a DataFrame
emotion_df = pd.DataFrame(list(emotion_counts.items()), columns=['Emotion', 'Count'])

# Ensure there are at least some emotions to plot
if not emotion_df.empty:
    # Sorting the DataFrame for better visualization
    emotion_df = emotion_df.sort_values(by='Count', ascending=False)

    # Plotting the stacked bar chart
    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid")

    # Create the bar plot
    bar_plot = sns.barplot(x="Emotion", y="Count", data=emotion_df, palette="viridis")

    # Add title and labels
    plt.title('Porsche to suppliers: Switch to renewable energy or lose future contracts: Emotion Analysis of Reddit Comments', fontsize=15)
    plt.xlabel('Emotions', fontsize=15)
    plt.ylabel('No. of comments', fontsize=15)

    # Add the value annotations on the bars
    for p in bar_plot.patches:
        bar_plot.annotate(format(p.get_height(), '.0f'),
                          (p.get_x() + p.get_width() / 2., p.get_height()),
                          ha = 'center', va = 'center',
                          xytext = (0, 10),
                          textcoords = 'offset points',
                          fontsize=12)

    # Show the plot
    plt.xticks(rotation=45)
    plt.show()
else:
    print("No emotions with a score of 0.6 or higher were found in the comments.")

print("Filtered emotion analysis results have been saved to 'emotion_analysis_results.json'")