This is the repository for ESRGAN. Most of the codes remain unchanged from the original codes (https://github.com/xinntao/BasicSR). Notice that we use the old version of BasicSR, which contains .json files for configuration and old arch of the pretrained models.

# changes
1. Please change the path in codes/options/train/train_ESRGAN.json and codes/options/test/test_ESRGAN.json. For better training result, please use the RRDB_ESRGAN_x4.pth for the "pretrain_model_G". 
2. To draw the validation graph, please use tb_logger or draw_val_graph.py. 
3. Please use generate_mod_LR_bic.py to prepare the data. 
4. Use net_interp.py to tune the alpha parameter. 

# other
In /Chaoyi, this directory contains the code to add gaussian kernel to the images and extract video frames.