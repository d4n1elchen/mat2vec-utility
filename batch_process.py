import os
import argparse
from mat2vec.processing import MaterialsTextProcessor

text_processor = MaterialsTextProcessor()

parser = argparse.ArgumentParser(description='Process articles form txt file.')

parser.add_argument('source_path', type=str, help='Path to source txt file.')
parser.add_argument('--save_path', type=str, default='corpus.txt', help='Save path (default: corpus.txt)')

args = parser.parse_args()

with open(args.source_path) as infile:
    with open(args.save_path, 'w+') as outfile:
        for line in infile:
            words, _ = text_processor.process(line)
            outfile.write(' '.join(words) + '\n')

