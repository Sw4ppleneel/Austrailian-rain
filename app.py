from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def main():
    if request.method == "POST" : 
        #Form being submitted 

        subject = request.form.get('subject')
        message = request.form.get('message')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 