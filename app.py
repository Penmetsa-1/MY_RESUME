from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

# Optional: handle unwanted 404 error from browser extensions or scripts
@app.route('/hybridaction/zybTrackerStatisticsAction')
def block_weird_tracker():
    return {}, 200

if __name__ == '__main__':
    app.run(debug=True)
