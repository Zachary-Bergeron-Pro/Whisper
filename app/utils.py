import whisper

# Load the model once, at the module level, to avoid reloading on each request
model = whisper.load_model("base")  # Consider using a smaller model to save resources

def transcribe_audio(filepath):
    result = model.transcribe(filepath)
    return result["text"]
