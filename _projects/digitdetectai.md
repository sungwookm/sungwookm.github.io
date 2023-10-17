---
title: 'DigitDetectAI'
date: 2023-10-14
collection: projects
tags:
  - cnn
  - mnist
---
One of the most prominent artificial intelligence applications are in the field of computer vision such as object detection and localization, visual data augmentation, visual navigation, and even in autonomous driving.

As my first stepping stone towards my independent research in computer vision, I developed DigitDetectAI, a RL trained model that takes in user input of a digit ranging from 1-10 and predicts what the user input digit is.

The original development of the project predicted 5 MNIST images at random, with a follow-up development where the model predicted user input images from an empty canvas.

The model was trained with the MNIST data using a CNN model in a **TinyVCG** architecture composed of 4 Conv2D layers, 2 MaxPool2D layers, 1 Flatten and Dense layers each. The model was trained in 10 epochs with an overall accuracy of **99.04%.**

<a href="../../external_files/DigitDetectAI/index.html" class="demo_btn btn" style="text_">DigitDetectAI</a>
