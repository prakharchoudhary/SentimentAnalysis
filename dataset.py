import os
from tqdm import tqdm ##########
from urllib.request import urlretrieve
from os.path import isfile, isdir
import tarfile############

IMDb_dataset_folder_path = 'IMDb-dataset-py'

# a simple progress bar to show progress while downloading dataset.
class DLProgress(tqdm):
	last_block=0

	def hook(self, block_num=1, block_size=1, total_size=None):
		self.total = total_size
		self.update((block_num - self.last_block) * block_size)
		self.last_block = block_num

# checks if the zip file is already present and if not then downloads it.
if not isfile('aclImdb_v1.tar.gz'):
	with DLProgress(unit='B', unit_scale=True, miniters=1, desc='IMDb Dataset') as pbar:
		urlretrieve(
			'http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz',
			'aclImdb_v1.tar.gz',
			pbar.hook)

# checks if the zip file is already extracted and if not then extracted it.
if not isdir(IMDb_dataset_folder_path):
	with tarfile.open('aclImdb_v1.tar.gz') as tar:
		tar.extractall()
		tar.close()


