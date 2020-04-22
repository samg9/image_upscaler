import torch
from .architecture.architecture import *
import cv2
import numpy as np

def esrgan_load_generate(path_to_image):
    upscale = 4

    device = torch.device('cpu')
    model = RRDB_Net(3, 3, 64, 23, gc=32, upscale=upscale, norm_type=None, act_type='leakyrelu', \
                            mode='CNA', res_scale=1, upsample_mode='upconv')
    checkpoint = torch.load('esrgan/models/{:s}'.format('RRDB_ESRGAN_x4_old_arch.pth'))
    model.load_state_dict(checkpoint, strict=True) 

    model.eval()
    for k, v in model.named_parameters():
        v.requires_grad = False
    model = model.to(device)

    img = cv2.imread(path_to_image, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.to(device)

    output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    path = 'test_docs/result1_rlt.png'#.format(base) #should set write path with static global
    cv2.imwrite(path, output)