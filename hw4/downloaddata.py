from datasets import load_dataset
# HF_ENDPOINT=https://hf-mirror.com python downloaddata.py可以解决hf被墙的微调
dataset = load_dataset("fashion_mnist")
image_size = 28
channels = 1
batch_size = 128