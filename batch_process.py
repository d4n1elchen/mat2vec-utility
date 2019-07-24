import os
import argparse
from tqdm import tqdm
from mat2vec.processing import MaterialsTextProcessor

text_processor = MaterialsTextProcessor()

parser = argparse.ArgumentParser(description='Process articles form txt file.')

parser.add_argument('source_path', type=str, help='Path to source txt file.')
parser.add_argument('--save_path', type=str, default='corpus.txt', help='Save path (default: corpus.txt)')

args = parser.parse_args()

def get_num_lines(file_path):
    with open(file_path) as f:
        n = sum(1 for l in f)
    return n

print('Read text form', args.source_path, ', write processed sentence to', args.save_path)
with open(args.source_path) as infile:
    with open(args.save_path, 'w+') as outfile:
        for line in tqdm(infile, total=get_num_lines(args.source_path)):
            words, _ = text_processor.process(line)
            outfile.write(' '.join(words) + '\n')

