import numpy as np
import h5py
from PIL import Image
import time

dataset = h5py.File("3DS/3dshapes.h5", "r")

images1 = dataset["images"][:240000]  # array shape [240000,64,64,3], uint8 in range(256)
labels1 = dataset["labels"][:240000]  # array shape [240000,6], float64
images2 = dataset["images"][240000:]  # array shape [240000,64,64,3], uint8 in range(256)
labels2 = dataset["labels"][240000:]  # array shape [240000,6], float64

print(images1.shape)
print(labels1.shape)
print(images2.shape)
print(labels2.shape)

# Select subet of data with only the desired values
# 1. Get rid of images where floor_hue, wall_hue, object_hue are the same
# 2. Get rid of images that are not largest or smallest scale
# 3. Get rid of images where the orientation is not left, right or frontal (-30, 0, 30)
# All selection criteria  subject to change.

# Work in two batches, because of memory issues
# Batch 1

start = time.time()
print("Start time batch 1:", start)

# 1. Get rid of images where floor_hue, wall_hue, object_hue are the same
# When not all values are the same, that means at leat two have to be different
different_hue_mask1 = (
    (labels1[:, 0] != labels1[:, 1]) | (labels1[:, 1] != labels1[:, 2])
)

labels1 = labels1[different_hue_mask1]
images1 = images1[different_hue_mask1]

print("Different hue mask applied.")
print(labels1.shape)
print(images1.shape)

# 2. Get rid of images that are not largest or smallest scale
two_sizes_mask1 = (labels1[:, 3] == 0.75) | (labels1[:, 3] == 1.25)

labels1 = labels1[two_sizes_mask1]
images1 = images1[two_sizes_mask1]

print("Two sizes mask applied.")
print(labels1.shape)
print(images1.shape)

# 3. Get rid of images where the orientation is not left, right or frontal (-30, 0, 30)
three_orientations_mask1 = (
    (labels1[:, 5] == -30.0) | (labels1[:, 5] == 0.0) | (labels1[:, 5] == 30.0)
)

labels1 = labels1[three_orientations_mask1]
images1 = images1[three_orientations_mask1]

print("Three orientations mask applied.")
print(labels1.shape)
print(images1.shape)

end = time.time()
print("End time batch 1:", end)

# Batch 2
start = time.time()
print("Start time batch 2:", start)

# 1. Get rid of images where floor_hue, wall_hue, object_hue are the same
# When not all values are the same, that means at leat two have to be different
different_hue_mask2 = (
    (labels2[:, 0] != labels2[:, 1]) | (labels2[:, 1] != labels2[:, 2])
)

labels2 = labels2[different_hue_mask2]
images2 = images2[different_hue_mask2]

print("Different hue mask applied.")
print(labels2.shape)
print(images2.shape)

# Get rid of images that are not largest or smallest scale
two_sizes_mask2 = (labels2[:, 3] == 0.75) | (labels2[:, 3] == 1.25)

labels2 = labels2[two_sizes_mask2]
images2 = images2[two_sizes_mask2]

print("Two sizes mask applied.")
print(labels2.shape)
print(images2.shape)


# Get rid of images where the orientation is not left, right or frontal (-30, 0, 30)
three_orientations_mask2 = (
    (labels2[:, 5] == -30.0) | (labels2[:, 5] == 0.0) | (labels2[:, 5] == 30.0)
)

labels2 = labels2[three_orientations_mask2]
images2 = images2[three_orientations_mask2]

print("Three orientations mask applied.")
print(labels2.shape)
print(images2.shape)

end = time.time()
print("End time batch 2:", end)

# Concatenate the two batches
images = np.concatenate((images1, images2), axis=0)
labels = np.concatenate((labels1, labels2), axis=0)

print(images.shape)