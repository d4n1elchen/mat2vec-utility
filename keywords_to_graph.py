from gensim.models import Word2Vec
from mat2vec.processing import MaterialsTextProcessor
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import plot_utility

text_processor = MaterialsTextProcessor()
w2v_model = Word2Vec.load("../mat2vec/mat2vec/training/models/pretrained_embeddings")
tsne_transformer = TSNE(n_components=2)

sentence = "LiCoO2 is a battery cathode material"
topn = 20

words, _ = text_processor.process(sentence)
similar_words_result = w2v_model.wv.most_similar(positive=words, topn=topn)

similar_words, similar_words_score = zip(*similar_words_result)
print(similar_words)

similar_words_vec = w2v_model[similar_words]

similar_words_embedded = tsne_transformer.fit_transform(similar_words_vec)

fig = plt.figure(figsize=(16,8))
plot_utility.plot_tsne(fig.gca(), similar_words, similar_words_embedded)
plt.show()
