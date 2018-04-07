"""Raspberry Pi Face Recognition Treasure Box
Face Recognition Training Script
Copyright 2013 Tony DiCola 

Run this script to train the face recognition system with positive and negative
training images.  The face recognition model is based on the eigen faces
algorithm implemented in OpenCV.  You can find more details on the algorithm
and face recognition here:
  http://docs.opencv.org/modules/contrib/doc/facerec/facerec_tutorial.html
"""
import fnmatch
import os

import cv2
import numpy as np

import config
import face


Mean = 'mean.png'
Positive_Eigenface = 'positive_eigenface.png'
Negative_Eigenface = 'negative_eigenface.png'

def walk_files(directory, match='*'):
	"""Generator function to iterate through all files in a directory recursively
	which match the given filename match parameter.
	"""
	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)

def prepare_image(filename):
	"""Read an image as grayscale and resize it to the appropriate size for
	training the face recognition model.
	"""
	return face.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

def normalize(X, low, high, dtype=None):
	"""Normalizes a given array in X to a value between low and high.
	Adapted from python OpenCV face recognition example at:
	  https://github.com/Itseez/opencv/blob/2.4/samples/python2/facerec_demo.py
	"""
	X = np.asarray(X)
	minX, maxX = np.min(X), np.max(X)
	# normalize to [0...1].
	X = X - float(minX)
	X = X / float((maxX - minX))
	# scale to [low...high].
	X = X * (high-low)
	X = X + low
	if dtype is None:
		return np.asarray(X)
	return np.asarray(X, dtype=dtype)

if __name__ == '__main__':
	print "Reading training images..."
	faces = []
	labels = []
	pos_count = 0
	neg_count = 0
	# Read all positive images
	for filename in walk_files(config.Subject_Dir, '*.pgm'):
		faces.append(prepare_image(filename))
		directory = os.path.dirname(filename)
                Positive_Label = int(os.path.split(directory)[1].replace("positive_",""))
		labels.append(Positive_Label)
		pos_count += 1
                print 'label = {0} filename = {1}'.format(Positive_Label,filename)
		#POSITIVE_LABEL += 1
	# Read all negative images
	#for filename in walk_files(config.NEGATIVE_DIR, '*.pgm'):
	#	faces.append(prepare_image(filename))
	#	labels.append(config.NEGATIVE_LABEL)
	#	neg_count += 1
	print 'Read', pos_count, 'positive images and', pos_count/10 , 'Subjects'
	
	# Training of the Attendence System
	print 'Training model...'
	model = cv2.createLBPHFaceRecognizer()
	model.train(np.asarray(faces), np.asarray(labels))

	# Save the trained Attendence System
	model.save(config.Training_Xml)
	print 'Training data saved to', config.Training_Xml
