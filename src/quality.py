#!/usr/bin/python3

import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity
from skimage import io

# 读取参考图像和待比较图像（支持彩色或灰度）
ref_img = io.imread('../data/lena.jpg')     # reference image
comp_img = io.imread('../data/lena.jpg')    # comparison image

# 确保图像尺寸相同
if ref_img.shape != comp_img.shape:
    raise ValueError("Images must have the same dimensions.")

# 计算PSNR（自动处理数据类型）
data_range = 255 if ref_img.dtype == np.uint8 else 1.0
psnr_value = peak_signal_noise_ratio(ref_img, comp_img, data_range=data_range)

# 计算SSIM（自动处理彩色/灰度）
is_color = (len(ref_img.shape) == 3 and ref_img.shape[-1] in (3, 4))
ssim_kwargs = {'channel_axis': -1} if is_color else {}
ssim_value = structural_similarity(ref_img, comp_img, data_range=data_range, **ssim_kwargs)

print(f"PSNR: {psnr_value:.2f} dB")
print(f"SSIM: {ssim_value:.4f}")