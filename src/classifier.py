from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from darkflow.net.build import TFNet
import cv2

print("TensorFlow version: ",tf.__version__)

options = {"model": "doc_seg/cfg/tiny-yolo-voc-6c.cfg","load": -1, "train": True, "gpu": 0.8, "epoch": 50, "dataset": "doc_seg/dokumenty/learn/", "annotation": "doc_seg/dokumenty/learn/" , "labels": "doc_seg/dok_lab.txt"}

tfnet = TFNet(options)
tfnet.train()