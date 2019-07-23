import matplotlib.pyplot as plt

def plot_tsne(label, vec):
    for ix, v in enumerate(vec):
        x, y = v[0], v[1]
        plt.scatter(x, y)
        plt.annotate(label[ix],
                     xy=(x, y),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
