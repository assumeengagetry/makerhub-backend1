这里是简化后的 `README.md`：

---

# 社团管理系统后端

[![GitHub License](https://img.shields.io/github/license/yourname/society-management)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

基于 FastAPI 的社团管理系统后端，支持微信小程序接入，提供完整的社团管理功能。

## 技术栈

- **Web框架**: FastAPI
- **数据库**: MongoDB
- **对象存储**: MinIO
- **Web服务器**: Nginx
- **包管理**: Poetry
- **部署**: Docker Compose
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
├─ app/          # 后端核心代码
│  ├─ models/    # 数据模型
│  ├─ routes/    # 路由定义
│  ├─ services/  # 服务层
│  ├─ schemas/   # 数据验证
│  ├─ core/      # 核心功能
|
├─ docker/       # Docker 配置
├─ nginx/        # Nginx 配置
├─ scripts/      # 运维脚本
└─ tests/        # 测试代码
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

### 使用 Docker 部署

```bash
# 启动所有服务
docker-compose up -d --build

# 查看运行状态
docker-compose ps

# 停止服务
docker-compose down
```

服务启动后访问：

- API文档：`https://your-domain.com/docs`
- MinIO控制台：`http://localhost:9001` (默认账号：`minioadmin/minioadmin`)

## 配置说明

### 环境变量 (.env)

```ini
# MongoDB 配置
MONGO_URI=mongodb://mongo:27017
DATABASE_NAME=society_db

# MinIO 配置
MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=your-access-key
MINIO_SECRET_KEY=your-secret-key
MINIO_BUCKET=society-files

# 应用配置
SECRET_KEY=your-secret-key
TOKEN_EXPIRE_MINUTES=1440
```

### Nginx 配置

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://backend:8000;
    }

    location /minio/ {
        proxy_pass http://minio:9000/;
    }
}
```

## 开发指南

- 使用 **Black** 进行代码格式化
- 使用 **isort** 进行 import 排序
- 提交前运行 **pre-commit** 检查：

```bash
pre-commit install
```

## 备份与恢复

### MongoDB 备份

```bash
# 备份
docker exec mongo sh -c 'mongodump --db society_db --archive' > backup.dump

# 恢复
docker exec -i mongo sh -c 'mongorestore --archive' < backup.dump
```

### MinIO 备份

```bash
aws s3 sync s3://society-files ./minio-backup --endpoint-url http://localhost:9000
```

## 日志管理

日志按天滚动保存，路径：`/var/log/society-manager/`

```python
from loguru import logger

logger.add("/var/log/society-manager/app.log", rotation="00:00", retention="30 days", compression="zip")
```

## 贡献指南

1. Fork 仓库并创建特性分支
2. 提交前运行测试
3. 更新文档
4. 创建 Pull Request

## 许可证

[MIT License](LICENSE)

---
