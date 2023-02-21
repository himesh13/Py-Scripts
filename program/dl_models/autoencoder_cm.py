import os
import autoencoder

TOKENIZER_OUT_PATH = "/home/himesh/TagCoder/tokenizer_out_java/"
OUT_FOLDER = "/home/himesh/TagCoder/result"
# TOKENIZER_OUT_PATH = r"..\..\data\tokenizer_out"
# OUT_FOLDER = r"..\results\rq1\raw"

smell_list = ["ComplexMethod"]
DIM = "1d"

for smell in smell_list:
    data_path = os.path.join(TOKENIZER_OUT_PATH, smell, DIM)
    autoencoder.main_lstm(smell, data_path, skip_iter=-1)