import pickle

from fastapi import FastAPI
app = FastAPI()  # <-- ini HARUS ada

# Load model dan vectorizer
with open('naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Teks baru untuk prediksi
teks_baru = ["efisiensi anggaran bagus sekali"]
fitur_baru = tfidf.transform(teks_baru)
prediksi = model.predict(fitur_baru)

print("Prediksi Sentimen:", prediksi[0])  # Misal: 1 (positif)