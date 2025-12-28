from flask import Flask, render_template, request, jsonify
from algorithms.sorting import bubble_sort, merge_sort
from algorithms.graph import bfs, dfs
from flask import request, jsonify
from algorithms.tree import build_tree, inorder, preorder, postorder
from algorithms.pathfinding import astar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    arr = data['array']
    algo = data['algorithm']

    if algo == 'bubble':
        steps = bubble_sort(arr)
    elif algo == 'merge':
        steps = merge_sort(arr)
    else:
        steps = []

    return jsonify(steps)
@app.route('/graph', methods=['POST'])
def graph_algo():
    data = request.json
    graph = data['graph']
    start = data['start']
    algo = data['algorithm']

    if algo == 'bfs':
        steps = bfs(graph, start)
    elif algo == 'dfs':
        steps = dfs(graph, start)
    else:
        steps = []

    return jsonify(steps)
@app.route('/tree', methods=['POST'])
def tree_algo():
    data = request.json
    arr = data['array']
    algo = data['algorithm']

    root = build_tree(arr)
    steps = []

    if algo == 'inorder':
        inorder(root, steps)
    elif algo == 'preorder':
        preorder(root, steps)
    elif algo == 'postorder':
        postorder(root, steps)

    return jsonify(steps)
@app.route('/pathfinding', methods=['POST'])
def pathfinding():
    data = request.json
    grid = data['grid']
    start = tuple(data['start'])
    end = tuple(data['end'])

    result = astar(grid, start, end)
    return jsonify(result)
if __name__ == '__main__':
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)