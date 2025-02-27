# posts.py 파일 내용 정의
posts_content = """\
from flask import Blueprint, jsonify, request

posts_bp = Blueprint('posts', __name__)

# 게시글 데이터 (임시로 메모리에서 관리)
posts = [
    {'id': 1, 'title': '첫 번째 게시글', 'content': '내용 1'},
    {'id': 2, 'title': '두 번째 게시글', 'content': '내용 2'}
]

@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@posts_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    return jsonify(post) if post else ('', 404)

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

@posts_bp.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if not post:
        return ('', 404)
    updated_data = request.get_json()
    post.update(updated_data)
    return jsonify(post)

@posts_bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return ('', 204)
"""

# posts.py 파일로 저장
with open('/mnt/data/posts.py', 'w') as file:
    file.write(posts_content)

"/mnt/data/posts.py"

