# Environmental-sustainability-by-companies
Our Research question:
What kind of user engagement can be seen on reddit regarding environmental sustainability by the automotive companies?
How did reddit users react to the initiatives taken by companies towards achieving environmental sustainability?
University project which involves performing User engagement analysis using NLP techniques such as Sentiment analysis and Emotion analysis. We have taken 4 companies into consideration: Porsche, Genesis, General Motors and Honda. For Porsche we have done emotion analysis and for the rest three we have done sentiment analysis.
Based on our previous research from the paper "Chan, C. C., Han, W., Tian, H., Liu, Y., Ma, T., & Jiang, C. Q. (2023). Automotive revolution and carbon neutrality. Frontiers in Energy, 17(6), 693–703. https://doi.org/10.1007/s11708-023-
0890-8". Which talks about the impact of automobiles on the environment, we wanted to research about what the companies are doing to tackle this problem and how the users are reacting to these initiatives by the companies.
We extract comments from a Reddit post which is relevant to our Research topic. To extract comments we used a python library called PRAW (Python Reddit Api Wrapper) which is specifically used to scrape data from Reddit.
The extracted comments are cleaned and stored in a JSON file and taking this JSON file as an input we perform sentiment and emotion analysis using the NLP library "Transformers by Hugging Face".
Each comment is labelled with either a Positive or Negative tag depending on the sentiment and a score is also mentioned which the confidence of the analysis, i.e. how confident the library is that the comment is either positive or negative, this is done by give the score from a range of 0-1, 0 means not confident, 1 means very confident.
For emotion analysis we have used the same NLP library (Transformers) which analyses the Reddit comment and labels them with labels like: Anger, Disgust, Suprised, Fear and Neutral. These labels show how the users feel about the companies initiative through the comments.
We also answer the question of why the users reacted in such a manner, that is the goal of our research, we want to know why the majority of users reacted negatively towards these initiatives by the companies.
We have created a separate document in the same repository which answers the question to why users reacted negatively.
