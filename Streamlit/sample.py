# template pattern1

import streamlit as st

class AppState:
    def __init__(self):
        # アプリケーションの状態変数を初期化
        self.page = "home"
        self.data = {}

class Page:
    def __init__(self, app_state):
        self.app_state = app_state

    def render(self):
        # ページのコンテンツを描画
        pass

class Widget:
    def __init__(self, app_state):
        self.app_state = app_state

    def render(self):
        # ウィジェットを描画
        pass

class Home(Page):
    def render(self):
        # ホームページのコンテンツを描画
        #ヘッダー表示
        st.header("streamlitテストアプリ")
        #タイトル表示
        st.title("Webアプリ開発中")
        #テキスト表示
        st.write("生活用アプリ")

class Data(Page):
    def render(self):
        # データページのコンテンツを描画
        pass

class InputWidget(Widget):
    def render(self):
        # 入力ウィジェットを描画
        pass

class OutputWidget(Widget):
    def render(self):
        # 出力ウィジェットを描画
        pass

app_state = AppState()

# ページとウィジェットのインスタンスを作成
home = Home(app_state)
data = Data(app_state)
input_widget = InputWidget(app_state)
output_widget = OutputWidget(app_state)

while True:
    # ページの表示
    if app_state.page == "home":
        home.render()
    elif app_state.page == "data":
        data.render()

    # ウィジェットの表示
    input_widget.render()
    output_widget.render()

    # イベント処理
    # ...
