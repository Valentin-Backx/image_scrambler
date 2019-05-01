from PIL import Image
import numpy as np

import sys


# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.open(sys.argv[1])

newImg = Image.new('RGB', (img.size[0],img.size[1]), "black") # create a new black image


pixels = img.load() # create the pixel map
newPixels = newImg.load()

indexes = []

for i in range(img.size[0]):    	# for every col:
    for j in range(img.size[1]):    # For every row
        indexes+=[pixels[i,j]]

print(img.size)

#shuffling indexes and showing "crypted" image
permutation = np.random.permutation(len(indexes))

indexes = np.array(indexes)[permutation]

for p in range(0,len(indexes)):
	newPixels[p/img.size[1],p%img.size[1]] = tuple(indexes[p])

newImg.show()

#reforming indexes and showing "decrypted" image
reformedImg = Image.new('RGB', (img.size[0],img.size[1]), "black") # create a new black image

reformedPixels = reformedImg.load()

inverse_permutation = np.argsort(permutation)

reformedIndexes = indexes[inverse_permutation]

for p in range(0,len(reformedIndexes)):
	reformedPixels[p/img.size[1],p%img.size[1]] = tuple(reformedIndexes[p])

reformedImg.show()
