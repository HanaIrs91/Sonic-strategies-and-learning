#Author: Hana Arshid #topic: cognitive and emotional experience #date: 20/01/2025
import pandas as pd
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import plotly.graph_objects as go


nltk.download('punkt')
nltk.download('stopwords')


file_path = '/Users/hanairshaid/Desktop/Wonder Cabinet - Instagram Posts.xlsx'


data = pd.read_excel(file_path)

text_column = "Post"  
documents = data[text_column].dropna().tolist()

full_text = " ".join(documents)

stop_words = set(stopwords.words("english"))
tokens = word_tokenize(full_text.lower())  
filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]

word_frequencies = Counter(filtered_words)

emotional_terms = [
    "emotional journey", "resilience", "resistance", "raw emotion", "tears", 
    "pain", "fears", "grief", "empathy", "despair", "lived experiences", "music therapy"
]

cognitive_terms = [
    "storytelling", "hands-on experimentation", "guided walks", "memory", 
    "cultural memory", "cultural narratives", "educational and cultural exchanges", 
    "raising awareness", "lived experiences", "music therapy"
]

emotional_frequencies = Counter()
cognitive_frequencies = Counter()

for term in emotional_terms:
    emotional_frequencies[term] = full_text.lower().count(term.lower())

for term in cognitive_terms:
    cognitive_frequencies[term] = full_text.lower().count(term.lower())

emotional_sorted = sorted(emotional_frequencies.items(), key=lambda x: x[1], reverse=True)
cognitive_sorted = sorted(cognitive_frequencies.items(), key=lambda x: x[1], reverse=True)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=[term[0] for term in emotional_sorted],  
    y=[term[1] for term in emotional_sorted], 
    name='Emotional Experience',
    marker_color='#EF553B',  
    textposition='inside',  
))

fig.add_trace(go.Bar(
    x=[term[0] for term in cognitive_sorted],  
    y=[term[1] for term in cognitive_sorted], 
    name='Cognitive Experience',
    marker_color='#AB63FA', 
    textposition='inside',  
))

fig.update_layout(
    title={
        'text': "<b>Word Frequencies by Emotional and Cognitive Experiences<b>",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 20, 'family': 'Times New Roman', 'color': 'black', 'weight': 'bold'}  # Bold title
    },
    xaxis_title="<b>Words<b>",
    yaxis_title="<b>Frequency<b>",
    barmode='group',
    template='plotly_white',
    legend_title="<b>Theme<b>",
    legend=dict(
        title="<b>Theme<b>",
        font=dict(family="Times New Roman", size=14, color="black"),
        tracegroupgap=0,
        orientation="v",  
        yanchor="top",
        y=1,
        xanchor="left",
        x=1  
    ),
    font=dict(family="Times New Roman", size=14, color="black")
)

# Show the plot
fig.show()
