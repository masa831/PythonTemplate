import tkinter as tk

def display_hello():
    result_label.config(text="Hello")

root = tk.Tk()
root.title("Helloプログラム")

# ボタンを作成し、押下時の処理を設定する
button = tk.Button(root, text="押下", command=display_hello)
button.pack(padx=50, pady=20)

# 結果表示用のラベルを作成する
result_label = tk.Label(root, text="")
result_label.pack(padx=50, pady=20)

root.mainloop()