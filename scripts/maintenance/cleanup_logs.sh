#!/bin/bash

LOG_DIR="/var/log/society-manager"

# 删除30天前的日志
find $LOG_DIR -type f -name "*.log" -mtime +30 -delete
find $LOG_DIR -type f -name "*.zip" -mtime +30 -delete

echo "已清理30天前的日志文件"