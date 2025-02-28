from flask import Flask, jsonify, request

app = Flask(__name__)

# 간단한 사용자 데이터 저장 (메모리 리스트 활용)
users = {
    "admin": "admin123",
    "guest": "guest123"
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = password
    return jsonify({"message": "User added successfully"})

@app.route('/edit/<username>', methods=['PUT'])
def edit_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    new_password = data.get("password")
    if not new_password:
        return jsonify({"error": "New password required"}), 400
    users[username] = new_password
    return jsonify({"message": "User updated successfully"})

@app.route('/delete/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    del users[username]
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

