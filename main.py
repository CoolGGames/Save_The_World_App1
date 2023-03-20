from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/3rs')
def next_page():
    return render_template('3rs.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    contactno = request.form['contactno']
    aspiration = request.form['aspiration']
    
    return 'Thanks for submitting the form!'

if __name__ == '__main__':
    app.run(debug=True)
