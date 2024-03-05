_base_ = [
    '../../recognition/swin/swin-small-p244-w877_in1k-pre_8xb8-amp-32x2x1-30e_kinetics400-rgb.py'
]

dataset_type = 'VideoDataset'
data_root = 'data/spa_data/'
data_root_val = 'data/spa_data/'
ann_file_train = 'data/spa_data/train_task3.txt'
ann_file_val = 'data/spa_data/val_task3.txt'
ann_file_test = 'data/spa_data/val_task3.txt'

model = dict(
    type='Recognizer3D_MultiTask',
    cls_head=dict(num_classes=7)
    cls_head_2=dict(
        type='I3DHead',
        in_channels=768,
        num_classes=3,
        spatial_type='avg',
        dropout_ratio=0.5,
        average_clips='prob')
    cls_head_3=dict(
        type='I3DHead',
        in_channels=768,
        num_classes=2,
        spatial_type='avg',
        dropout_ratio=0.5,
        average_clips='prob')
    )

file_client_args = dict(io_backend='disk')
train_pipeline = [
    dict(type='DecordInit', **file_client_args),
    dict(type='SampleFrames', clip_len=32, frame_interval=2, num_clips=1),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='RandomResizedCrop'),
    dict(type='Resize', scale=(224, 224), keep_ratio=False),
    # dict(type='Flip', flip_ratio=0.5),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
val_pipeline = [
    dict(type='DecordInit', **file_client_args),
    dict(
        type='SampleFrames',
        clip_len=32,
        frame_interval=2,
        num_clips=1,
        test_mode=True),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]
test_pipeline = [
    dict(type='DecordInit', **file_client_args),
    dict(
        type='SampleFrames',
        clip_len=32,
        frame_interval=2,
        num_clips=4,
        test_mode=True),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 224)),
    dict(type='ThreeCrop', crop_size=224),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='PackActionInputs')
]

repeat_sample = 2
train_dataloader = dict(
    batch_size=2,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_train,
        data_prefix=dict(video=data_root),
        pipeline=train_pipeline))
val_dataloader = dict(
    batch_size=2,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_val,
        data_prefix=dict(video=data_root_val),
        pipeline=val_pipeline,
        test_mode=True))
test_dataloader = dict(
    batch_size=1,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_val,
        data_prefix=dict(video=data_root_val),
        pipeline=test_pipeline,
        test_mode=True))

val_evaluator = dict(type='AccMetric_MultiTask')
test_evaluator = val_evaluator

optim_wrapper = dict(optimizer=dict(lr=2e-3))

# Default setting for scaling LR automatically
#   - `enable` means enable scaling LR automatically
#       or not by default.
#   - `base_batch_size` = (16 GPUs) x (8 samples per GPU).
auto_scale_lr = dict(enable=False, base_batch_size=128)
