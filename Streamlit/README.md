# Streamlit

## memo

```bash
% cd
cd Streamlit

% 仮想環境起動
envs\Scripts\activate

% cd&仮想環境起動
cd Streamlit & envs\Scripts\activate

% 終了
deactivate
```

## 概要

回答案を表示

Streamlitで汎用性の高いWebアプリケーション開発を実現するクラス実装テンプレート

Streamlitは、PythonでWebアプリケーション開発を容易にする強力なフレームワークです。  
コード量を抑えながら、インタラクティブなUIやリアルタイムデータ処理など、高度な機能を実現できます。  

## 参考URL

<https://toukei-lab.com/streamlit>

## 実行方法

```python
# 実行コマンド
streamlit run xxx.py
```

## streamlit終了時サーバが落ちないとき

```bash
# スレッド強制終了
taskkill /F /IM streamlit.exe

# PID確認
tasklist /FI "IMAGENAME eq streamlit.exe"

# ゾンビプロセスを強制終了
taskkill /F /PID <PID>
```
