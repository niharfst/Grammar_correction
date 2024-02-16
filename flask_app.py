from flask import Flask, render_template, request
from transformers import MT5ForConditionalGeneration, AutoTokenizer

app = Flask(__name__)

# Load the model and tokenizer
model = MT5ForConditionalGeneration.from_pretrained(r"mT5-\mT5-ep19-20240216T113959Z-001")
tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():
    if request.method == 'POST':
        # Get the input sentence from the form
        input_sentence = request.form['sentence']

        # Tokenize the input sentence
        inputs = tokenizer(input_sentence, return_tensors="pt")

        # Generate corrected sentence
        corrected_output = tokenizer.batch_decode(model.to('cpu').generate(inputs.input_ids, max_length=50), skip_special_tokens=True)[0]

        return render_template('result.html', input_sentence=input_sentence, corrected_output=corrected_output)

if __name__ == '__main__':
    app.run(debug=True)
