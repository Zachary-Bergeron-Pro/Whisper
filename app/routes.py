from flask import Blueprint, request, jsonify, render_template
import os
from app.utils import transcribe_audio

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        
        try:
            transcription = transcribe_audio(filepath)
            return jsonify({'transcription': transcription})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            os.remove(filepath)
