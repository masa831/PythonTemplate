from src import timer # または from my_package import timer
import asyncio
import time


# デコレータに変数名を渡して計測
@timer.start('optimize_time')
def run_optimization():
    time.sleep(1.5)
    return "SUCCESS"

@timer.start('data_process_time')
def process_data():
    time.sleep(0.5)

# 実行
timer.set('all_time')
run_optimization()
process_data()
timer.end('all_time')

# 計測結果の取り出し
results = timer.get_results()
print(results) 
# 出力例: {'optimize_time': 1.5002, 'data_process_time': 0.5001}