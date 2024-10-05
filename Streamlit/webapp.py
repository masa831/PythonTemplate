import streamlit as st
import plotly.express as px


class WebApp:
    def __init__(self):
        self.md_path = 'md/description.md'
        self.slidar_val1 = 0
        self.slidar_val2 = 0
        self.button_state = False

    def run(self):
        self.show_initial_page()

        if self.button_state:
            self.show_timeline(self.slidar_val1, self.slidar_val2)

    def show_initial_page(self):
        st.title('Streamlit Webアプリ')
        # 初期画面にマークダウンファイルを表示する
        self.show_md()
        self.button_state = st.button('実行')

        st.sidebar.title('サイドバー')
        st.sidebar.markdown('ここにスライダーが表示されます。')
        self.slidar_val1 = st.sidebar.slider('スライダー1', 0, 100, 50)
        self.slidar_val2 = st.sidebar.slider('スライダー2', 0, 100, 50)

    def show_md(self):
        with open(self.md_path, 'r', encoding='utf-8') as file:
            initial_page_content = file.read()
            st.markdown(initial_page_content)

    def show_timeline(self, value1, value2):
        # st.markdown('# 実行結果')
        st.subheader('実行結果')
        st.write(f'スライダー1の値: {value1}')
        st.write(f'スライダー2の値: {value2}')

        # plotly.express.timelineを表示する
        # 以下はダミーのデータとしてランダムなデータを使用しています
        df = px.data.gapminder().query("country=='Japan'")
        fig = px.timeline(df, x_start="year", x_end="year", y="country", title="Timeline Plot")
        st.plotly_chart(fig)

# アプリの実行
app = WebApp()
app.run()
