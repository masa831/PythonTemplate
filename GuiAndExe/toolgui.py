import PySimpleGUI as sg
from tkinter import messagebox
import time


class ToolGui:
    '''
    ToolGuiはGUIの設定をまとめたクラスです。

    Attributes:
        theme (theme): PySimpleGUIのテーマ
        window (window): windowオブジェクト
        list_xxx (list(str)): xxx
        dict_type (dictionary): xxx

    '''

    def __init__(self):
        '''
        ToolGuiのコンストラクタ。

        Note:
            layout用の変数をどこまでself変数とすべきか判断に迷う

        '''
        # テーマ指定
        self.theme = sg.theme('DefaultNoMoreNagging')

        self.dict_type = {'ALL':0, 'First':1, 'Second':2} # 辞書型で定義
        self.list_xxx = ('apple','banana','grape')
        
        # Note: list(dict_type.keys())と記載することで、辞書型のkeyをリストとして取得できる。
        # ウィンドウのレイアウトを定義
        layout = [
            [sg.Text("ツールテンプレートです。")],
            [sg.Text('ファイル', size=(12,1)), sg.Input( key="file1", enable_events=True), sg.FileBrowse("ファイル選択")],
            [sg.Text('タイプ', size=(12,1)), sg.Combo(list(self.dict_type.keys()), size=(15,1), key="xxx", enable_events=True)],
            [sg.Text('対象', size=(12,1)), sg.Combo(self.list_xxx, size=(15,1), key="type", enable_events=True)],
            [sg.Button("開始", size=(10,1), key="start", enable_events=True), sg.Button("終了", size=(10,1), key="quit", enable_events=True)]
        ]

        # タブを生成する場合のテンプレート
        # tab1_layout = [
        #     [sg.Text("AAAAAA")],
        #     [sg.Button("A", key="A", enable_events=True)]
        # ]

        # tab2_layout = [
        #     [sg.Text("BBBBB")],
        #     [sg.Button("B", key="B", enable_events=True)]
        # ]
        
        # self.layout = [
        #     [sg.TabGroup([[sg.Tab('VVV', tab1_layout), sg.Tab('XXXX', tab2_layout)]])]
        # ]

        # ウィンドウを作成
        self.window = sg.Window("ツール", layout)

    def run(self):
        '''
        GUI Windowのメインループ関数
        '''

        # 各種項目の値格納用変数
        filepath = ""
        status = 0
        target = ""

        # イベントループ
        while True:
            event, values = self.window.read()
            if (event == sg.WINDOW_CLOSED) or (event == "quit"):
                break
            elif event == "start":
                try:
                    # 処理中のポップアップ表示
                    popup_merge = sg.Window('Popup', [[sg.Text("")], [sg.Text('   処理中...   ')], [sg.Text("")]] , auto_close=False, finalize=True, grab_anywhere=True, modal=True, font=14)
                    popup_merge.refresh() # この処理がないと、画面が更新されず、ブラックアウトしてしまう
                    
                    # 時間がかかる処理の代替
                    time.sleep(10)
                    print(filepath, status, target)

                    # ポップアップ消去
                    popup_merge.close() # 現状の作りでは、すべての分岐にこれを配置する必要あり
                    
                    # コールバック関数の結果によって、メッセージを表示
                    sg.popup("Process is Successful. \n AAAA ")

                except Exception as e:
                    popup_merge.close()
                    messagebox.showerror("エラー", str(e)) # 下部のモジュールでエラーが発生しても、raiseしていれば、ここで内容を表示できる

            elif event == "file1":
                filepath = values['file1']
    
            elif event == "xxx":
                status = self.dict_type[values['xxx']]

            elif event == "type":
                target = values['type']


        self.window.close()

if __name__ == "__main__":
    tool = ToolGui()
    tool.run()
