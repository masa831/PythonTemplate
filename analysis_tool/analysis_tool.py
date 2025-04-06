import ast

class FunctionCallAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.call_graph = {}  # {関数名: [呼び出される関数名リスト] }
        self.current_function = None

    def visit_FunctionDef(self, node):
        """関数定義の開始"""
        self.current_function = node.name
        self.call_graph[self.current_function] = []
        self.generic_visit(node)
        self.current_function = None

    def visit_Call(self, node):
        """関数呼び出しの解析"""
        if isinstance(node.func, ast.Name):  # 直接呼び出し (foo())
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):  # メソッド呼び出し (obj.foo())
            func_name = node.func.attr
        else:
            func_name = None

        if self.current_function and func_name:
            self.call_graph[self.current_function].append(func_name)

        self.generic_visit(node)

def analyze_function_calls(filepath):
    """Python ファイルを解析して関数の依存関係を取得"""
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=filepath)

    analyzer = FunctionCallAnalyzer()
    analyzer.visit(tree)
    return analyzer.call_graph



class ClassInheritanceAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.inheritance_graph = {}  # {クラス名: [親クラス名リスト]}

    def visit_ClassDef(self, node):
        """クラス定義を解析して継承関係を取得"""
        class_name = node.name
        base_classes = [base.id for base in node.bases if isinstance(base, ast.Name)]
        self.inheritance_graph[class_name] = base_classes
        self.generic_visit(node)

def analyze_class_inheritance(filepath):
    """Python ファイルを解析してクラスの継承関係を取得"""
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=filepath)

    analyzer = ClassInheritanceAnalyzer()
    analyzer.visit(tree)
    return analyzer.inheritance_graph


import networkx as nx
import matplotlib.pyplot as plt

def plot_dependency_graph(dependencies):
    """関数の依存関係を可視化"""
    G = nx.DiGraph()

    for func, calls in dependencies.items():
        for call in calls:
            G.add_edge(func, call)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    plt.show()


import inspect
import re
import importlib.util

def load_module(filepath):
    """指定したファイルをモジュールとしてロードする"""
    module_name = "target_module"
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def get_function_dependencies(filepath):
    """関数の依存関係を解析"""
    module = load_module(filepath)
    functions = inspect.getmembers(module, inspect.isfunction)
    
    dependencies = {}
    for name, func in functions:
        source = inspect.getsource(func)
        called_functions = re.findall(r'\b(\w+)\(', source)
        dependencies[name] = list(set(called_functions) - {name})  # 自分自身の呼び出しを除外

    return dependencies
