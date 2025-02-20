# 社团管理系统后端

[![GitHub License](https://img.shields.io/github/license/yourname/society-management)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

基于FastAPI的社团管理系统后端，支持微信小程序接入，提供完整的社团管理功能。

## 技术栈

- **Web框架**: FastAPI
- **数据库**: MongoDB 5.0+
- **对象存储**: MinIO
- **Web服务器**: Nginx
- **包管理**: Poetry
- **部署方式**: Docker Compose
- **日志系统**: Loguru
- **API文档**: Swagger UI/ReDoc

## 系统架构

```
client -> Nginx -> FastAPI -> MongoDB
                   │
                   └-> MinIO
```

## 目录结构
```
makerhub-backend1
├─ app
│  ├─ core
│  │  ├─ auth.py
│  │  ├─ config.py
│  │  ├─ db.py
│  │  ├─ logging.py
│  │  ├─ utils.py
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ models
│  │  ├─ b6orrow_stuff_model.py
│  │  ├─ base_model.py
│  │  ├─ c10ompetition_model.py
│  │  ├─ c13leaning_model.py
│  │  ├─ d11uty_apply_model.py
│  │  ├─ d12uty_model.py
│  │  ├─ e4vent_model.py
│  │  ├─ m15essage_model.py
│  │  ├─ p3rinter_model.py
│  │  ├─ p9roject_model.py
│  │  ├─ r17esource.py
│  │  ├─ r2egulation_model.py
│  │  ├─ s14chedule_model.py
│  │  ├─ s7tuff_model.py
│  │  ├─ t5ask_model.py
│  │  ├─ u1ser_model.py
│  │  ├─ v8enue_borrow_model.py
│  │  └─ x16iumi_model.py
│  ├─ routes
│  │  ├─ 10competition_router.py
│  │  ├─ 11duty_apply_router.py
│  │  ├─ 12duty_router.py
│  │  ├─ 13cleaning_router.py
│  │  ├─ 14schedule_router.py
│  │  ├─ 15message_router.py
│  │  ├─ 16xiumi_router.py
│  │  ├─ 17resource_router.py
│  │  ├─ 1user_router.py
│  │  ├─ 2regulation_router.py
│  │  ├─ 3printer_router.py
│  │  ├─ 4event_router.py
│  │  ├─ 5task_router.py
│  │  ├─ 6borrow_stuff_router.py
│  │  ├─ 7stuff_router.py
│  │  ├─ 8venue_router.py
│  │  └─ 9project_router.py
│  ├─ schemas
│  │  ├─ 10competition_schemas.py
│  │  ├─ 11duty_apply_schemas.py
│  │  ├─ 12duty_schemas.py
│  │  ├─ 13cleaning_schemas.py
│  │  ├─ 14schedule_schemas.py
│  │  ├─ 15message_schemas.py
│  │  ├─ 16xiumi_schemas.py
│  │  ├─ 1user_schemas.py
│  │  ├─ 2regulation_schemas.py
│  │  ├─ 3printer_schemas.py
│  │  ├─ 4event_schemas.py
│  │  ├─ 5task_schemas.py
│  │  ├─ 6borrow_stuff_schemas.py
│  │  ├─ 7stuff_schemas.py
│  │  ├─ 8venue_borrow_schemas.py
│  │  └─ 9project_schemas.py
│  └─ services
│     ├─ 10competition_service.py
│     ├─ 12duty_service.py
│     ├─ 13cleaning_service.py
│     ├─ 14schedule_service.py
│     ├─ 15message_service.py
│     ├─ 16xiumi_service.py
│     ├─ 1user_service.py
│     ├─ 2regulation_service.py
│     ├─ 3printer_service.py
│     ├─ 4event_service.py
│     ├─ 5task_service.py
│     ├─ 6borrow_stuff_service.py
│     ├─ 7stuff_service.py
│     ├─ 8venue_borrow_service.py
│     └─ 9project_service.py
├─ docker
│  ├─ minio
│  └─ mongo
│     └─ init.js
├─ docker-compose.yml
├─ Dockerfile
├─ nginx
│  ├─ conf.d
│  │  └─ society.conf
│  └─ nginx.conf
├─ poetry.lock
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ scripts
│  ├─ backup
│  │  ├─ minio_backup.sh
│  │  └─ mongo_backup.sh
│  └─ maintenance
│     ├─ cleanup_logs.sh
│     └─ health_check.py
tests
   ├─ conftest.py
   ├─ integration/
+  │  ├─ test_auth.py
+  │  ├─ test_file_upload.py
+  │  └─ test_user_flow.py
   └─ unit/
+     ├─ services/
+     │  ├─ test_user_service.py
+     │  └─ test_stuff_service.py
+     ├─ models/
+     │  ├─ test_user_model.py
+     │  └─ test_borrow_model.py
      └─ test_members.py

```

```
app/

模型层：每个业务模型独立文件，命名遵循[业务]_model.py格式

验证层：每个模型对应独立schema文件，处理输入输出验证

服务层：每个业务领域独立服务，复杂业务逻辑在此实现

路由层：按业务模块划分路由，保持接口粒度清晰

nginx/

包含反向代理和负载均衡配置

独立配置文件便于不同环境切换

tests/

单元测试与集成测试分离

使用pytest fixtures统一管理测试依赖

scripts/

标准化运维操作脚本

备份脚本支持定时任务调用

docker/

数据库初始化脚本保证服务启动时自动配置

独立目录存放各服务的Docker相关配置

docs/

包含自动生成的API文档和设计文档

推荐使用mkdocs维护项目文档
```




## 快速开始

### 环境准备

1. 安装依赖工具：

```bash
curl -sSL https://install.python-poetry.org | python3 -
pip install --user poetry
sudo apt-get install docker docker-compose
```

2. 复制环境文件：

```bash
cp .env.example .env
```

### 使用Docker部署

```bash
# 启动所有服务
docker-compose up -d --build

# 查看运行状态
docker-compose ps

# 停止服务
docker-compose down
```

服务启动后访问：

- API文档：https://your-domain.com/docs
- MinIO控制台：http://localhost:9001 (默认账号：minioadmin/minioadmin)

## 配置说明

### 环境变量(.env)

```ini
# MongoDB
MONGO_URI=mongodb://mongo:27017
DATABASE_NAME=society_db

# MinIO
MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=your-access-key
MINIO_SECRET_KEY=your-secret-key
MINIO_BUCKET=society-files

# 应用配置
SECRET_KEY=your-secret-key
TOKEN_EXPIRE_MINUTES=1440
```

### Nginx配置

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /minio/ {
        proxy_pass http://minio:9000/;
        proxy_set_header Host $http_host;
    }
}
```

## 开发指南

### 代码规范

- 使用Black进行代码格式化
- 使用isort进行import排序
- 提交前运行pre-commit检查：

```bash
pre-commit install
```

## 备份与恢复

### MongoDB备份

```bash
# 备份
docker exec mongo sh -c 'mongodump --db society_db --archive' > backup.dump

# 恢复
docker exec -i mongo sh -c 'mongorestore --archive' < backup.dump
```

### MinIO备份

建议使用AWS S3兼容工具：

```bash
aws s3 sync s3://society-files ./minio-backup --endpoint-url http://localhost:9000
```

## 日志管理

日志文件按天滚动保存，路径：`/var/log/society-manager/`

```python
# 示例日志配置
from loguru import logger

logger.add(
    "/var/log/society-manager/app.log",
    rotation="00:00",  # 每天滚动
    retention="30 days",  # 保留30天
    compression="zip"
)
```

## 贡献指南

1. Fork仓库并创建特性分支
2. 提交代码前运行测试套件
3. 更新相关文档
4. 创建Pull Request

## 许可证

[MIT License](LICENSE)

---
