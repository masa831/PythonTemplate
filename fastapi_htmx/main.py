from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import io
import matplotlib.pyplot as plt
import numpy as np
import asyncio  # 非同期処理のため
from src.parameter import Parameter
from src.dataset import Datasets
from src.optimizer import ScipModel


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 計算結果を一時保存する辞書（簡易的なキャッシュ）
# NOTE: グローバル変数を共有しているので、複数人でアクセス時は他の人の結果が表示さえる可能性あり
# session_id, user_idなどをキーにするとよいかも
results_cache = {}

# 静的ファイルの設定（必要であれば）
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "graph_url": None})


@app.post("/calculate_tsp", response_class=HTMLResponse)
async def calculate_tsp(
    request: Request,
    start_point: str = Form(...),
    end_point: str = Form(...)
):
    # 最適化処理を実行
    param = Parameter()
    data_path = "data"
    ds = Datasets.generate(data_path)
    optimizer = ScipModel(param, ds)
    df, ans_vars = optimizer.optimize()

    # キャッシュに結果を保存
    results_cache['coords'] = ds.coords
    results_cache['ans_x'] = ans_vars['x']

    # kpi
    dist = df['distance'].sum().round(3)
    num_cities = ds.n_depots

    return f"""
    <div id="graph-area" class="space-y-4">
        <div class="grid grid-cols-2 gap-4 bg-blue-50 p-4 rounded-lg border border-blue-200 text-left">
            <div><span class="text-gray-500 text-xs">総移動距離:</span> <p class="font-bold text-lg">{dist} km</p></div>
            <div><span class="text-gray-500 text-xs">訪問都市数:</span> <p class="font-bold text-lg">{num_cities}</p></div>
        </div>

        <img src="/generate_graph?t={asyncio.get_event_loop().time()}"
             alt="TSP Route" class="mx-auto max-w-full h-auto shadow-md rounded border">

        <p class="text-sm text-green-600 font-bold text-center">計算が完了しました</p>
    </div>
    """


@app.get("/generate_graph")
async def generate_graph():
    coords = results_cache['coords']
    x_matrix = results_cache['ans_x']

    # ダミーのグラフ生成ロジック
    n = len(coords)
    # plt.figure(figsize=(5, 4))
    fig, ax = plt.subplots(figsize=(6, 4))

    # 1. 都市（点）をプロット
    plt.scatter(coords[:, 0], coords[:, 1], c='red', s=80, zorder=5)

    # 2. 都市番号を表示
    for i, (x, y) in enumerate(coords):
        plt.annotate(f" {i}", (x, y), fontsize=12, fontweight='bold', color='black')

    # 3. 最適ルートと距離を表示
    found_lines = False
    for i in range(n):
        for j in range(n):
            # x_matrixがスカラーではなく行列であることを確認してアクセス
            if x_matrix[i, j] > 0.5:
                p1 = coords[i]
                p2 = coords[j]
                # 線を描画
                plt.plot([p1[0], p2[0]], [p1[1], p2[1]], c='blue', alpha=0.5, zorder=1)
                # 距離の計算  # ここはdsからの引用でも可
                dist = np.sqrt(np.sum((p1 - p2)**2))
                # 中間地点の計算（ここにテキストを置く）
                mid_x = (p1[0] + p2[0]) / 2
                mid_y = (p1[1] + p2[1]) / 2
                # 距離を表示 (小数点1ケタまで)
                # bboxを付けると背景が白くなり、線と重なっても読みやすくなります
                plt.text(mid_x, mid_y, f"{dist:.1f}",
                         fontsize=9, color='darkgreen', fontweight='bold',
                         ha='center', va='center',
                         bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

                # 矢印を追加
                plt.arrow(p1[0], p1[1], (p2[0]-p1[0])*0.5, (p2[1]-p1[1])*0.5, 
                          head_width=1.2, head_length=1.5, fc='blue', ec='blue', alpha=0.3)
                found_lines = True

    if not found_lines:
        print("警告: 有効なルートが見つかりませんでした。")

    plt.title("TSP Optimal Route with Distances")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True, linestyle='--', alpha=0.5)

    # Matplotlibのグラフをメモリ上のPNG画像として保存
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)  # メモリを解放

    return StreamingResponse(buf, media_type="image/png")


# def plot_tsp_route(coords, x_matrix):
    """
    coords: (n, 2) の都市座標配列
    x_matrix: (n, n) のバイナリ行列
    """
    # n = len(coords)
    # plt.figure(figsize=(5, 4))

    # # 1. 都市（点）をプロット
    # plt.scatter(coords[:, 0], coords[:, 1], c='red', s=80, zorder=5)

    # # 2. 都市番号を表示
    # for i, (x, y) in enumerate(coords):
    #     plt.annotate(f" {i}", (x, y), fontsize=12, fontweight='bold', color='black')

    # # 3. 最適ルートと距離を表示
    # found_lines = False
    # for i in range(n):
    #     for j in range(n):
    #         # x_matrixがスカラーではなく行列であることを確認してアクセス
    #         if x_matrix[i, j] > 0.5:
    #             p1 = coords[i]
    #             p2 = coords[j]
    #             # 線を描画
    #             plt.plot([p1[0], p2[0]], [p1[1], p2[1]], c='blue', alpha=0.5, zorder=1)
    #             # 距離の計算  # ここはdsからの引用でも可
    #             dist = np.sqrt(np.sum((p1 - p2)**2))
    #             # 中間地点の計算（ここにテキストを置く）
    #             mid_x = (p1[0] + p2[0]) / 2
    #             mid_y = (p1[1] + p2[1]) / 2
    #             # 距離を表示 (小数点1ケタまで)
    #             # bboxを付けると背景が白くなり、線と重なっても読みやすくなります
    #             plt.text(mid_x, mid_y, f"{dist:.1f}", 
    #                      fontsize=9, color='darkgreen', fontweight='bold',
    #                      ha='center', va='center',
    #                      bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

    #             # 矢印を追加
    #             plt.arrow(p1[0], p1[1], (p2[0]-p1[0])*0.5, (p2[1]-p1[1])*0.5, 
    #                       head_width=1.2, head_length=1.5, fc='blue', ec='blue', alpha=0.3)
    #             found_lines = True

    # if not found_lines:
    #     print("警告: 有効なルートが見つかりませんでした。")

    # plt.title("TSP Optimal Route with Distances")
    # plt.xlabel("X Coordinate")
    # plt.ylabel("Y Coordinate")
    # plt.grid(True, linestyle='--', alpha=0.5)
    # plt.show()
