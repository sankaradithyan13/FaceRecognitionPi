"""Raspberry Pi Face Recognition Attendence System Configuration
Copyright 2016 Aeron System Pvt. Ltd. 
"""
# The following values below can be edited to configure the device
# Threshold for the confidence of a recognized face before it's considered a
# positive match.  
# but you might need to tweak this value down if 
# you're getting too many false positives (incorrectly recognized faces), or up
# if too many false negatives (undetected faces).

"""The confidence of a recognized face before it's considered a positive match should
be lesser than this threshold. Confidence values below this threshold will be considered
a positive match because the lower the confidence value, or distance, the more confident
the algorithm is that the face was correctly detected.
"""
Threshold = 70.0

# The face recognizer model will be stored and loaded to this file.
Training_Xml = 'training.xml'

#Subject_Id is used to a holder which contain the subject Id value
Subject_Id = 1

# Subject_Dir is the directory which contain the subject training image data.
Subject_Dir = './training/'
Image_Dir = './img'

# Size (in pixels) to resize images for training and prediction.
# Don't change this unless you also change the size of the training images.
Face_Width  = 92
Face_Height = 112

# Face detection cascade classifier configuration.
# You don't need to modify this unless you know what you're doing.
# See: http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html
Cascade          = 'haarcascade_frontalface_default.xml'
Scale_Factor     = 1.18
Min_Neighbors    = 4
Size_of_Adjacent = (30, 30)

# Filename to use when saving the most recently captured image for debugging.
Recent_Image = 'capture.pgm'

def get_camera():	
	# Use this code for capturing from a webcam:
	  import webcam
	  return webcam.OpenCVCapture(device_id=-1)
