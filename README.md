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

```bash
.
├── app/                           # 后端主程序目录
│   ├── core/                      # 核心基础模块
│   │   ├── config.py             # 应用配置类
│   │   ├── security.py           # 安全相关工具(JWT等)
│   │   └── logging.py            # 日志配置
│   │
│   ├── routes/                  # API路由层
│   │   ├── user_router.py       # 用户相关路由
│   │   ├── schedule_router.py   # 排班路由
│   │   ├── borrow_router.py     # 借用管理路由
│   │   ├── item_router.py       # 物品路由
│   │   ├── duty_router.py       # 值班路由
│   │   ├── message_router.py    # 消息路由
│   │   ├── xiumi_router.py      # 秀米路由
│   │   ├── cleaning_router.py   # 打扫路由
│   │   ├── competition_router.py # 比赛路由
│   │   ├── venue_router.py      # 场地路由
│   │   ├── task_router.py       # 任务路由
│   │   ├── printer_router.py    # 打印机路由
│   │   ├── project_router.py    # 项目路由
│   │   ├── event_router.py      # 事件路由
│   │   └── regulation_router.py # 制度路由
│   │
│   ├── models/                   # 数据库模型
│   │   ├── base_model.py        # 基础模型类（所有模型的基类）
│   │   ├── user_model.py        # 用户模型
│   │   ├── schedule_model.py    # 排班模型
│   │   ├── borrow_record_model.py      # 借用记录模型
│   │   ├── item_model.py        # 物品模型
│   │   ├── duty_apply_model.py  # 值班申请模型
│   │   ├── duty_record_model.py # 值班记录模型
│   │   ├── message_model.py     # 消息模型
│   │   ├── xiumi_model.py       # 秀米模型
│   │   ├── cleaning_model.py    # 打扫模型
│   │   ├── competition_model.py # 比赛模型
│   │   ├── venue_borrow_model.py # 场地借用模型
│   │   ├── task_model.py        # 任务模型
│   │   ├── printer_model.py     # 打印机模型
│   │   ├── project_model.py     # 项目模型
│   │   ├── event_model.py       # 事件模型
│   │   └── regulation_model.py  # 规章制度模型
│   │
│   ├── schemas/                 # 数据验证层
│   │   ├── user_schemas.py      # 用户相关DTO
│   │   ├── schedule_schemas.py  # 排班相关DTO
│   │   ├── borrow_record_schemas.py    # 借用记录DTO
│   │   ├── item_schemas.py      # 物品管理DTO
│   │   ├── duty_apply_schemas.py # 值班申请DTO
│   │   ├── duty_record_schemas.py # 值班记录DTO
│   │   ├── message_schemas.py   # 消息系统DTO
│   │   ├── xiumi_schemas.py     # 秀米系统DTO
│   │   ├── cleaning_schemas.py  # 打扫管理DTO
│   │   ├── competition_schemas.py # 比赛管理DTO
│   │   ├── venue_borrow_schemas.py # 场地借用DTO
│   │   ├── task_schemas.py      # 任务管理DTO
│   │   ├── printer_schemas.py   # 打印机管理DTO
│   │   ├── project_schemas.py   # 项目管理DTO
│   │   ├── event_schemas.py     # 事件管理DTO
│   │   └── regulation_schemas.py # 规章制度DTO
│   │
│   ├── services/                # 业务逻辑层
│   │   ├── user_service.py      # 用户服务
│   │   ├── schedule_service.py  # 排班服务
│   │   ├── borrow_service.py    # 借用管理服务
│   │   ├── item_service.py      # 物品管理服务
│   │   ├── duty_service.py      # 值班管理服务
│   │   ├── message_service.py   # 消息服务
│   │   ├── xiumi_service.py     # 秀米服务
│   │   ├── cleaning_service.py  # 打扫服务
│   │   ├── competition_service.py # 比赛服务
│   │   ├── venue_service.py     # 场地服务
│   │   ├── task_service.py      # 任务服务
│   │   ├── printer_service.py   # 打印机服务
│   │   ├── project_service.py   # 项目服务
│   │   ├── event_service.py     # 事件服务
│   │   └── regulation_service.py # 制度服务
│   │
│   ├── utils/                    # 工具模块
│   │   ├── minio_client.py       # MinIO客户端封装
│   │   ├── mongo_utils.py        # MongoDB工具
│   │   └── datetime_utils.py     # 时间处理工具
│   │
│   ├── middleware/               # 中间件目录
│   │   └── auth_middleware.py    # 鉴权中间件
│   │
│   ├── main.py                   # FastAPI入口文件
│   └── dependencies.py           # 依赖注入配置
│
├── nginx/                        # Nginx配置
│   ├── nginx.conf                # 主配置文件
│   └── conf.d/                   # 扩展配置目录
│       └── society.conf          # 应用专属配置
│
├── tests/                        # 测试套件
│   ├── unit/                     # 单元测试
│   │   ├── test_members.py
│   │   └── test_activities.py
│   │
│   ├── integration/              # 集成测试
│   └── conftest.py               # 测试配置
│
├── scripts/                      # 运维脚本
│   ├── backup/                   # 备份脚本
│   │   ├── mongo_backup.sh
│   │   └── minio_backup.sh
│   │
│   └── maintenance/             # 维护脚本
│       ├── cleanup_logs.sh
│       └── health_check.py
│
├── docs/                         # 文档目录
│   ├── api_docs/                # OpenAPI生成的文档
│   └── architecture.md          # 架构设计文档
│
├── docker/                       # Docker相关文件
│   ├── mongo/                   # MongoDB初始化脚本
│   │   └── init.js
│   └── minio/                   # MinIO初始化配置
│
├── .env.example                 # 环境变量示例文件
├── .gitignore                   # Git忽略规则
├── docker-compose.yml           # Docker编排配置
├── Dockerfile                   # 应用镜像构建文件
├── pyproject.toml               # Poetry依赖配置
├── poetry.lock                 # 精确依赖版本
├── requirements.txt            # 备用依赖清单
└── README.md                    # 项目说明文档

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

### 安装依赖

```bash
poetry install
poetry shell
```

### 运行测试

```bash
pytest tests/ --cov=app --cov-report=term-missing
```

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

## API文档

自动生成的OpenAPI文档包含以下主要接口：

### 成员管理

- `POST /members/`：创建新成员
- `GET /members/{id}`：获取成员详情
- `PUT /members/{id}`：更新成员信息

### 活动管理

- `POST /activities/`：创建新活动
- `GET /activities/`：获取活动列表
- `POST /activities/{id}/signup`：活动报名

### 文件管理

- `POST /files/upload`：文件上传
- `GET /files/{filename}`：文件下载

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

**维护提示**：

- 定期检查`/scripts/maintenance`目录中的维护脚本
- 生产环境建议启用HTTPS
- 敏感配置应通过保密管理方案处理
- 每日检查存储使用情况（MongoDB + MinIO）

根据实际部署环境需要调整配置参数，最新更新请参考代码注释。



现在的文件树（大改版）
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
└─ tests
   ├─ conftest.py
   ├─ integration
   └─ unit
      └─ test_members.py

```