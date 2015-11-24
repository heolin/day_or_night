from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer, RPropMinusTrainer
from pybrain.structure import  LinearLayer,SigmoidLayer

import PIL.Image
import PIL.ImageStat

import numpy as np

from django.conf import settings
import os

def read_image(image_path):
    return np.asarray(PIL.Image.open(image_path))

def get_histogram(image_array):
    result = np.array([0.0 for _ in xrange(256)])
    for x in image_array:
        result[x] += 1.0
    return result

def get_histograms(image):
    w, h, d = image.shape
    image_flat = image.reshape(w * h, d)
    histogram_r = get_histogram(image_flat[:, 0])
    histogram_g = get_histogram(image_flat[:, 1])
    histogram_b = get_histogram(image_flat[:, 2])

    histogram_r_norm = (histogram_r / float(sum(histogram_r))).reshape(256, 1)
    histogram_g_norm = (histogram_g / float(sum(histogram_g))).reshape(256, 1)
    histogram_b_norm = (histogram_b / float(sum(histogram_b))).reshape(256, 1)

    return np.concatenate((histogram_r_norm, histogram_g_norm, histogram_b_norm), axis=0).reshape(768)


def parse(x):
    if x[0] > 0.5:
        return "DAY"
    else:
        return "NIGHT"


from pybrain.tools.xml.networkreader import NetworkReader
network = NetworkReader.readFrom(os.path.join(settings.STATIC_PATH, "network.xml"))

def get(path):
    return network.activate(get_histograms(read_image(path)))[0]




