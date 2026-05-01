import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_news(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)
    return prediction[0]

if __name__ == "__main__":
    while True:
        text = input("Enter news text (or type 'exit'): ")
        if text.lower() == 'exit':
            break
        print("Prediction:", predict_news(text))
