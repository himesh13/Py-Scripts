import os
import rq1_rnn_emb_lstm as rnn
import inputs

# --- Parameters --
DIM = "1d"

# TOKENIZER_OUT_PATH = "../../data/tokenizer_out_cs/"
TOKENIZER_OUT_PATH = "/home/himesh/TagCoder/tokenizer_out_java/"
# ---

smell = "ComplexMethod"
data_path = os.path.join(os.path.join(TOKENIZER_OUT_PATH, smell), DIM)
inputs.preprocess_data(data_path)
rnn.main(data_path, smell)