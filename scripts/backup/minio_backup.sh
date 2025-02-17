#!/bin/bash

BACKUP_DIR="/backup/minio"
DATE=$(date +%Y%m%d)

# 设置MinIO环境变量
export MC_HOST_minio=http://${MINIO_ACCESS_KEY}:${MINIO_SECRET_KEY}@localhost:9000

# 创建备份目录
mkdir -p $BACKUP_DIR/$DATE

# 执行备份
mc mirror minio/society-files $BACKUP_DIR/$DATE

# 检查备份是否成功
if [ $? -eq 0 ]; then
    echo "MinIO备份成功: $DATE"
else
    echo "MinIO备份失败"
    exit 1
fi