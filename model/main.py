import sys

from model import TransformerLM
from decoders.greedy import decode_greedy
from decoders.sampling import decode_sampling

if (len(sys.argv) < 2):
    print("Please specify the name of the txt file you want to summarize")
    sys.exit(1)

file_name = sys.argv[1]

with open(file_name, 'r') as file:
  text = file.read()

model = TransformerLM(model_depth=512,
                      ff_depth=2048,
                      nr_layers=6,
                      nr_heads=8,
                      mode='eval')

model.init_from_file('modelOutput/model.pkl.gz', weights_only=True)

print("The summarization of the file you provided is:")
print(decode_sampling(text, model))