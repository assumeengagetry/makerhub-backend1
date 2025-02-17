#!/bin/bash

BACKUP_DIR="/backup/mongodb"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="society_db_$DATE.gz"

# 创建备份目录
mkdir -p $BACKUP_DIR

# 执行备份
mongodump --db society_db --archive=$BACKUP_DIR/$BACKUP_NAME --gzip

# 删除30天前的备份
find $BACKUP_DIR -type f -mtime +30 -delete

# 检查备份是否成功
if [ $? -eq 0 ]; then
    echo "MongoDB备份成功: $BACKUP_NAME"
else
    echo "MongoDB备份失败"
    exit 1
fi