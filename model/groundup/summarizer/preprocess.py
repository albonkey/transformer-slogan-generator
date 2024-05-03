import numpy as np
import tensorflow_datasets as tfds
import trax

def get_data_streams():
  train_data = tfds.load('cnn_dailymail', split='train', as_supervised=True)
  test_data = tfds.load('cnn_dailymail', split='test', as_supervised=True)

  train_data = tfds.as_numpy(train_data)
  test_data = tfds.as_numpy(test_data)

  train_stream = process_dataset(train_data)
  test_stream = process_dataset(test_data)

  train_input, train_target, train_mask = next(train_stream)

  assert sum((train_input - train_target)**2) == 0

  boundaries =  [128, 256,  512, 1024]
  batch_sizes = [16,    8,    4,    2, 1]

  train_batch_stream = trax.data.BucketByLength(
      boundaries, batch_sizes)(train_stream)

  test_batch_stream = trax.data.BucketByLength(
      boundaries, batch_sizes)(test_stream)
  
  return (train_batch_stream, test_batch_stream)


def process_dataset(dataset):
  pipeline = trax.data.Serial(
    tokenize,
    preprocess,
    trax.data.FilterByLength(2048)
  )

  return pipeline(dataset)

def tokenize(stream):
  return trax.data.Tokenize(vocab_dir='groundup/summarizer/vocab_dir/', vocab_file='summarize32k.subword.subwords')(stream)

def preprocess(stream):
  PAD = 0
  EOS = 1

  for (article, summary) in stream:
    joint = np.array(list(article) + [EOS, PAD] + list(summary) + [EOS])
    mask = [0] * (len(list(article)) + 2) + [1] * (len(list(summary)) + 1)
    yield joint, joint, np.array(mask)