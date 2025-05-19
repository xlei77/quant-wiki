---
{}
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)


# VQVAE Generative Model Overview

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

This is a PyTorch implementation of the VQVAE generative model (<https://arxiv.org/abs/1711.00937>).

You can find the author's [original implementation in TensorFlow](https://github.com/deepmind/sonnet/blob/master/sonnet/python/modules/nets/vqvae.py) which includes [examples that can be run in Jupyter notebooks](https://github.com/deepmind/sonnet/blob/master/sonnet/examples/vqvae_example.ipynb).

## Install Dependencies

To install dependencies, create a conda or virtual environment using Python 3, then run `pip install -r requirements.txt`.

## Running VQ VAE

To run the VQ-VAE simply run `python3 main.py`. Make sure to include the `-save` flag if you want to save your model. You can also add parameters in the command line. The default values are specified below:

To run VQ-VAE, simply run `python3 main.py`. If you want to save the model, make sure to include the `-save` flag. You can also add parameters in the command line. The default values are shown below:

```python
parser.add_argument("--batch_size", type=int, default=32)
parser.add_argument("--n_updates", type=int, default=5000)
parser.add_argument("--n_hiddens", type=int, default=128)
parser.add_argument("--n_residual_hiddens", type=int, default=32)
parser.add_argument("--n_residual_layers", type=int, default=2)
parser.add_argument("--embedding_dim", type=int, default=64)
parser.add_argument("--n_embeddings", type=int, default=512)
parser.add_argument("--beta", type=float, default=.25)
parser.add_argument("--learning_rate", type=float, default=3e-4)
parser.add_argument("--log_interval", type=int, default=50)
```

## Model

VQ VAE consists of the following basic model components:

1. `Encoder` class and defines `x -> z_e`
2. Class `VectorQuantizer` that converts encoder output into discrete one-hot vectors, which are indices of the nearest embedding vectors `z_e -> z_q`
3. `Decoder` class and defines mapping `python3 main.py`0 and class that reconstructs the original image

The encoder/decoder classes are stacks of convolution and deconvolution layers, with residual blocks in their architecture [see ResNet paper](https://arxiv.org/abs/1512.03385). The residual modules are defined by `python3 main.py`1 and `python3 main.py`2 classes.

These components are organized in the following folder structure:

```
models/
    - decoder.py -> Decoder
    - encoder.py -> Encoder
    - quantizer.py -> VectorQuantizer
    - residual.py -> ResidualLayer, ResidualStack
    - vqvae.py -> VQVAE
```

## PixelCNN - Sampling from VQ VAE Latent Space

To sample from the latent space, we fit a PixelCNN `python3 main.py`3 on the latent pixel values. The trick here is to recognize that VQ VAE maps images to a latent space that has the same structure as a 1-channel image. For example, if you run the default VQ VAE parameters, you map RGB images `python3 main.py`4 to a latent space with shape (8,8,1), which is equivalent to `python3 main.py`5 grayscale images. Therefore, you can use PixelCNN to fit the distribution of "pixel" values in the 8x8 1-channel latent space.

To train PixelCNN on latent representations, you first need to follow these steps:

1. Train VQ VAE on your chosen dataset
2. Encode the dataset using the saved VQ VAE parameters and save the discrete latent space representations using `python3 main.py`6. In `python3 main.py`7, quantizer.py is min_encoding_indices `python3 main.py`8 utils.load_latent_block `python3 main.py`9 python pixelcnn/gated_pixelcnn.py `-save`0 LATENT_BLOCK`, which only works after you have trained VQ VAE and saved the latent representations.