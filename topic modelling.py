#Author: Hana Arshid #topic: cognitive and emotional experience #date: 20/01/2025

import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import plotly.express as px

nltk.download('stopwords')
nltk.download('punkt')

file_path = '/Users/hanairshaid/Desktop/Wonder Cabinet - Instagram Posts.xlsx'

data = pd.read_excel(file_path)

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = ''.join([char for char in text if char not in string.punctuation])  
    tokens = word_tokenize(text.lower())  
    tokens = [word for word in tokens if word not in stop_words]  
    return tokens

documents = data['Post'].dropna().apply(preprocess_text).tolist()

all_tokens = [token for doc in documents for token in doc]
token_counts = Counter(all_tokens)

themes = {
    "Sound as Artefact": ["valley", "hymns", "recitals", "historical", "craft"],
    "Sound as Art": ["performances", "concerts", "artistic", "expression", "creativity"],
    "Sound as Lecturing": ["guided", "narratives", "awareness", "knowledge", "education"],
    "Sound as Ambiance/Soundtrack": ["environments", "soundtrack", "soothing", "peaceful", "relaxing"],
    "Sound as Crowd Curation": ["collective", "hands-on", "therapy", "exchanges", "gathering"],
}

theme_frequencies = {}
for theme, keywords in themes.items():
    theme_frequencies[theme] = {word: token_counts[word] for word in keywords if word in token_counts}

top_keywords = {}
for theme, keywords in theme_frequencies.items():
    sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
    top_keywords[theme] = sorted_keywords[:5]

visualization_data = []
for theme, keywords in top_keywords.items():
    for keyword, count in keywords:
        visualization_data.append({
            'Theme': theme,
            'Keyword': keyword,
            'Frequency': count
        })

df = pd.DataFrame(visualization_data)

fig = px.bar(df, 
             x='Keyword', 
             y='Frequency', 
             color='Theme', 
             barmode='group', 
             title='<b>Top 5 Keywords for Each Sound Theme</b>',
             labels={'Keyword': 'Word', 'Frequency': 'Frequency', 'Theme': 'Theme'},
             text='Frequency',
             category_orders={'<b>Theme<b>': ["Sound as Artefact", "Sound as Art", 
                                        "Sound as Lecturing", "Sound as Ambiance/Soundtrack", 
                                        "Sound as Crowd Curation"]})

fig.update_layout(
    title={'text': '<b>Top 5 Keywords for Each Sound Theme</b>', 'x': 0.5, 'xanchor': 'center'},
    font=dict(family="Times New Roman"),
    xaxis_title="<b>Keywords<b>",
    yaxis_title="<b>Frequency<b>"
)

# Show the plot
fig.show()

