from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs.10.000.000,00'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Dehli, India',
  'salary': 'Rs.15.000.000,00'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Fransisco, USA',
  'salary': '$150,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='EZ')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
