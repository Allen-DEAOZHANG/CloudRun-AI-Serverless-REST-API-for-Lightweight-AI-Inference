# Dummy model for sentiment classification
# Replace with HuggingFace or TensorFlow Lite model for real deployment

def predict(text: str):
    if "good" in text.lower():
        return "positive", 0.92
    elif "bad" in text.lower():
        return "negative", 0.87
    else:
        return "neutral", 0.55
