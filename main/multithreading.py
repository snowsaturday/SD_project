# from multiprocessing.dummy import Pool as ThreadPool
# import time
#
# data = []
#
# for i in range(1000000):
# 	data.append('url{}'.format(i))
#
#
# def f(url):
# 	# do phantomjs stuff
# 	return str(url) + ' ok'
#
#
# if __name__ == '__main__':
#
# 	p = ThreadPool()
# 	t1 = time.time()
# 	make = p.map(f, data)
# 	t2 = time.time()
# 	print(make)
# 	print(t2 - t1)

	# t1 = time.time()
	# make = []
	# for i in data:
	# 	make.append('{}'.format(i))
	# t2 = time.time()
	# print(make)
	# print(t2 - t1)


import random
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import math


# # A histogram
# n = np.random.randn(100000)
# fig, axes = plt.subplots(1, 2, figsize=(12,4))
#
# axes[0].hist(n)
# axes[0].set_title("Default histogram")
# axes[0].set_xlim((min(n), max(n)))
#
# axes[1].hist(n, cumulative=True, bins=50)
# axes[1].set_title("Cumulative detailed histogram")
# axes[1].set_xlim((min(n), max(n)));

array = []

for x in range(0, 1000000):
	x = random.triangular(1, 100)
	print(format(x, '.16f'))

