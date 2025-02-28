from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite 데이터베이스 설정
app.config['SECRET_KEY'] = 'your_secret_key'  # 세션을 위한 비밀 키 설정
db = SQLAlchemy(app)

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

# 사용자 목록 페이지
@app.route('/')
def index():
    users = User.query.all()  # 모든 사용자 조회
    return render_template('index.html', users=users)

# 사용자 추가 페이지
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        # 새로운 사용자 추가
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_user.html')

# 사용자 수정 페이지
@app.route('/edit/<username>', methods=['GET', 'POST'])
def edit_user(username):
    user = User.query.filter_by(username=username).first()  # 수정할 사용자 찾기
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_user.html', user=user)

# 사용자 삭제 페이지
@app.route('/delete/<username>', methods=['GET', 'POST'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()  # 삭제할 사용자 찾기
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    db.create_all()  # 테이블 생성
    app.run(debug=True)

