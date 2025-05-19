---
{}
---

Here's the English translation of the provided Chinese text, maintaining technical accuracy, markdown formatting, math expressions, and code elements:

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# Overview of Diffusion Model Training and Sampling Process

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

**Diffusion models** are inspired by non-equilibrium thermodynamics. They define a Markov chain of diffusion steps, gradually adding random noise to the data, and then learn the reverse diffusion process to construct desired data samples from noise. Unlike VAEs or flow models, diffusion models are learned with a fixed procedure, and the latent variables have high dimensionality.

During the training phase, noise is added to the image, and this noisy image is input to the network. The network needs to predict the added noise.

During the usage phase, starting from randomly generated noise, the network predicts what noise was added, and then gradually removes the noise until the original is restored.

---

# 1. Diffusion Process

- The diffusion process continuously adds noise to the image step by step until the image becomes pure noise;
- The added noise is Gaussian noise, and each subsequent moment is obtained by adding noise to the image from the previous moment.

**Process of adding noise:**

Two parameters are defined here: $\alpha_t$ and $\beta_t$; ($t$ ranges from 0 to $T$ integers, $\beta_t$ changes from $\beta_1$ to $\beta_T$, gradually increasing. In the paper, it increases from 0.0001 in equal increments $T$ times, up to 0.002)

The relationship between $\alpha_t$ and $\beta_t$ is:

$\beta_t$0             (1)

$T$ represents the number of steps required for the image to completely transform into pure noise through gradual noise addition, i.e., the total number of noise addition steps needed for the image. $t$ represents a specific step within $T$.

The expression for the process of adding noise to the image can be written as:

$\beta_t$4          (2)

$\beta_t$5 represents the image after adding noise at the $t$ diffusion step, while $\beta_t$7 is the image obtained at time $\beta_t$8; $\beta_t$9 represents the noise added at time $t$, which is sampled from a standard normal distribution $t$1

Therefore, we can gradually add noise from the original image $t$2 to $t$3 according to formula (2):

$t$4

$t$5

......

$\beta_t$4

......

$t$7

From this, we can see that as $\beta_t$ gradually increases, $\alpha_t$ gradually decreases, and $T$0 gradually increases. This means that the added noise is gradually increasing, while the proportion of the original image is gradually decreasing, and the degree of noise addition is expanding step by step.

However, for network training, data needs to be randomly sampled. It would be too cumbersome to recursively calculate from $t$2 every time we sample at time $t$.

So we need to calculate it in one go:

Substituting the equation: $T$3 into (2), we get

$T$4  

Expanding the equation:

$T$5  

$T$6  

Where each added noise — $T$7 — follows a normal distribution $t$1

So we can combine the coefficients between $T$9 and $\beta_t$9, because multiplying a normal distribution by a coefficient only changes the variance, and $\beta_t$1

Therefore,

$\beta_t$2  

$\beta_t$3  

$\beta_t$4  

Substituting $\beta_t$5 into the above equation, repeating the process, and substituting $\beta_t$6, we get

$\beta_t$7  

$\beta_t$8    (3)

Where $\beta_t$9 represents the product from $\beta_1$0 to $\alpha_t$

# 2. Training Process

Therefore, the training process of the diffusion model is as follows:

1. Randomly select an image from the dataset,
2. Randomly select a diffusion step from 1 to T,
3. Calculate $\beta_t$5 according to equation (3),
4. Input to the network, get the output, compute the loss between the output and the added noise, update the gradient,
5. Repeat training until satisfied.

The detailed code process for the training process is as follows:

```python
for i, (x_0) in enumerate(tqdm_data_loader):  # 由数据加载器加载数据，
 x_0 = x_0.to(device)  # 将数据加载至相应的运行设备(device)
    t = torch.randint(1, T, size=(x_0.shape[0],), device=device)  # 对每一张图片随机在1~T的扩散步中进行采样
    sqrt_alpha_t_bar = torch.gather(sqrt_alphas_bar, dim=0, index=t).reshape(-1, 1, 1, 1)  # 取得不同t下的 根号下alpha_t的连乘
    """取得不同t下的 根号下的一减alpha_t的连乘"""
    sqrt_one_minus_alpha_t_bar = torch.gather(sqrt_one_minus_alphas_bar, dim=0, index=t).reshape(-1, 1, 1, 1)
    noise = torch.randn_like(x_0).to(device)  # 从标准正态分布中采样得到z
    x_t = sqrt_alpha_t_bar * x_0 + sqrt_one_minus_alpha_t_bar * noise  # 计算x_t
    out = net_model(x_t, t)  # 将x_t输入模型，得到输出
    loss = loss_function(out, noise) # 将模型的输出，同添加的噪声做损失
    optimizer.zero_grad()  # 优化器的梯度清零
    loss.backward()  # 由损失反向求导
    optimizer.step()  # 优化器更新参数
```

# 3. Forward Usage Process

The usage process is to remove noise step by step from $t$3 to predict $t$2

In other words, given $t$3, we need to first infer $\beta_t$7, then $\beta_1$7..., and finally predict $t$2

According to Bayes' formula, the derivation is:
$\beta_1$9
The entire algorithm is:

1. $t$3 is randomly sampled from a standard normal distribution;
2. Loop from T to 1,
3. Calculate $\beta_t$7 according to the above formula, repeating the process, where $\beta_T$2 is the network model, the input is the result of step $\beta_t$5 and step t, because the model needs to encode the position of each step, $\beta_T$4 is sampled from a standard normal distribution, and z is set to zero when t is the last step

The specific code is as follows:

```python
for t_step in reversed(range(T)):  # 从T开始向零迭代
    t = t_step
    t = torch.tensor(t).to(device)

    z = torch.randn_like(x_t,device=device) if t_step > 0 else 0  # 如果t大于零，则采样自标准正态分布，否则为零
    """按照公式计算x_{t-1}"""
    x_t_minus_one = torch.sqrt(1/alphas[t])*(x_t-(1-alphas[t])*model(x_t, t.reshape(1,))/torch.sqrt(1-alphas_bar[t]))+torch.sqrt(betas[t])*z
    
    x_t = x_t_minus_one
```

# 4. Network Model

The model uses UNet and includes position encoding information for the t-th diffusion step.