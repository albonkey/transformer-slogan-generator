import os
import trax
from trax import layers as tl
from trax.supervised import training
from preprocess import get_data_streams
from model import TransformerLM

def training_loop(TransformerLM, train_gen, eval_gen, output_dir = 'groundup/slogan/modelOutput'):
    """
    Input:
        TransformerLM (trax.layers.combinators.Serial): The model you are building.
        train_gen (generator): Training stream of data.
        eval_gen (generator): Evaluation stream of data.
        output_dir (str): folder to save your file.
        
    Returns:
        trax.supervised.training.Loop: Training loop.
    """
    
    output_dir = os.path.expanduser(output_dir)
    lr_schedule = trax.lr.warmup_and_rsqrt_decay(n_warmup_steps=100, max_value=0.01)

    train_task = training.TrainTask(
      labeled_data=train_gen,
      loss_layer=tl.CrossEntropyLoss(), 
      optimizer=trax.optimizers.Adam(0.01),
      lr_schedule=lr_schedule,
      n_steps_per_checkpoint=10,
    )

    eval_task = training.EvalTask( 
      labeled_data=eval_gen,
      metrics=[tl.CrossEntropyLoss(), tl.Accuracy()]
    )

    model = TransformerLM(mode='train')

    loop = training.Loop(model,
                         train_task,
                         eval_tasks=[eval_task],
                         output_dir=output_dir
                        )
  
    return loop

# Get Preprocessed Data
train_batch_stream, eval_batch_stream = get_data_streams()

# Training
loop = training_loop(TransformerLM, train_batch_stream, eval_batch_stream)
loop.run(100)