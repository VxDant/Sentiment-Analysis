import re
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 1. create a text file to read data from it. read.txt
# 2. clean a the same data text file from punctuations
# 3. (what we have is data in a string format of lines.) MAKE A LIST FORMAT OF CLEANED WORDS
# 4. REMOVE UNNECESSARY WORDS. ONLY ADEQUATE AMOUNT OF WORDS ARE REQ. WHICH CARRY EMOTION
# 5. WE NEED THE COUNT THE AMOUNT OF THE EMOTIONAL WORDS. DISPLAY GRAPH

# 6. TWITTER MODULE

# 7. nltk toolkit. make settings.py file and download nltk.download()

file1 = open('read.txt', 'r+', encoding='utf-8')
content = file1.read().lower()
content_re = re.sub('[!@?.,]', '', content)

lis_words = word_tokenize(content_re, "english")

'''stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]'''

final_words = []

for word in lis_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []

with open('emotions.txt', 'r') as file2:
    for line in file2:
        line = re.sub('\n', '', line).replace("'", "").replace(",", "").strip()
        word, emotion = line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
c = Counter(emotion_list)
print(c)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    if score['neg'] > score['pos']:
        print("NEGATIVE VIBE")
    elif score['neg'] < score['pos']:
        print("POSITIVE VIBE")
    else:
        print("NEUTRAL VIBE")


sentiment_analyse(content_re)

fig, ax1 = plt.subplots()
fig.autofmt_xdate()
ax1.bar(c.keys(), c.values())
# plt.savefig('graph.png')
plt.show()
