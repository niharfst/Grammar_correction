# Sentence Correction Flask App
This is a simple Flask web application that uses a pre-trained model to correct sentences. Users can input a sentence, and the application will provide the corrected version of the input sentence.

## Requirements
Python 3.x

Flask

Hugging Face Transformers Library

## Download The model and Install requirements

1. Download the model from following url  https://drive.google.com/drive/folders/16F9C0hkd57HRhd_-VuEQUTPoV0LDZbJK?usp=sharing
2. Rename the folder name in the `MT5ForConditionalGeneration.from_pretrained('folder path here')`.
3. Install the requirements `pip install -r requirements.txt`.
4. You can see the generated results here `mT5-results-ep29.txt`.
5. To run the flask app `python flask_app.py`.
