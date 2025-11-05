#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国节假日日历生成器
生成 iCalendar (.ics) 格式的日历文件
"""

from datetime import datetime, date
from typing import List, Dict, Optional
import uuid


class Holiday:
    """节假日类"""
    def __init__(self, name: str, start_date: date, end_date: Optional[date] = None, 
                 is_workday: bool = False, description: str = ""):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date or start_date
        self.is_workday = is_workday
        self.description = description


def format_date(dt: date) -> str:
    """格式化日期为 iCalendar 格式"""
    return dt.strftime("%Y%m%d")


def generate_ics_event(holiday: Holiday) -> str:
    """生成单个事件的 ICS 内容"""
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{holiday.name}-{holiday.start_date}"))
    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    
    event_type = "补班" if holiday.is_workday else "假期"
    summary = f"{holiday.name} ({event_type})"
    
    event = f"""BEGIN:VEVENT
UID:{uid}@chinese-holiday
DTSTAMP:{now}
DTSTART;VALUE=DATE:{format_date(holiday.start_date)}
DTEND;VALUE=DATE:{format_date(holiday.end_date)}
SUMMARY:{summary}
DESCRIPTION:{holiday.description}
STATUS:CONFIRMED
TRANSP:TRANSPARENT
END:VEVENT"""
    
    return event


def get_holidays_2025() -> List[Holiday]:
    """获取 2025 年的节假日安排"""
    holidays = [
        # 元旦
        Holiday("元旦", date(2025, 1, 1), date(2025, 1, 1), description="2025年元旦假期"),
        
        # 春节
        Holiday("春节", date(2025, 1, 28), date(2025, 2, 4), description="2025年春节假期"),
        Holiday("春节调休", date(2025, 1, 26), date(2025, 1, 26), is_workday=True, description="春节调休补班"),
        Holiday("春节调休", date(2025, 2, 8), date(2025, 2, 8), is_workday=True, description="春节调休补班"),
        
        # 清明节
        Holiday("清明节", date(2025, 4, 4), date(2025, 4, 6), description="2025年清明节假期"),
        
        # 劳动节
        Holiday("劳动节", date(2025, 5, 1), date(2025, 5, 5), description="2025年劳动节假期"),
        Holiday("劳动节调休", date(2025, 4, 27), date(2025, 4, 27), is_workday=True, description="劳动节调休补班"),
        
        # 端午节
        Holiday("端午节", date(2025, 5, 31), date(2025, 6, 2), description="2025年端午节假期"),
        Holiday("端午节调休", date(2025, 5, 31), date(2025, 5, 31), is_workday=True, description="端午节调休补班"),
        
        # 中秋节
        Holiday("中秋节", date(2025, 10, 6), date(2025, 10, 8), description="2025年中秋节假期"),
        Holiday("中秋节调休", date(2025, 9, 28), date(2025, 9, 28), is_workday=True, description="中秋节调休补班"),
        Holiday("中秋节调休", date(2025, 10, 11), date(2025, 10, 11), is_workday=True, description="中秋节调休补班"),
        
        # 国庆节
        Holiday("国庆节", date(2025, 10, 1), date(2025, 10, 8), description="2025年国庆节假期"),
    ]
    
    return holidays


def get_holidays_2026() -> List[Holiday]:
    """获取 2026 年的节假日安排（国办发明电〔2025〕7号）"""
    holidays = [
        # 元旦：1月1日至3日放假调休，共3天。1月4日（周日）上班
        Holiday("元旦", date(2026, 1, 1), date(2026, 1, 3), description="2026年元旦假期"),
        Holiday("元旦调休", date(2026, 1, 4), date(2026, 1, 4), is_workday=True, description="元旦调休补班"),
        
        # 春节：2月15日（农历腊月二十八）至23日（农历正月初七）放假调休，共9天
        # 2月14日（周六）、2月28日（周六）上班
        Holiday("春节", date(2026, 2, 15), date(2026, 2, 23), description="2026年春节假期（农历腊月廿八至正月初七）"),
        Holiday("春节调休", date(2026, 2, 14), date(2026, 2, 14), is_workday=True, description="春节调休补班"),
        Holiday("春节调休", date(2026, 2, 28), date(2026, 2, 28), is_workday=True, description="春节调休补班"),
        
        # 清明节：4月4日（周六）至6日（周一）放假，共3天
        Holiday("清明节", date(2026, 4, 4), date(2026, 4, 6), description="2026年清明节假期"),
        
        # 劳动节：5月1日（周五）至5日（周二）放假调休，共5天。5月9日（周六）上班
        Holiday("劳动节", date(2026, 5, 1), date(2026, 5, 5), description="2026年劳动节假期"),
        Holiday("劳动节调休", date(2026, 5, 9), date(2026, 5, 9), is_workday=True, description="劳动节调休补班"),
        
        # 端午节：6月19日（周五）至21日（周日）放假，共3天
        Holiday("端午节", date(2026, 6, 19), date(2026, 6, 21), description="2026年端午节假期"),
        
        # 中秋节：9月25日（周五）至27日（周日）放假，共3天
        Holiday("中秋节", date(2026, 9, 25), date(2026, 9, 27), description="2026年中秋节假期"),
        
        # 国庆节：10月1日（周四）至7日（周三）放假调休，共7天
        # 9月20日（周日）、10月10日（周六）上班
        Holiday("国庆节", date(2026, 10, 1), date(2026, 10, 7), description="2026年国庆节假期"),
        Holiday("国庆节调休", date(2026, 9, 20), date(2026, 9, 20), is_workday=True, description="国庆节调休补班"),
        Holiday("国庆节调休", date(2026, 10, 10), date(2026, 10, 10), is_workday=True, description="国庆节调休补班"),
    ]
    
    return holidays


def generate_calendar(holidays: List[Holiday], calendar_name: str = "中国法定节假日") -> str:
    """生成完整的 ICS 日历文件"""
    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    
    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Chinese Holiday Calendar//CN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:{calendar_name}
X-WR-TIMEZONE:Asia/Shanghai
X-WR-CALDESC:中国法定节假日及调休安排
"""
    
    for holiday in holidays:
        ics_content += generate_ics_event(holiday) + "\n"
    
    ics_content += "END:VCALENDAR\n"
    
    return ics_content


def main():
    """主函数"""
    print("正在生成中国节假日日历...")
    
    # 获取节假日数据
    holidays_2025 = get_holidays_2025()
    holidays_2026 = get_holidays_2026()
    
    # 合并所有节假日
    all_holidays = holidays_2025 + holidays_2026
    
    # 生成日历文件
    ics_content = generate_calendar(all_holidays, "中国法定节假日 (2025-2026)")
    
    # 保存到文件
    with open("chinese_holiday.ics", "w", encoding="utf-8") as f:
        f.write(ics_content)
    
    print(f"✓ 日历文件已生成: chinese_holiday.ics")
    print(f"✓ 2025年: {len(holidays_2025)} 个事件")
    print(f"✓ 2026年: {len(holidays_2026)} 个事件")
    print(f"✓ 总计: {len(all_holidays)} 个事件")
    print("\n使用方法：")
    print("1. 将此文件上传到 GitHub 仓库")
    print("2. 启用 GitHub Pages")
    print("3. 在日历应用中订阅: https://your-username.github.io/ChineseHoliday/chinese_holiday.ics")


if __name__ == "__main__":
    main()
