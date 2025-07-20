import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('twitter_training.csv', header=None, names=['id', 'topic', 'sentiment', 'tweet'])

# Clean up the sentiment labels (optional, if there are upper/lower case issues)
df['sentiment'] = df['sentiment'].str.capitalize()

# Count sentiment frequencies
sentiment_counts = df['sentiment'].value_counts()

# Display distribution as a barplot
plt.figure(figsize=(8,6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='pastel')
plt.title('Sentiment Distribution in Social Media Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.show()

# If you want to look at sentiment over different topics, use a countplot:
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='sentiment', hue='topic', order=sentiment_counts.index)
plt.title('Sentiment Distribution by Topic')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# OPTIONAL: Wordcloud (install wordcloud first)
# from wordcloud import WordCloud
# for sentiment in df['sentiment'].unique():
#     text = ' '.join(df[df['sentiment'] == sentiment]['tweet'])
#     wc = WordCloud(width=600, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(8,5))
#     plt.imshow(wc, interpolation='bilinear')
#     plt.axis('off')
#     plt.title(f'Wordcloud for {sentiment} Tweets')
#     plt.show()

# Example: Calculate ratio of positive to negative for a specific topic
topic = 'Borderlands'
topic_df = df[df['topic'] == topic]
pos = len(topic_df[topic_df['sentiment'] == 'Positive'])
neg = len(topic_df[topic_df['sentiment'] == 'Negative'])
neutral = len(topic_df[topic_df['sentiment'] == 'Neutral'])
print(f'For topic "{topic}": Positive={pos}, Negative={neg}, Neutral={neutral}')
