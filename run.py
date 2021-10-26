from flask import Flask , jsonify
import main
app = Flask(__name__)

@app.route('/')
def entry_point():
    return jsonify({'holder':1552})

if __name__ == '__main__':
    app.run(debug=False)
