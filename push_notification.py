import firebase_admin
from firebase_admin import credentials, messaging

# Firebase Admin SDK 초기화
# 'path/to/firebase-adminsdk.json' 부분을 실제 JSON 파일 경로로 변경하세요.
cred = credentials.Certificate("jobcrwaling-firebase-adminsdk-fbsvc-44f5aa55c6.json")
firebase_admin.initialize_app(cred)

def send_push_notification(title, body):
    """
    Firebase Cloud Messaging(FCM)을 이용해 푸시 알림 전송
    :param title: 알림 제목
    :param body: 알림 내용
    """
    # FCM 메시지 구성: topic을 이용하여 구독자에게 전송
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        topic="kt-job-alerts"  # 구독 토픽, 클라이언트 앱에서 이 토픽에 구독되어 있어야 합니다.
    )
    try:
        response = messaging.send(message)
        print("✅ 푸시 알림 전송 완료:", response)
    except Exception as e:
        print("❌ 푸시 알림 전송 실패:", e)
