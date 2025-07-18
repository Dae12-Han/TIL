"""
데이터 모델 정의 파일
공동구매, 나눔, 사용자, 참여, 알림 등
"""

# 예시: 사용자 모델
class User:
    def __init__(self, nickname, password=None, name=None):
        self.nickname = nickname
        self.password = password  # 반별 입장용
        self.name = name  # 선택적 로그인용

# 예시: 공동구매 모델
class GroupPurchase:
    def __init__(self, title, description, creator):
        self.title = title
        self.description = description
        self.creator = creator

# 예시: 나눔 모델
class Sharing:
    def __init__(self, title, description, creator):
        self.title = title
        self.description = description
        self.creator = creator
