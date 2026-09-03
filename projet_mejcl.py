from flask import Flask, render_template

projet_mejcl = Flask(__name__)

@projet_mejcl.route("/")
def page():
    return render_template("index.html")
    
if __name__ == "__main__":
    projet_mejcl.run(debug=True)
