from setuptools import setup

setup(
    name='test_package',
    version='0.1.0',
    description='パッケージの説明文',
    author='作者名',
    author_email='メールアドレス',
    url='プロジェクトURL',
    packages=['test_package'],  # パッケージ名
    install_requires=[
        # 必要な依存関係
        # '依存関係パッケージ名1',
        # '依存関係パッケージ名2',
        # ...
    ],
    python_requires='>=3.8',  # 必要なPythonバージョン
)
