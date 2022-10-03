import tensorflow as tf
import pandas as pd
import numpy as np

from class_DeepHit import Model_DeepHit
from tf_slim import fully_connected as FC_Net

tf.compat.v1.disable_eager_execution()

def load_logging(filename):
    data = dict()
    with open(filename) as f:
        def is_float(input):
            try:
                num = float(input)
            except ValueError:
                return False
            return True

        for line in f.readlines():
            if ':' in line:
                key,value = line.strip().split(':', 1)
                if value.isdigit():
                    data[key] = int(value)
                elif is_float(value):
                    data[key] = float(value)
                elif value == 'None':
                    data[key] = None
                else:
                    data[key] = value
            else:
                pass 
    return data

# Load the saved optimized hyperparameters

in_hypfile = 'model/hyperparameters_log.txt'
in_parser = load_logging(in_hypfile)

# Forward the hyperparameters
mb_size                     = in_parser['mb_size']

iteration                   = in_parser['iteration']

keep_prob                   = in_parser['keep_prob']
lr_train                    = in_parser['lr_train']

h_dim_shared                = in_parser['h_dim_shared']
h_dim_CS                    = in_parser['h_dim_CS']
num_layers_shared           = in_parser['num_layers_shared']
num_layers_CS               = in_parser['num_layers_CS']

if in_parser['active_fn'] == 'relu':
    active_fn                = tf.nn.relu
elif in_parser['active_fn'] == 'elu':
    active_fn                = tf.nn.elu
elif in_parser['active_fn'] == 'tanh':
    active_fn                = tf.nn.tanh
else:
    print('Error!')


initial_W                   = tf.keras.initializers.glorot_normal()

alpha                       = in_parser['alpha']  #for log-likelihood loss
beta                        = in_parser['beta']  #for ranking loss


# Create the dictionaries 
# For the input settings
input_dims                  = { 'x_dim'         : x_dim,
                                'num_Event'     : num_Event,
                                'num_Category'  : num_Category}

# For the hyperparameters
network_settings            = { 'h_dim_shared'         : h_dim_shared,
                                'h_dim_CS'          : h_dim_CS,
                                'num_layers_shared'    : num_layers_shared,
                                'num_layers_CS'    : num_layers_CS,
                                'active_fn'      : active_fn,
                                'initial_W'         : initial_W }

# Create the DeepHit network architecture

tf.compat.v1.reset_default_graph()

imported_graph = tf.compat.v1.train.import_meta_graph('model/model_itr_0.meta')

with tf.compat.v1.Session() as sess:
    # restore the saved vairable
    
    imported_graph.restore(sess,'models/checkpoint')
    
    model = Model_DeepHit(sess, "DeepHit", input_dims, network_settings)

