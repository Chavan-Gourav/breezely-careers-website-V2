from flask import Flask , render_template, request, abort
from database import load_jobs_from_db, load_job_from_db, add_application_to_db


app = Flask(__name__)



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


@app.route('/job/<id>/apply', methods=['POST']) 
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    # store this in the DB
    # send an eamil
    # display acknowledgment 
    return render_template('application_submitted.html', application=data, job=job)
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

