import sys
from loguru import logger
from pathlib import Path

def setup_logging():
    # 移除默认的处理器
    logger.remove()
    
    # 添加控制台输出
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO"
    )
    
    # 添加文件日志
    log_path = Path("/var/log/society-manager/app.log")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    logger.add(
        str(log_path),
        rotation="00:00",  # 每天轮换
        retention="30 days",  # 保留30天
        compression="zip",
        level="INFO",
        encoding="utf-8"
    )

    return logger