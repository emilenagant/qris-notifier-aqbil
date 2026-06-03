from flask import Flask, request, jsonify

app = Flask(__name__)

latest_transaction = {"amount": 0, "name": "", "has_new": False}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook masuk:", data)
    latest_transaction["amount"] = data.get("amount_raw", 0)
    latest_transaction["name"]   = data.get("donator_name", "Seseorang")
    latest_transaction["has_new"] = True
    return jsonify({"status": "ok"}), 200

@app.route("/check", methods=["GET"])
def check():
    if latest_transaction["has_new"]:
        latest_transaction["has_new"] = False
        return jsonify({
            "has_transaction": True,
            "amount": latest_transaction["amount"],
            "name": latest_transaction["name"]
        })
    return jsonify({"has_transaction": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
