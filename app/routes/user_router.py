# filepath: /society-management/society-management/app/routes/user_router.py

from flask import Blueprint, request, jsonify
from app.models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        if User.objects(userid=data['userid']).first():
            return jsonify({'error': '用户已存在'}), 400
            
        user = User(
            userid=data['userid'],
            password=generate_password_hash(data['password']),
            real_name=data['real_name'],
            phone_num=data['phone_num'],
            level=data.get('level', 1)
        ).save()
        return jsonify({'message': '注册成功', 'id': str(user.id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = User.objects(userid=data['userid']).first()
        if user and check_password_hash(user.password, data['password']):
            return jsonify({
                'message': '登录成功',
                'user': {
                    'userid': user.userid,
                    'real_name': user.real_name,
                    'level': user.level
                }
            }), 200
        return jsonify({'error': '用户名或密码错误'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/user/<userid>', methods=['PUT'])
def update_user(userid):
    data = request.get_json()
    try:
        user = User.objects(userid=userid).first()
        if not user:
            return jsonify({'error': '用户不存在'}), 404
            
        if 'real_name' in data:
            user.real_name = data['real_name']
        if 'phone_num' in data:
            user.phone_num = data['phone_num']
        if 'level' in data:
            user.level = data['level']
        if 'state' in data:
            user.state = data['state']
        
        user.save()
        return jsonify({'message': '用户信息更新成功'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400