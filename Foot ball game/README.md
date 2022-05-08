# Football game using computer Vision :
### What is a MediaPipe?
- MediaPipe is a Framework for building machine learning pipelines for processing time-series data like video, audio, etc. This cross-platform Framework works in Desktop/Server, Android, iOS, and embedded devices like Raspberry Pi and Jetson Nano.
- MediaPipe powers revolutionary products and services daily. Unlike power-hungry machine learning Frameworks, MediaPipe requires minimal resources. It is so tiny and efficient that even embedded IoT devices can run it. In 2019, MediaPipe opened up a whole new world of opportunity for researchers and developers following its public release. 

### Graphs :
-The MediaPipe perception pipeline is called a Graph. Let us take the example of the first solution, Hands. We feed a stream of images as input which comes out with hand landmarks rendered on the images. 


![mp](https://user-images.githubusercontent.com/64165946/167312070-da8ab58d-ea9d-402f-9bee-261fa87978dd.PNG)

- In computer science jargon, a graph consists of Nodes connected by Edges. Inside the MediaPipe Graph, the nodes are called Calculators, and edges are called Streams. Every stream carries a sequence of Packets that have ascending time stamps. 

- In the image above, we have represented Calculators with rectangular blocks and Streams using arrows. 

### Calculators :

- These are specific computation units written in C++ with assigned tasks to process. The packets of data ( Video frame or audio segment ) enter and leave through the ports in a calculator. When initializing a calculator, it declares the packet payload type that will traverse the port. Every time a graph runs, the Framework implements Open, Process, and Close methods in the calculators. Open initiates the calculator; the process repeatedly runs when a packet enters. The process is closed after an entire graph run.

- All the calculators shown above are built-in into MediaPipe. We can group them into four categories.

    * Pre-processing calculators are family of image and media processing calculators. The ImageTransform and ImageToTensors in the graph above fall in this category.

    * Inference calculators allow native integration with Tensorflow and Tensorflow Lite for ML inference.

    * Post-processing calculators perform ML post-processing tasks such as detection, segmentation, and classification. TensorToLandmark is a post-processing calculator.

    * Utility calculators are a family of calculators performing final tasks such as image annotation.

### About the project :
- This project is a direct application of mediapipe which detects two hands (right and left) for the same person.This can be used in multiple projects such as robot arm,virtual presentation,virtual pointer,distance calculator,... In this particular project it is used to move the two bats in order to keep the ball inside the playground with the help of opencv and cv2 and some calculations of the objects coordinates (x and y).
- This project was done by following the Tuto of Murtaza hassan but with some modification : https://www.youtube.com/watch?v=LIDJzJhlyyg
- Demo Link on Youtube : https://www.youtube.com/watch?v=zwSnqhUkNXI
- Demo :

[![asciicast](https://user-images.githubusercontent.com/64165946/167310704-394ddb17-7fa9-4541-ba15-fd01e8baddba.mp4)](https://user-images.githubusercontent.com/64165946/167310704-394ddb17-7fa9-4541-ba15-fd01e8baddba.mp4)

- Please do not hesitate to send your feedbacks to : khaoula.benali@ensi-uma.tn .
