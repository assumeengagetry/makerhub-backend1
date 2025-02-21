FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装 Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# 添加 Poetry 到环境变量中
ENV PATH="/root/.local/bin:${PATH}"

# 复制项目文件
COPY pyproject.toml poetry.lock ./

# 复制应用代码
COPY app/ ./app/

# 使用 Poetry 安装依赖
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# 设置环境变量
ENV PYTHONPATH=/app
ENV PORT=8000

# 暴露端口
EXPOSE ${PORT}

# 启动命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
