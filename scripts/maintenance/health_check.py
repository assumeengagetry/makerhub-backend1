import requests
import sys
from loguru import logger

def check_api_health():
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            logger.info("API服务运行正常")
            return True
        else:
            logger.error(f"API服务异常: {response.status_code}")
            return False
    except Exception as e:
        logger.error(f"健康检查失败: {str(e)}")
        return False

if __name__ == "__main__":
    sys.exit(0 if check_api_health() else 1)