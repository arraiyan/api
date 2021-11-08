from flask import Flask , jsonify ,render_template
import main
app = Flask(__name__)

@app.route('/')
def entry_point():
    return jsonify(main.data())



@app.route('/live_progress')
def progress_page():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True,port=8000)
