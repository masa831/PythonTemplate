# src/utils/path.py
from pathlib import Path


def find_project_root(marker_dirs=("data", "src")) -> Path:
    """
    プロジェクトルートを探す。指定したディレクトリがすべて存在するディレクトリをルートとみなす。
    """
    # 現在のパスを取得
    current = Path().resolve()
    print(f'[DBG] {current=}')
    # 現在のパス、親ディレクトリを対象に検索
    for parent in [current] + list(current.parents):
        # marker_dirs のディレクトリがすべて存在するか確認
        if all((parent / d).is_dir() for d in marker_dirs):
            return parent
    raise RuntimeError("プロジェクトルートが見つかりません")


def resolve_path_from_root(*relative_parts, marker_dirs=("data", "src")) -> Path:
    """
    プロジェクトルートを起点としたパスを解決する。
    例: resolve_path_from_root("data", "sample.csv")
    """
    root = find_project_root(marker_dirs)
    return root.joinpath(*relative_parts)
