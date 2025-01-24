#Author: Hana Arshid, topic: bigrams/sonic strategies #date: 20/01/2025

import pandas as pd
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter
import plotly.express as px

nltk.download('punkt')
nltk.download('stopwords')

file_path = '/Users/hanairshaid/Desktop/Wonder Cabinet - Instagram Posts.xlsx'

df = pd.read_excel(file_path)

posts = df.iloc[:, 2].dropna().astype(str).tolist()

text = " ".join(posts)

tokens = nltk.word_tokenize(text.lower())

stop_words = set(stopwords.words('english'))

exclude_words = stop_words.union({
    "sawa", "sound", "music", "around", "am", "pm", "january", "february", "march", "april", "may", "june", 
    "july", "august", "september", "october", "november", "december", "monday", "tuesday", "wednesday", 
    "thursday", "friday", "saturday", "sunday", "wonder", "cabinet", "areej", "ashhab", "dina", "shilleh", 
    "khalil", "sakakini", "elias", "halabi", "le", "guess", "supported", "french", "cultural", 
    "part", "proceeds", "cordially", "invites", "joined", "performance", "attend", 
    "laurence", "sammour", "ramallah", "center", "bethlehem", "workshop", "participants",
    "radio", "al", "hara", "sary", "moussa", "musicians", "moussa", "abed", 
    "english", "subtitles", "kobeissy"
})

tokens = [word for word in tokens if word.isalpha() and word not in exclude_words]

bigrams = ngrams(tokens, 2)

bigram_freq = Counter(bigrams)

top_bigrams = bigram_freq.most_common(20)

bigram_labels = [' '.join(bigram) for bigram, _ in top_bigrams]
frequencies = [freq for _, freq in top_bigrams]

bigram_df = pd.DataFrame({
    'Bigram': bigram_labels,
    'Frequency': frequencies
})

fig = px.bar(bigram_df, 
             x='Bigram', 
             y='Frequency', 
             title='<b>Top 20 Most Frequent Bigrams Associated with Sound and Music<b>',
             labels={'Bigram': 'Bigrams', 'Frequency': 'Frequency'},
             color='Frequency', 
             color_continuous_scale='Viridis')

fig.update_layout(
    title_font=dict(family='Times New Roman', size=24),
    title_x=0.5,
    font=dict(family='Times New Roman', size=12),
    xaxis_title='<b>Bigrams<b>',
    yaxis_title='<b>Frequency<b>',
    xaxis_tickangle=-45,
    showlegend=False
)

fig.write_html('bigram_visualisation.html')

print("figure has been saved as bigram_visualisation.html")
