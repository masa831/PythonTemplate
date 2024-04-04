import streamlit as st


class App:
    def __init__(self):
        self.app_state = {}

    def render(self):
        # ヘッダー表示
        st.header("Streamlit テストアプリ")

        # タイトル表示
        st.title("Webアプリ開発中")

        # テキスト表示
        st.write("生活用アプリ")

        # スライダー
        self.render_slider()

        # ボタン
        self.render_buttons()

        # テキスト入力
        self.render_text_input()

        # チェックボックス
        self.render_checkbox()

    def render_slider(self):
        # タイトル
        st.title("スライダー")

        # スライダーの値取得
        weight = st.slider("今日の体重は", 0, 100)

        # 値の表示
        st.write("今の体重は" + str(weight) + "kgです")

    def render_buttons(self):
        # タイトル
        st.title("今日の天気は")

        # リセットボタン
        st.button("リセット", type="primary")

        # 晴れボタン
        if st.button("晴れ？"):
            st.write("今日も元気に！")
        else:
            st.write("傘を忘れずに")

    def render_text_input(self):
        # タイトル
        st.title("やること")

        # テキスト入力
        todo = st.text_input("今やること", key="do")

        # 入力内容の表示
        st.write("やること:", self.app_state.get("do", ""))

    def render_checkbox(self):
        # タイトル
        st.title("ごみ捨てチェック")

        # チェックボックス
        is_trashed = st.checkbox("ごみ捨てた？")

        # チェック状態によるメッセージ表示
        if is_trashed:
            st.write("お疲れ様！")
        else:
            st.write("忘れずに！")


if __name__ == "__main__":
    app = App()
    app.render()
