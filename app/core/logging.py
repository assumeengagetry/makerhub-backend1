import sys
from pathlib import Path
from loguru import logger

def setup_logging():
    # 创建日志目录
    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)

    # 移除默认处理程序
    logger.remove()

    # 添加控制台输出
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG"
    )

    # 添加文件输出
    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="30 days",
        compression="zip",
        level="INFO",
        encoding="utf-8"
    )

    return logger