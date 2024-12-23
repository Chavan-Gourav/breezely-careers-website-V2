from flask import Flask , render_template, jsonify, abort
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)



# Sample job data
jobs = load_jobs_from_db()
@app.route('/')
def hello_breezely(): 
    return render_template('home.html', jobs=jobs)



@app.route('/job/<int:id>') 
def show_job(id):
    job = load_job_from_db(id)
    if job is None:
        abort(404, description="Job not found")  
    return render_template('jobpage.html', job=job)





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

