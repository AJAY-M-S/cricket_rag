# retriever.py
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import os

def preprocess_data():
    df = pd.read_csv("data/match_info_data.csv")

    formatted_texts = []

    for _, row in df.iterrows():
        match_id = row['id']
        season = row['season']
        city = row['city']
        team1 = row['team1']
        team2 = row['team2']
        winner = row['winner']
        player_of_match = row['player_of_match']
        venue = row['venue']

        text = (
            f"Match ID: {match_id} | "
            f"Teams: {team1} vs {team2} | "
            f"Winner: {winner} | "
            f"Player of Match: {player_of_match} | "
            f"Venue: {venue} | "
            f"City: {city} | "
            f"Season: {season}"
        )

        formatted_texts.append(text)

    return formatted_texts

def build_faiss(texts):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(embeddings)

    os.makedirs("faiss_store", exist_ok=True)
    faiss.write_index(index, "faiss_store/cricket.index")
    with open("faiss_store/texts.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(texts))

if __name__ == "__main__":
    texts = preprocess_data()
    build_faiss(texts)
