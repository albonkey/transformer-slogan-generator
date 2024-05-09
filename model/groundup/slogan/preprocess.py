import sys
import os
import numpy as np
import trax
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'shared'))
from Tokenization.Tokenization import convert_tokens_to_ids

def get_data_streams():
  train_gen = get_dataset_generator('groundup/slogan/data/train_data_tokens.csv')
  test_gen = get_dataset_generator('groundup/slogan/data/test_data_tokens.csv')

  train_stream = process_dataset(train_gen)
  test_stream = process_dataset(test_gen)

  train_input, train_target, train_mask = next(train_stream)

  assert sum((train_input - train_target)**2) == 0 

  boundaries =  [128, 256,  512, 1024]
  batch_sizes = [16,    8,    4,    2, 1]

  train_batch_stream = trax.data.BucketByLength(
      boundaries, batch_sizes)(train_stream)
  
  test_batch_stream = trax.data.BucketByLength(
      boundaries, batch_sizes)(test_stream)
  
  return (train_batch_stream, test_batch_stream)

def get_dataset_generator(file_path):
  data = pd.read_csv(file_path)
  for index, row in data.iterrows():
    yield row['company'], row['description'], row['slogan']

def process_dataset(dataset):
  input_pipeline = trax.data.Serial(
    tokenToID,
    preprocess,
    trax.data.FilterByLength(2048)
  )

  return input_pipeline(dataset)

def tokenToID(stream):
  for (company, description, slogan) in stream:
    companyTokenized = convert_tokens_to_ids(company.split())
    descriptionTokenized = convert_tokens_to_ids(description.split())
    sloganTokenized = convert_tokens_to_ids(slogan.split())
    yield companyTokenized, descriptionTokenized, sloganTokenized

def preprocess(stream):
  EOS = 50260
  PAD = 50257
  
  for (company, description, slogan) in stream:
    joint = np.array(list(company) + list(description) + [EOS, PAD] + list(slogan) + [EOS])
    mask = [0] * (len(list(company)) + len(list(description)) + 2) + [1] * (len(list(slogan)) + 1)
    yield joint, joint, np.array(mask)
