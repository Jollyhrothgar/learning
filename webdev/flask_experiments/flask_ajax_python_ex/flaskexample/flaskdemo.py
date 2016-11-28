from flaskexample import app
from flask import Flask, jsonify, render_template, request
 
@app.route('/')
def index():
    page_structure = [
        {
            'element_id':'submitBtn3',
            'input_name':'echoText3',
            'input_id':'echoText3',
            'result_id':'echoResult3',
        },
        {
            'element_id':'submitBtn2',
            'input_name':'echoText2',
            'input_id':'echoText2',
            'result_id':'echoResult2',
        },
    ]
    for element in page_structure:
        print(element['element_id'])
    return render_template('index.html',page_structure=page_structure)

@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')}
    print(ret_data)
    return jsonify(ret_data)
