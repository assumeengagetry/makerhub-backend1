from flask import Blueprint, request, jsonify
from app.models.project_model import Project
from datetime import datetime

project_bp = Blueprint('project', __name__)

@project_bp.route('/project', methods=['POST'])
def create_project():
    data = request.get_json()
    try:
        project = Project(
            apply_id=data['apply_id'],
            project_name=data['project_name'],
            director=data['director'],
            college=data['college'],
            major_grade=data['major_grade'],
            phone_num=data['phone_num'],
            email=data['email'],
            mentor=data['mentor'],
            description=data.get('description', ''),
            application_file=data.get('application_file', ''),
            prove_file=data.get('prove_file', ''),
            member=data.get('member', []),
            start_time=datetime.strptime(data['start_time'], '%Y-%m-%d'),
            end_time=datetime.strptime(data['end_time'], '%Y-%m-%d')
        ).save()
        return jsonify({'message': '项目创建成功', 'id': str(project.id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@project_bp.route('/project/<apply_id>', methods=['GET'])
def get_project(apply_id):
    try:
        project = Project.objects(apply_id=apply_id).first()
        if project:
            return jsonify(project.to_dict()), 200
        return jsonify({'error': '项目不存在'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@project_bp.route('/project/<apply_id>', methods=['PUT'])
def update_project(apply_id):
    data = request.get_json()
    try:
        project = Project.objects(apply_id=apply_id).first()
        if not project:
            return jsonify({'error': '项目不存在'}), 404
            
        if 'audit_state' in data:
            project.audit_state = data['audit_state']
        if 'project_state' in data:
            project.project_state = data['project_state']
        
        project.save()
        return jsonify({'message': '项目更新成功'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@project_bp.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.objects()
        return jsonify([project.to_dict() for project in projects]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400