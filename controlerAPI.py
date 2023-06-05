from flask import Flask, jsonify, request
import privateGPT

app = Flask(__name__)


# GET request to retrieve all data
@app.route('/api/health', methods=['GET'])
def get_data():
    return jsonify("I'm UP nd Runing")

# POST request to add new data
@app.route('/api/query', methods=['POST'])
def add_data():
    new_item = request.get_json()
    message=privateGPT.printResult(new_item["query"])
    return jsonify({"message": message})

if __name__ == '__main__':
    privateGPT.invockModel()
    app.run(host='0.0.0.0')
