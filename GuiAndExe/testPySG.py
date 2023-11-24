import PySimpleGUI as sg

class SimpleGUIApp:
    """
    PySimpleGUIを使用したシンプルなGUIアプリケーションのクラス。

    Exaples:
        app = SimpleGUIApp()
        app.run()
    """

    def __init__(self):
        """
        ウィンドウとレイアウトを初期化します。
        """
        # テーマ指定
        sg.theme('Default')
        # レイアウト
        self.layout = [
            [sg.Text("テンプレートレイアウトです。\nここには説明文を入れます。")],
            [sg.Text('ファイル1', size=(25, 1)), sg.Input( key="FILE1", enable_events=True), sg.FileBrowse("ファイル選択")],
            [sg.Text('ファイル2'), sg.Input(key="FILE2", enable_events=True), sg.FileBrowse("ファイル選択")],
            [sg.Button("start", key="START", enable_events=True)]
            ]

        # ウィンドウ生成
        self.window = sg.Window("Demo", self.layout)

    def run(self):
        """
        イベントループを開始します。
        """
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'START':
                try:
                    file1 = values["FILE1"]
                    file2 = values["FILE2"]
                    print('Start')
                    print(file1)
                    print(file2)
                    print('Finish')
                    
                    # 以下テンプレート
                    # コールバック関数結果を格納 ※アンパック使用
                    # jdg_flg, msg = template.func(file1,file2)

                    # コールバック関数の結果によって、メッセージを表示
                    # if jdg_flg == 1:
                    #     sg.popup("Process is Successful.")
                    # elif jdg_flg == 0:
                    #     sg.popup("Process is Successful. \n The File hasn't changed at all.")
                    # elif jdg_flg == -1:
                    #     sg.popup("An Error Occurred.\n" + msg)
                    # else:
                    #     sg.popup("An unexpected error has occurred.")

                except Exception :
                    print(traceback.format_exc())
                    sg.popup("An unexpected error has occurred.")

        self.window.close()

# 使用例
if __name__ == "__main__":
    app = SimpleGUIApp()
    app.run()

