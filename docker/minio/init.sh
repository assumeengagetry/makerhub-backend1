#!/bin/sh

# 等待 MinIO 服务启动
sleep 10

# 创建桶
mc alias set myminio http://localhost:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
mc mb myminio/$MINIO_BUCKET

# 上传初始图片
mc cp /docker-entrypoint-init.d/images/* myminio/$MINIO_BUCKET/