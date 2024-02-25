from flask import Flask, request, jsonify
import google.generativeai as genai  # Import necessary libraries

app = Flask(__name__)
genai.configure(api_key="AIzaSyC2nVBDMs3vN9mhboxlY46WfWTcHjI1QdI")  # Replace with your actual API key
model = genai.GenerativeModel('gemini-pro')

@app.route('/generate_response', methods=['POST'])
def generate_response():
    try:
        prompt = request.json['prompt']
        response = model.generate_content(prompt)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
