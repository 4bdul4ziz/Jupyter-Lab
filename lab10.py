import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

# A dictionary containing the labels for
labels = {}
state_evaluations = {}

evaluation_per_player = [-1, 1]
evaluation_function_per_player = [min, max]


def main():
    tokens = "SDF"

    state = "F"
    labels[state] = state
    graph = []
    evalulation = move(state, tokens, graph)
    print("Game ends. Evaluation", evalulation)
    print(graph)
    plot_graph(graph)


def plot_graph(graph):
    G = nx.DiGraph()
    G.add_edges_from(graph)
    pos = graphviz_layout(G, prog="dot")
    fig = plt.gcf()
    fig.set_size_inches(160.5, 10.5)
    colors = ['green' if state_evaluations[node]
              == -1 else 'red' for node in G]
    nx.draw(G, pos, labels=labels, node_color=colors,
            font_size=16, node_size=300)
    plt.show()


def current_player(state):
    return int(len(state) % 2 == 1)


def move(state, tokens, graph):
    player_index = current_player(state)
    evaluate_function = evaluation_function_per_player[player_index]

    available_moves = []
    for t in tokens:
        if t != state[-1] and is_valid(state + t):
            available_moves.append(t)
    if not available_moves:
        evaluation = evaluation_per_player[1 - player_index]
        state_evaluations[state] = evaluation
        return evaluation

    results = []
    for m in available_moves:
        next_state = state + m
        labels[next_state] = m
        next_eval = move(next_state, tokens, graph)
        graph.append((state, next_state))
        results.append(next_eval)

    evaluation = evaluate_function(results)
    state_evaluations[state] = evaluation
    return evaluation


def is_valid(state):
    if "#" in state:
        return False
    res = [state[i: j] for i in range(len(state))
           for j in range(i + 1, len(state) + 1)]
    filtered = []
    for r in res:
        if len(r) > 2 and r[0] == r[-1]:
            filtered.append(r)

    return len(filtered) == len(set(filtered))


if __name__ == '__main__':
    main()
