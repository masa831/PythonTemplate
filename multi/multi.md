# 並列化処理関連

pythonにおける並列処理はいくつか方法がある。

Treading
諸事情で実装経験があったのでやってみた
→こいつは１コアしか使えないので速度は大きく変わらない模様。
それでも4minも変わるのは意外

multiprocessing.Process
並列処理したい関数に引数が複数あるので、Processを利用した。
しかしいくらggってもスレッド数の制限方法が分からず、それは実装できなかった。
そのせいで、実行すると1000個の並列処理をするのでPCがカクカクになってしまった。

multiprocessing.Pool
引数は1つしか持てないが、スレッド数を簡単に指定できる。
以下のような関数をカマス事で複数引数にも対応できた。

```python
def wrapper(args):
	return f(*args)
```

### 参考URL

<https://qiita.com/XM03/items/c9d15ece66d48057c798>

<https://qiita.com/simonritchie/items/1ce3914eb5444d2157ac>