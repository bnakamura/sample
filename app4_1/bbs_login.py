from flask import session, redirect

# ログイン用userの一覧を定義
USERLIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc',
    'bin':'bin',
}

# ログインしているかを調べる sessionにloginというキーがあればログイン状態と判定する
def is_login():
    return 'login' in session

# ログイン処理
def try_login(user, password):
    # 該当ユーザがいるか？
    if user not in USERLIST: return False
    # パスワードが合っているか？
    if USERLIST[user] != password:return False
    # ログイン処理
    session['login'] = user
    return True

# ログアウト処理
def try_logout():
    session.pop('login', None)
    return True

# セッションからユーザ名を得る
def get_user():
    if is_login(): return session['login']
    return 'not login'