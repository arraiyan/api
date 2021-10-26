from flask import Flask , jsonify
import main
app = Flask(__name__)

@app.route('/')
def entry_point():
    return jsonify(main.data())

if __name__ == '__main__':
    app.run(debug=False)
