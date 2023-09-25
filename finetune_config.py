_base_ = [
    'configs/_base_/models/resnet50.py',           # model settings
    'configs/_base_/datasets/imagenet_bs32.py',    # data settings
    'configs/_base_/schedules/imagenet_bs256.py',  # schedule settings
    'configs/_base_/default_runtime.py',           # runtime settings
]

# model settings
model = dict(
    backbone=dict(
        frozen_stages=2,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='https://download.openmmlab.com/mmclassification/v0/resnet/resnet18_8xb32_in1k_20210831-fbbb1da6.pth',
            prefix='backbone',
        )),
    head=dict(num_classes=2),
)

# >>>>>>>>>>>>>>> Override data settings here >>>>>>>>>>>>>>>>>>>
data_root = 'data/shoe'
train_dataloader = dict(
    dataset=dict(
        type='CustomDataset',
        data_root=data_root,
        ann_file='',       # We assume you are using the sub-folder format without ann_file
        data_prefix='train',
    ))
val_dataloader = dict(
    dataset=dict(
        type='CustomDataset',
        data_root=data_root,
        ann_file='',       # We assume you are using the sub-folder format without ann_file
        data_prefix='val',
    ))
test_dataloader = val_dataloader

# Change the checkpoint saving interval to iter-based
default_hooks = dict(checkpoint=dict(by_epoch=False, interval=10))

train_cfg = dict(by_epoch=False, max_epochs=100, val_interval=10)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
