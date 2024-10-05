import os
import nbformat


def is_output_cleared(nb_path: str) -> bool:
    """指定されたipynbファイルの出力クリア状態を判定"""
    # ノートブックファイルを読み込む
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # 各セルの出力を確認
    for cell in nb.cells:
        if cell.cell_type == 'code':  # コードセルのみチェック
            if cell.outputs:  # 出力がある場合
                return False  # 出力がクリアされていないセルがあった場合、Falseを返す
    return True  # すべてのセルがクリアされている場合はTrueを返す


def check_notebooks_in_folder(folder_path: str) -> None:
    """指定パス以下のipynbファイルを判定"""
    # 指定されたフォルダ内の全ての.ipynbファイルを取得する
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                # 各ノートブックの出力がクリアされているかをチェック
                if is_output_cleared(notebook_path):
                    print(f"{notebook_path}: [OK] 全てのセルの出力はクリアされています。")
                else:
                    print(f"{notebook_path}: [NG] クリアされていないセルの出力があります。")

# 使用方法
# フォルダパスを指定
# folder_path = 'your_folder_path'
# 関数を実行する
# check_notebooks_in_folder(folder_path)
