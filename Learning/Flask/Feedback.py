# BackEnd

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Feedback Form"

@app.route('/feedback')
def feedback():
    return render_template('feedback_form.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    data = request.json 
    print(data)

    ## Save data to a file or process as needed
    with open('feedback_data.txt', 'a') as file:
        file.write(json.dumps(data) + '\n')

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
