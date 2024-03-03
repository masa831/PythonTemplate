import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 100, (20,5)), columns=("国語", "数学", "理科", "社会", "英語"))

#表の表示
##サイドバーを活用
st.sidebar.title("テストの結果")
st.sidebar.dataframe(df) 

#棒グラフ
st.title("国語の成績")
st.bar_chart(df["国語"])

#折れ線グラフ
st.title("数学")
st.line_chart(df["数学"])

#散布図
df["合計"]=df["国語"]+df["数学"]+df["英語"]+df["理科"]+df["社会"]
st.title("理科と数学の関係")
st.scatter_chart(df, x = "理科", y = "数学", size="合計")

#Mapに散布図を表示
st.title("東京駅付近に散布図")
mapdf = pd.DataFrame(
    # 東京駅付近
    np.random.rand(50, 2)/[50, 50]  + [35.68, 139.76],
    # latitude 緯度 longitude 経度
    columns=['lat', 'lon']
)

st.map(mapdf)
