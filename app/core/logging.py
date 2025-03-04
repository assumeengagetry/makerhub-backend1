import sys
from pathlib import Path
from loguru import logger

def setup_logging():
    # 创建日志目录
    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)  # 如果目录不存在则创建

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
        rotation="00:00",  # 每天创建一个新日志文件
        retention="7 days",  # 保留30天的日志
        compression="zip",  # 压缩日志文件
        level="INFO",
        encoding="utf-8"
    )

    return logger  # 返回配置好的logger实例