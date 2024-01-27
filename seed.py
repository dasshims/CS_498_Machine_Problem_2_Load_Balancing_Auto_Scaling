from flask import Flask, request
import json

app = Flask(__name__)
seed_num = "100"

@app.route("/", methods=["GET", "POST"])
def serve():
    if request.method == 'POST':
        payload = json.loads(request.get_data())
        global seed_num
        print(f"seed number before {seed_num}")
        seed_num = payload['num']
        return f"seed number updated to {seed_num}"

    if request.method == 'GET':
        print("Inside get")
        return f"seed value is {seed_num}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)