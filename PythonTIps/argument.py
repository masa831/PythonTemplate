# sample code
import argparse

parser = argparse.ArgumentParser(description='hogehoge')

# 引数を設定する
parser.add_argument('-a', '--A', type=int, default=1, required=True, help='-hの時の説明文')
parser.add_argument('-c', '--color', choices=['red', 'blue', 'green'])
parser.add_argument('-ft', '--flag_t', action='store_true')
parser.add_argument('-ff', '--flag_f', action='store_false')

# プログラム内で引数を使う
args = parser.parse_args()
print(args.A)
print(args.color)
print(args.flag_t)
print(args.flag_f)

# 参考URL
# https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0

# command sample
# argument.py -a 100
# -> 100, None, False, True
# argument.py -a 100 -c red -ft -ff
# -> 100, red, True, False
