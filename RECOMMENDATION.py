
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv('ecommerce_data.csv')


data['description'] = data['description'].apply(lambda x: x.lower())

data['description'] = data['description'].apply(lambda x: x.split())


cv = CountVectorizer()
count_matrix = cv.fit_transform(data['description'])

cosine_sim = cosine_similarity(count_matrix)

def get_recommendations(product_name, cosine_sim=cosine_sim):
    idx = data[data['product_name'] == product_name].index[0] 
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    product_indices = [i[0] for i in sim_scores]
    return data['product_name'].iloc[product_indices]

print(get_recommendations('product_name_1'))