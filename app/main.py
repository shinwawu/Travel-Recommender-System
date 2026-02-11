# app/main.py
import pandas as pd
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Global variables
rec_engine = None
DATA_PATH = os.path.join("data", "hotels_brazil.csv")


# Basic ML Recommender System -> Content Based + Vector Search
class HotelRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

        self.df["content"] = (
            self.df["city"]
            + " "
            + self.df["neighborhood"]
            + " "
            + self.df["amenities"]
            + " "
            + self.df["description"]
        )

        # Vectorization
        self.tfidf = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.tfidf.fit_transform(self.df["content"])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, hotel_id: int, top_n: int = 4):
        if hotel_id not in self.df["id"].values:
            return []
        idx = self.df[self.df["id"] == hotel_id].index[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        hotel_indices = [i[0] for i in sim_scores[1 : top_n + 1]]
        return self.df.iloc[hotel_indices].to_dict(orient="records")

    def get_all_hotels(self):
        return self.df.to_dict(orient="records")


@asynccontextmanager
async def lifespan(app: FastAPI):

    global rec_engine
    rec_engine = HotelRecommender(DATA_PATH)
    yield


# API
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Endpoints
@app.get("/hotels")
def get_hotels():
    return rec_engine.get_all_hotels()


@app.get("/recommend/{hotel_id}")
def recommend(hotel_id: int):
    recs = rec_engine.get_recommendations(hotel_id)
    if not recs:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return recs
