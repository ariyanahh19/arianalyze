import pickle

from fastapi import FastAPI
app = FastAPI()  # <-- ini HARUS ada

# Load model dan vectorizer
with open('naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)


@app.post("/predict_sentiment/")
async def predict_sentiment(teks_baru: str):
    fitur_baru = tfidf.transform([teks_baru])
    prediksi = model.predict(fitur_baru)
    sentiment = prediksi[0]
    return {"sentiment": sentiment}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)