import pickle
import torchvision.datasets as dset

import numpy as np

import sys

# for bleu score
from nltk.translate import bleu_score
from nltk import word_tokenize

final_file_name = sys.argv[1]
match_index_path = sys.argv[2]
start_index = int(sys.argv[3])
end_index = int(sys.argv[4])

# load the data with cocoAPI this time we dont need transform
cap = dset.CocoCaptions(root = '/home/raille/coco-features/coco-dataset/train2017',
                        annFile = '/home/raille/coco-features/coco-dataset/annotations/captions_train2017.json')

# load the match index pickle
match_index = pickle.load( open( match_index_path, "rb" ) )

# implement bleu score
total_bleu_score = []
weights = [0.25, 0.25, 0.25, 0.25]

for i, matched_index in enumerate(match_index[start_index:end_index]):
    score = []
    for caption in cap[i][1]:
        candidate_tokens = word_tokenize(caption.replace('.',''))
        references_tokens = [word_tokenize(i.replace('.','')) for i in cap[matched_index][1]] 
        score.append(bleu_score.sentence_bleu(references_tokens, candidate_tokens, weights))
    mean = np.mean(score)
    total_bleu_score.append(mean)

with open(final_file_name, "a") as myfile:
    myfile.write(str(np.mean(total_bleu_score)) + ',')