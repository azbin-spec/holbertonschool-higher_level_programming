#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

global users
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def jsoni():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<string:username>")
def usepart(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_users():
    data_user = request.json
    if data_user.get("username"):
        users[data_user["username"]] = data_user
        return jsonify({"message": "User added", "user": data_user}), 201
    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
