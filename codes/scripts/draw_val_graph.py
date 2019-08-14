import numpy as np
import matplotlib.pyplot as plt

filename = "0723_pretrain.log"

f = open("./log/" + filename)
epoch_list = []
psnr_list = []
for line in f.readlines():
    splited = line.split(' ')
    # print (splited)
    # continue
    epoch = int(splited[4][7:-1])
    psnr_str = splited[-1][:-1]
    e_log = psnr_str.split('e')
    psnr = float(e_log[0]) * 10**(int(e_log[1]))
    epoch_list.append(epoch)
    psnr_list.append(psnr)

n = []
print (max(psnr_list))
print (np.mean(psnr_list))
max_index = psnr_list.index(max(psnr_list))
print (epoch_list[max_index])
for x in range(0, len(psnr_list)):
    n.append(x)
plt.plot(n, psnr_list)
plt.xlabel("epoch")
plt.ylabel("psnr")
plt.title("Validation Result")
plt.show()
