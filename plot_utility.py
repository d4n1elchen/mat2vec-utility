import matplotlib.pyplot as plt

def plot_tsne(ax, label, vec):
    for ix, v in enumerate(vec):
        x, y = v[0], v[1]
        ax.scatter(x, y)
        ax.annotate(label[ix],
                     xy=(x, y),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
