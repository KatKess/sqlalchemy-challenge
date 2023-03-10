from flask import Flask,jsonify

app = Flask(__name__)

hello_dict = {"Hello": "World"}

@app.route("/")
def home():
    return "Hi"

@app.route("/normal")
def normal():
    return hello_dict

@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)

If __name__"_main_":
    app.run(debug=True)
    