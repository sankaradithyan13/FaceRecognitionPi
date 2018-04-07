Face Recognition Based Attendance System
==========================================

Raspberry Pi powered face recognition system using USB Webcam.

In today’s fast paced world, for an organization with around 500 employees, a manual attendance system is highly inefficient and time consuming. Traditional methods of automatic attendance systems like fingerprint, RFID or iris scans are easy to bypass as the biometric features such systems take into consideration are far less than facial features. Our facial recognition system is used to detect a person’s face and then compare it with the stored facial database to recognize it. Once the face is recognized, his attendance is marked along with his in-time and out-time and stored in a database. This paper proposes a system which uses Haar Cascade method for facial detection integrated with Principal Component Analysis (PCA) technology for facial recognition. This whole process is carried out on a Raspberry Pi B+ Module using OpenCV (Open Source Computer Vision) library installed on it. The attendance database is created in MySQL which keeps a record of employee in-time and out-time. Proposed biometric face recognition system is basically used in three domains: employee management, leave management, time attendance system and last but not the least can be used as authorization and access control systems

This project has following objectives which are fulfilled using OpenCV: -
1. Capture the faces to create a database.
2. Train the recognizer for these faces.
3. Detect the face in a real time captured image.
4. Recognize the detected face by comparing with database.
5. Blink LED to show the user whether valid entry or not.
6. Store the in-time and out-time of a valid entry.
7. Link the stored database with a Centralized Server.
