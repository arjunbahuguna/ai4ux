1. [Link to demo-video](https://wetransfer.com/downloads/d30e575ed297db77329d92ad95771ced20210307215448/8a2a49)<br>
2. [Link to XD website design](https://xd.adobe.com/view/5789e5de-1b5b-4805-99c5-45a0700862df-02da/?fullscreen)

## Commentree (Evaluate your UX through actual users!)

### The Problem
UX designers value user feedback highest. The user's word is the gold standard. But we often overlook the greatest source of user feedback: social media. In ignoring the 'collective knowledge' of their user group and by not being able to listen to their UI complaints online, UX designers miss out on important insights.

## The Solution
Using machine learning for social media analysis, we mine existing user feedback (user reviews, tweets, etc) about a product available on social media sites like Twitter, Facebook, Instagram to recommend UX/UI design changes. This gives the UX designer continuous and direct feedback from their actual users, and our analysis recommends changes to the design.

## The Framework
We use the below framework to measure our product's UX from online reviews posted to social media.
<img src="https://raw.githubusercontent.com/standard-deviant/ai4ux/main/hexagon.jpeg">
## Implementing the Framework on Social Media User Feedback:
| UX Framework Attribute | Words to look out for in user feedback |
| --- | --- |
| Useful | Understandable, Consistent, Error, Approachable, ... |
| Desirable | Appropriate, Efficient, Truthful, Engaging, ... |
| Accessible | Disability, Visibility, Read Aloud, Difficult, ... |
| Secure | Permission, Location, Data, Confidence, Reliable, ... |                                     
| Usability | Consistent, Completion, Informing, Navigation, ... |

# Process
## The Data
The users' feedback has been sourced from Twitter & App store reviews for this prototype, but can be sourced from any social media or app platform we want. The text data from the tweets contain words that can trigger one of the seven prongs of our UX framework. By mapping the text data of the tweet to our framework, we can evaluate the UX of the product.

## The Analysis
We use multiple analysis techniques from natural language processing (NLP) and supervised machine learning to do analysis on user tweets. Some of these techniques include:
#### 1. Sentiment analysis
Gain a measure of user satisfaction from the tweet by algorithmically measuring how positive or negative the sentiment of the tweet is.
#### 2. n-gram analysis
Tokenization and frequency analysis of text data from tweets and user reviews.
#### 3. Measuring UX success accroding to Framework
Use the 7-prong framework to determine the quality of the UX, from user feedback.
#### 4. Aid strategy
Prioritze which design bugs to fix first by visualizing frequency of particular complaints in user feedback.

## The Insights

### Frequently Occuring Words
<img src="https://raw.githubusercontent.com/standard-deviant/ai4ux/main/MostFrequentWords.jpeg">

### Negative Sentiment Distribution
<img src="https://raw.githubusercontent.com/standard-deviant/ai4ux/main/NegativeSntiment.jpeg">

### Positive Sentiment Distribution
<img src="https://raw.githubusercontent.com/standard-deviant/ai4ux/main/PositiveSentiment.jpeg">

### Word Cloud for representing most used words
<img src="https://raw.githubusercontent.com/standard-deviant/ai4ux/main/WordCloud.jpeg">


### Architecture Modules
#### 1. Collect User Feedback from tweets
#### 2. Analyze feedback to evaluate UX
#### 3. Gain insights in the form of graphs
#### 4. Suggest changes in UX according to user feedback


### Tech Stack
1. Jupyter notebook & Colab
2. Data analysis: pandas, numpy
3. Data visualization: seaboarn, matplotlib
4. Natural Language Processing: nltk, textblob, wordcloud
5. Twitter API
6. MongoDB
7. Adobe XD

### The Team
1. Daksha Dixit
2. Simran Singh
3. Arnav Ajay
4. Arjun Bahuguna
5. Poojita Sure
