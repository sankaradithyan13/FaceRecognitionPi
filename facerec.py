import cv2
import glob
import os
import sys
import select
import config
import face
import Database_1

def is_letter_input(letter):
	# Utility function to check if a specific character is available on stdin.
	# Comparison is case insensitive.
	if select.select([sys.stdin,],[],[],0.0)[0]:
		input_char = sys.stdin.read(1)
		return input_char.lower() == letter.lower()
	return False

if __name__ == '__main__':
        count = 0
       
        # Load training data into model
	print 'Loading training data...'
	model = cv2.createLBPHFaceRecognizer()
	model.load(config.Training_Xml)
	print 'Training data loaded!'

	# Initialize camer and box.
	camera = config.get_camera()

	# Move box to locked position.
	print 'Running box...'

	#print 'Press button to lock (if unlocked), or unlock if the correct face is detected.'
	print 'Press Ctrl-C to quit.'

	while True:
		# Check if capture should be made.
		# Check if button is pressed.
		if is_letter_input('c'):
				print 'Button pressed, looking for face...'

				# Check for the positive face and unlock if found.
				image = camera.read()

				# Convert image to grayscale.
				image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

				# Get coordinates of single face in captured image.
				result = face.detect_single(image)

				if result is None:
					print 'Could not detect single face!  Check the image in capture.pgm' \
						  ' to see what was captured and try again with only one face visible.'
					continue
				x, y, w, h = result

				# Crop and resize image to face.
				crop = face.resize(face.crop(image, x, y, w, h))

				# Test face against model.
				label, confidence = model.predict(crop)
			
				if confidence < config.Threshold:
					print 'Recognized face!'

				else:
					print 'Did not recognize face!'
				print 'name = {0} with confidence {1}'.format(label,confidence)
				Database_1.data_entry(label)
