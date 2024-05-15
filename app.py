from flask import Flask, request, jsonify, send_file
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torch
import os
from gtts import gTTS

app = Flask(__name__)

# Đường dẫn đến các mô hình .pth của bạn
MODEL_PATHS = {
    "model1": "path_to_model1.pth",
    "model2": "path_to_model2.pth",
    "model3": "path_to_model3.pth"
}

# Load các mô hình vào bộ nhớ
models = {}
tokenizers = {}

for model_name, model_path in MODEL_PATHS.items():
    model = torch.load(model_path)
    tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    models[model_name] = Wav2Vec2ForCTC.from_pretrained(model)
    tokenizers[model_name] = tokenizer

@app.route('/generate', methods=['POST'])
def generate_speech():
    data = request.get_json()
    model_name = data.get("model")
    text = data.get("text")

    if model_name not in models:
        return jsonify({"error": "Model not found"}), 404

    if not text:
        return jsonify({"error": "Text is required"}), 400

    model = models[model_name]
    tokenizer = tokenizers[model_name]

    # Chuyển đổi văn bản thành giọng nói (ở đây dùng Google Text-to-Speech như ví dụ)
    tts = gTTS(text)
    audio_path = "output.mp3"
    tts.save(audio_path)

    return send_file(audio_path, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
