#!/usr/bin/env python3
import sys
from selenium_kt import fetch_kt_jobs  # 기존 크롤링 코드가 들어있는 모듈
from push_notification import send_push_notification  # 푸시 알림 함수 (Firebase 등)

def main():
    # 크롤링 실행
    jobs = fetch_kt_jobs()
    
    # 여기서 이전에 크롤링한 데이터와 비교하여 새로운 공고만 필터링하는 로직을 넣을 수 있음.
    # 예제에서는 단순히 최근 3개의 공고가 새로 올라왔다고 가정합니다.
    new_jobs = jobs[:3]  # 필요에 따라 변경
    
    # 새로운 공고가 있다면 각 공고에 대해 푸시 알림 전송
    if new_jobs:
        for job in new_jobs:
            # 예시: 제목과 회사, 기간, 링크 정보를 알림 본문에 포함
            notification_title = job["title"]
            notification_body = f"{job['company']} | {job['date']} | {job['dday']}\n{job['link']}"
            send_push_notification(notification_title, notification_body)
    else:
        print("🚀 새로운 공고 없음")
    
    print("✅ 스크립트 실행 완료")

if __name__ == "__main__":
    main()
