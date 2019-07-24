# mat2vec-utility
Some tools that based on mat2vec

Most similar word vis
---
```
usage: keywords_to_graph.py [-h] [--topn TOPN] sentence

Visualize word embedding for most similar word to a sentence

positional arguments:
  sentence     A sentence to be analyzed.

optional arguments:
  -h, --help   show this help message and exit
  --topn TOPN  List and visualize topn similar words (default: 20)
```
Example:
```
python keywords_to_graph.py "cathodic oxygen reduction reaction" --topn=100
```

Corpus batch process
---
```
usage: batch_process.py [-h] [--save_path SAVE_PATH] source_path

Process articles form txt file.

positional arguments:
  source_path           Path to source txt file.

optional arguments:
  -h, --help            show this help message and exit
  --save_path SAVE_PATH
                        Save path (default: corpus.txt)
```
Example:
```
python batch_process.py example.txt
```
