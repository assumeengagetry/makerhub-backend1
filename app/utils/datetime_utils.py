# datetime_utils.py

from datetime import datetime, timedelta
from typing import Optional
import pytz

CHINA_TZ = pytz.timezone('Asia/Shanghai')

def get_current_time() -> datetime:
    """获取当前北京时间"""
    return datetime.now(CHINA_TZ)

def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """格式化日期时间"""
    if dt.tzinfo is None:
        dt = CHINA_TZ.localize(dt)
    return dt.strftime(format_str)

def parse_datetime(date_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> Optional[datetime]:
    """解析日期时间字符串"""
    try:
        dt = datetime.strptime(date_str, format_str)
        return CHINA_TZ.localize(dt)
    except ValueError:
        return None

def get_week_start_end(dt: datetime = None) -> tuple[datetime, datetime]:
    """获取指定日期所在周的起止时间"""
    if dt is None:
        dt = get_current_time()
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=6)
    return start.replace(hour=0, minute=0, second=0), end.replace(hour=23, minute=59, second=59)