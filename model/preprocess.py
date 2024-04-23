import numpy as np
from sklearn.model_selection import train_test_split
import trax
import pandas as pd
from transformers import GPT2Tokenizer


def get_data_streams(csv_file_path):
  data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
  train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

  train_gen = dataset_generator(train_data)
  test_gen = dataset_generator(test_data)

  train_stream = process_dataset(train_gen)
  test_stream = process_dataset(test_gen)

  train_input, train_target, train_mask = next(train_stream)

  assert sum((train_input - train_target)**2) == 0 

  boundaries =  [128, 256,  512, 1024]
  batch_sizes = [16,    8,    4,    2, 1]

  # Create the streams.
  train_batch_stream = trax.data.BucketByLength(
      boundaries, batch_sizes)(train_stream)
  
  test_batch_stream = trax.data.BucketByLength(
      boundaries, batch_sizes)(test_stream)
  
  return (train_batch_stream, test_batch_stream)

def dataset_generator(data):
  for index, row in data.iterrows():
    yield str(row['company']), str(row['description']), str(row['slogan'])

def process_dataset(dataset):
  input_pipeline = trax.data.Serial(
    trax.data.Tokenize(vocab_dir='model/vocab_dir/', vocab_file='summarize32k.subword.subwords'),
    preprocess,
    trax.data.FilterByLength(2048)
  )

  return input_pipeline(dataset)

def preprocess(stream):
  EOS = 1
  PAD = 0
  print(stream)
  for (company, description, slogan) in stream:
    joint = np.array(list(company) + list(description) + [EOS, PAD] + list(slogan) + [EOS])
    mask = [0] * (len(list(company)) + len(list(description)) + 2) + [1] * (len(list(slogan)) + 1)
    yield joint, joint, np.array(mask)
