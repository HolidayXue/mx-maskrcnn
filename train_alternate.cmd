set TRAIN_DIR=model/res50-fpn/cityscape/alternate/
set DATASET=Cityscape
set SET=train
set TEST_SET=val

python train_alternate_mask_fpn.py^
    --network resnet_fpn^
    --dataset %DATASET%^
    --image_set %SET%^
    --root_path %TRAIN_DIR%^
    --pretrained model/resnet-50^
    --prefix %TRAIN_DIR%^
    --pretrained_epoch 0^
    --gpu 0 > %TRAIN_DIR%train.log