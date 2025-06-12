import os

def find_absolute_path(relative_path: str) -> str:
    current_dir = os.getcwd()
    max_depth = 2

    # 上位3階層を含む探索対象ディレクトリ一覧を作成
    search_dirs = [os.path.abspath(current_dir)]
    for _ in range(max_depth):
        current_dir = os.path.dirname(current_dir)
        search_dirs.append(os.path.abspath(current_dir))

    # 各ディレクトリに対して、下位3階層を再帰的に探索
    for base_dir in search_dirs:
        for root, dirs, files in os.walk(base_dir):
            # 深さ制限
            rel_depth = os.path.relpath(root, base_dir).count(os.sep)
            if rel_depth > max_depth:
                continue

            candidate_path = os.path.join(root, relative_path)
            if os.path.isfile(candidate_path):
                return os.path.abspath(candidate_path)

    return None  # ファイルが見つからなかった場合
