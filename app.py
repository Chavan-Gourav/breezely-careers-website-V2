from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample job data
    Jobs = [
        {'title': 'Data Analyst', 'location': 'Bengaluru, India', 'salary': 'Rs. 10,00,000'},
        {'title': 'Data Scientist', 'location': 'Delhi, India', 'salary': 'Rs. 15,00,000'},
        {'title': 'Frontend Engineer', 'location': 'Remote'},
        {'title': 'Backend Engineer', 'location': 'San Francisco, USA', 'salary': '$120,000'}
    ]

    # Render home.html and pass the job data
    return render_template('home.html', jobs=Jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
