"""
자취 공동구매/나눔 알리미 프로젝트의 메인 실행 파일
최소 10년차 파이썬 개발자 기준, PEP8 스타일 준수
"""

from flask import Flask, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # 세션을 위한 키


from app.views import views_bp
app.register_blueprint(views_bp)


if __name__ == "__main__":
    app.run(debug=True)
