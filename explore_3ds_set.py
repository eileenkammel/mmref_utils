# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
# Date: 2024-09-23 11:34:39


import h5py

dataset = h5py.File("3DS/3dshapes.h5", "r")

images = dataset["images"]  # array shape [480000,64,64,3], uint8 in range(256)
labels = dataset["labels"]  # array shape [480000,6], float64

_FACTORS_IN_ORDER = [
    "floor_hue",
    "wall_hue",
    "object_hue",
    "scale",
    "shape",
    "orientation",
]
_NUM_VALUES_PER_FACTOR = {
    "floor_hue": 10,
    "wall_hue": 10,
    "object_hue": 10,
    "scale": 8,
    "shape": 4,
    "orientation": 15,
}

# Figure out unique values of each attribute

# _FLOOR_HUE = labels[:, 0]
# _UNIQUE_FLOOR_HUE = np.unique(_FLOOR_HUE)
# _NUM_FLOOR_HUE = _UNIQUE_FLOOR_HUE.size
# print("Unique floor hue vals:", _UNIQUE_FLOOR_HUE)
# print(_NUM_FLOOR_HUE)


# _WALL_HUE = labels[:, 1]
# _UNIQUE_WALL_HUE = np.unique(_WALL_HUE)
# _NUM_WALL_HUE = _UNIQUE_WALL_HUE.size
# print("Unique wall hue vals:", _UNIQUE_WALL_HUE)
# print(_NUM_WALL_HUE)

# _OBJECT_HUE = labels[:, 2]
# _UNIQUE_OBJECT_HUE = np.unique(_OBJECT_HUE)
# _NUM_OBJECT_HUE = _UNIQUE_OBJECT_HUE.size
# print("Unique object hue vals:", _UNIQUE_OBJECT_HUE)
# print(_NUM_OBJECT_HUE)

# _SCALE = labels[:, 3]
# _UNIQUE_SCALE = np.unique(_SCALE)
# _NUM_SCALE = _UNIQUE_SCALE.size
# print("Unique scale vals:", _UNIQUE_SCALE)
# print(_NUM_SCALE)

# _SHAPE = labels[:, 4]
# _UNIQUE_SHAPE = np.unique(_SHAPE)
# _NUM_SHAPE = _UNIQUE_SHAPE.size
# print("Unique shape vals:", _UNIQUE_SHAPE)
# print(_NUM_SHAPE)

# _ORIENTATION = labels[:, 5]
# _UNIQUE_ORIENTATION = np.unique(_ORIENTATION)
# _NUM_ORIENTATION = _UNIQUE_ORIENTATION.size
# print("Unique orientation vals:", _UNIQUE_ORIENTATION)
# print(_NUM_ORIENTATION)


_UNIQUE_FLOOR_HUE = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
_UNIQUE_WALL_HUE = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
_UNIQUE_OBJECT_HUE = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
_UNIQUE_SCALE = [
    0.75,
    0.82142857,
    0.89285714,
    0.96428571,
    1.03571429,
    1.10714286,
    1.17857143,
    1.25,
]
_UNIQUE_SHAPE = [0, 1, 2, 3]
_UNIQUE_ORIENTATION = [
    -30.0,
    -25.71428571,
    -21.42857143,
    -17.14285714,
    -12.85714286,
    -8.57142857,
    -4.28571429,
    0.0,
    4.28571429,
    8.57142857,
    12.85714286,
    17.14285714,
    21.42857143,
    25.71428571,
    30.0,
]
