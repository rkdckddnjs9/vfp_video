#python tools/train.py configs/spa_video/slowfast_r50_8xb8-4x16x1-256e_kinetics400-rgb.py --work-dir ./work_dirs/task1/slowfast/

#python tools/train.py configs/spa_video/c3d_sports1m-pretrained_8xb30-16x1x1-45e_ucf101-rgb.py --work-dir ./work_dirs/task1/c3d/

#python tools/train.py configs/spa_video/timesformer_divST_8xb8-8x32x1-15e_kinetics400-rgb.py --work-dir ./work_dirs/task1/timesformer/

python tools/train.py configs/spa_video/tpn-slowonly_imagenet-pretrained-r50_8xb8-8x8x1-150e_kinetics400-rgb.py --work-dir ./work_dirs/task1/tpn/

python tools/train.py configs/spa_video/mvit-small-p244_32xb16-16x4x1-200e_kinetics400-rgb.py --work-dir ./work_dirs/task1/mvit/

python tools/train.py configs/spa_video/swin-small-p244-w877_in1k-pre_32xb4-amp-32x2x1-30e_kinetics710-rgb.py --work-dir ./work_dirs/task1/video-swin/
