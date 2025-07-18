"""
지역 및 반 선택, 비밀번호 입력 UI (Flask + HTML + CSS)
최소 10년차 파이썬 개발자 기준, PEP8 및 웹 접근성 준수
"""

from flask import Blueprint, render_template, request, redirect, url_for, session

views_bp = Blueprint('views', __name__)

REGIONS = ["서울", "대전", "광주", "구미", "부산"]


@views_bp.route('/select_region', methods=['GET', 'POST'])
def select_region():
    if request.method == 'POST':
        region = request.form.get('region')
        return redirect(url_for('views.select_entry', region=region))
    return render_template('select_region.html', regions=REGIONS)



# 임시 데이터 저장소
group_purchases = [
    {
        'title': '수박 같이 사서 나눌 사람?',
        'description': '마트에서 큰 수박 사서 반씩 나눠요!',
        'deadline': '오늘 저녁',
        'participants': '3',
        'creator': '김수박',
        'joiners': [],
        'comments': []
    }
]
sharings = [
    {
        'type': '나눔',
        'title': '김치 나눔해요',
        'description': '집에서 담근 김치, 필요하신 분 나눔합니다!',
        'quantity': '2',
        'creator': '홍길동',
        'receivers': [],
        'comments': []
    },
    {
        'type': '교환',
        'title': '장조림 교환 원해요',
        'description': '장조림과 김치 교환 원합니다!',
        'quantity': '1',
        'creator': '이교환',
        'receivers': [],
        'comments': []
    }
]
chats = [
    {
        'creator': '이저녁',
        'message': '오늘 저녁 같이 먹으러 갈 사람?',
        'comments': []
    }
]



@views_bp.route('/class_home', methods=['GET', 'POST'])

def class_home():
    region = session.get('region')
    class_name = session.get('class_name')
    dong = session.get('dong')
    nickname = session.get('nickname')
    # 수다글 작성 처리
    if request.method == 'POST':
        message = request.form.get('message')
        if nickname and message:
            chats.append({'creator': nickname, 'message': message, 'comments': []})
        return redirect(url_for('views.class_home'))
    # 안내문구 생성
    if dong:
        welcome_msg = f"{region} {dong} 모여라!"
    elif class_name:
        welcome_msg = f"{region} {class_name} 칭구들!"
    else:
        welcome_msg = f"{region}에 입장하셨습니다!"
    return render_template('class_home.html', region=region, class_name=class_name, dong=dong,
                           group_purchases=group_purchases, sharings=sharings, chats=chats, nickname=nickname, welcome_msg=welcome_msg)

# 댓글 작성 라우트
@views_bp.route('/write_comment/<int:chat_idx>', methods=['POST'])

def write_comment(chat_idx):
    nickname = session.get('nickname')
    text = request.form.get('text')
    if nickname and text and 0 <= chat_idx < len(chats):
        if 'comments' not in chats[chat_idx]:
            chats[chat_idx]['comments'] = []
        chats[chat_idx]['comments'].append({'creator': nickname, 'text': text})
    return redirect(url_for('views.class_home'))

# 공동구매 글 작성
@views_bp.route('/write_group_purchase', methods=['GET', 'POST'])
def write_group_purchase():
    if request.method == 'POST':
        post = {
            'title': request.form['title'],
            'description': request.form['description'],
            'deadline': request.form['deadline'],
            'participants': request.form['participants'],
            'creator': request.form['creator']
        }
        group_purchases.append(post)
        return redirect(url_for('views.class_home'))
    return render_template('write_group_purchase.html')

# 나눔 글 작성
@views_bp.route('/write_sharing', methods=['GET', 'POST'])
def write_sharing():
    if request.method == 'POST':
        post_type = request.form.get('type')
        post = {
            'type': post_type,
            'title': request.form['title'],
            'description': request.form['description'],
            'quantity': request.form['quantity'],
            'creator': request.form['creator'],
            'receivers': [],
            'comments': []
        }
        sharings.append(post)
        return redirect(url_for('views.class_home'))
    # 나눔/교환 타입 선택 폼 추가
    return render_template('write_sharing.html', types=['나눔', '교환'])

# 캠퍼스/반 입장 선택 및 닉네임 입력 플로우
@views_bp.route('/select_entry/<region>', methods=['GET', 'POST'])
def select_entry(region):
    if request.method == 'POST':
        entry_type = request.form.get('entry')
        session['region'] = region
        if entry_type == 'area':
            dong = request.form.get('dong')
            session['dong'] = dong
            session.pop('class_name', None)
        elif entry_type == 'class':
            class_name = request.form.get('class_name')
            session['class_name'] = class_name
            session.pop('dong', None)
        # 닉네임 세션 체크
        if not session.get('nickname'):
            return redirect(url_for('views.enter_nickname'))
        return redirect(url_for('views.class_home'))
    return render_template('select_entry.html', region=region)

@views_bp.route('/enter_nickname', methods=['GET', 'POST'])
def enter_nickname():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        session['nickname'] = nickname
        # region/class_name이 이미 세션에 있으므로 바로 홈으로 이동
        return redirect(url_for('views.class_home'))
    return render_template('enter_nickname.html')

# 로그인 페이지
@views_bp.route('/', methods=['GET', 'POST'])
@views_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        # 실제 인증 로직은 추후 구현
        session['nickname'] = nickname
        # 로그인 성공 시 캠퍼스 선택으로 이동
        return redirect(url_for('views.select_region'))
    return render_template('login.html')

# 공동구매글 참여 라우트
@views_bp.route('/join_group_purchase/<int:post_idx>', methods=['POST'])
def join_group_purchase(post_idx):
    nickname = session.get('nickname')
    if nickname and 0 <= post_idx < len(group_purchases):
        if nickname not in group_purchases[post_idx]['joiners']:
            group_purchases[post_idx]['joiners'].append(nickname)
    return redirect(url_for('views.class_home'))

# 공동구매글 댓글 작성 라우트
@views_bp.route('/comment_group_purchase/<int:post_idx>', methods=['POST'])
def comment_group_purchase(post_idx):
    nickname = session.get('nickname')
    text = request.form.get('text')
    if nickname and text and 0 <= post_idx < len(group_purchases):
        group_purchases[post_idx]['comments'].append({'creator': nickname, 'text': text})
    return redirect(url_for('views.class_home'))

# 나눔/교환글 나눔받기/교환하기 라우트
@views_bp.route('/receive_sharing/<int:post_idx>', methods=['POST'])
def receive_sharing(post_idx):
    nickname = session.get('nickname')
    if nickname and 0 <= post_idx < len(sharings):
        if nickname not in sharings[post_idx]['receivers']:
            sharings[post_idx]['receivers'].append(nickname)
    return redirect(url_for('views.class_home'))

# 나눔/교환글 댓글 작성 라우트
@views_bp.route('/comment_sharing/<int:post_idx>', methods=['POST'])
def comment_sharing(post_idx):
    nickname = session.get('nickname')
    text = request.form.get('text')
    if nickname and text and 0 <= post_idx < len(sharings):
        sharings[post_idx]['comments'].append({'creator': nickname, 'text': text})
    return redirect(url_for('views.class_home'))
