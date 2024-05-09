import sys
import os
from model import TransformerLM
from helpers import tokenize, detokenize

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'shared'))
from decoders.greedy import decode_greedy
from decoders.sampling import decode_sampling

if (len(sys.argv) < 2):
    print("Please specify the name of the txt file you want to summarize")
    sys.exit(1)

file_name = sys.argv[1]

with open(file_name, 'r') as file:
  text = file.read()

model = TransformerLM(mode='eval')

model.init_from_file('groundup/slogan/modelOutput/model.pkl.gz', weights_only=True)

print("The slogan of the file you provided is:")
print(decode_sampling(text, model, EOS=50260, PAD=50257, tokenize=tokenize, detokenize=detokenize))