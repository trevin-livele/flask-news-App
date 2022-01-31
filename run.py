from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    base_url = "https://newsapi.org/v2/everything?q=Apple&from=2022-01-26&sortBy=popularity&apiKey=ffb788ce77dc47d3aa4d36f8cccc8f43"

    data = requests.get(base_url).json()
    print(type(data))
    return render_template("index.html", data=[data])

if __name__ == "__main__":
    app.run(debug=True)
