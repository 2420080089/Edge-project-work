The Fake News Detector (Edge - Python) is a lightweight machine learning project designed to identify whether a news article is real or fake. It uses basic Natural Language Processing (NLP) techniques and a simple classification model, making it efficient enough to run on edge devices like laptops, low-power systems, or embedded platforms.

This project converts news text into numerical features using TF-IDF vectorization and then applies a Logistic Regression model to classify the content. Unlike heavy AI models, this approach ensures fast performance, low memory usage, and offline capability, which are essential for edge computing environments.

The system is easy to use and customizable—users can train it with their own datasets, improve accuracy, and extend it into web or mobile applications. While it provides a good starting point for fake news detection, its effectiveness depends on the quality and size of the training data.

⚡ Features
Lightweight (edge-device friendly)
Fast prediction
Works offline
Easy to modify

⚠️ Limitations
Small dataset → lower accuracy
Cannot fully detect sarcasm or satire
Needs better data for real-world use

🔧 Future Improvements
Add web interface using Flask
Use larger dataset
Improve NLP preprocessing
Deploy on Raspberry Pi / mobile
