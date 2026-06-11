import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/')
def home():
    return render_template('index.html')
'''
@app.route('/predict',methods=['POST'])
def predict():
    
    #for rendering result on html GUI
    
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)

    output=round(prediction[0],2)
    return render_template('index.html',prediction_text="Employee salary should be $ {}".format(output))
'''

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering result on HTML GUI
    '''
    try:
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text="Employee salary should be $ {}".format(output))
    except ValueError:
        return render_template('index.html', prediction_text="Invalid input. Please enter numeric values.")
    except Exception as e:
        return render_template('index.html', prediction_text="Something went wrong. Please try again.")
    
    

@app.route('/predict_api',methods=['POST'])

def predict_api():
    '''
    For direct API calls request
    '''
    data=request.get_json(force=True)
    # Input validation
    required_fields = ['experience', 'test_score', 'interview_score']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    if not (0 <= data['experience'] <= 20):
        return jsonify({'error': 'experience must be between 0 and 20'}), 400
    if not (1 <= data['test_score'] <= 10):
        return jsonify({'error': 'test_score must be between 1 and 10'}), 400
    if not (1 <= data['interview_score'] <= 10):
        return jsonify({'error': 'interview_score must be between 1 and 10'}), 400
    prediction=model.predict([np.array(list(data.values()))])
    output=prediction[0]
    return jsonify(output)

if __name__=="__main__":
    app.run(debug=True)

