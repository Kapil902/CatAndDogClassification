# CatAndDogClassification

##Setting Up Kaggle API Key:

We create a directory named .kaggle in the user's home directory.
We copy the Kaggle API key (downloaded from the Kaggle profile) into this directory. This key allows us to download datasets from Kaggle using the Kaggle command-line tool.
##Downloading and Extracting the Dataset:

Up next download the "dogs-vs-cats" dataset from Kaggle using the Kaggle CLI. This dataset likely contains a large number of images of both cats and dogs.
Then extract the downloaded ZIP file to the /content directory.
##Importing Necessary Libraries:

We import TensorFlow and Keras, popular deep learning frameworks for building and training neural networks.
Various layers and utilities from Keras are imported for constructing the CNN model.
Creating Data Generators:

Two data generators are created using image_dataset_from_directory. One for the training data (from the train directory) and another for validation data (from the test directory).
The batch size and image size for these generators are specified.
Labels are inferred as integers (0 for cats, 1 for dogs).
##Data Normalization:

A function named "process" is defined to normalize the pixel values of images to be between 0 and 1, as neural networks perform better with input data in this range.
This normalization function is applied to both the training and validation datasets using the map method.
##Creating the CNN Model:

A sequential model is created using Keras.
The model consists of three convolutional layers with increasing numbers of filters, each followed by batch normalization and max-pooling layers.
The convolutional layers use 'relu' activation functions.
After the convolutional layers, a flatten layer is added to transform the 2D feature maps into a 1D vector.
Two dense layers with 'relu' activation and dropout layers are included to prevent overfitting.
Finally, an output layer with a single neuron and 'sigmoid' activation, common for binary classification tasks, is added.
##Model Compilation:

The model is compiled using the 'adam' optimizer and 'binary_crossentropy' loss function, suitable for binary classification tasks.
'Accuracy' is specified as a metric to monitor during training.
##Model Training:

The model is trained using the fit method, providing the training and validation datasets.
Training is performed for 10 epochs, meaning the entire dataset is processed 10 times.
During training, various metrics such as accuracy and loss are monitored and recorded.
##Visualization:

Matplotlib is used to plot the training and validation accuracy and loss over epochs. These plots help visualize how well the model is learning from the data and if it's overfitting or underfitting.
##Testing the Model:

A random cat or dog image is loaded for testing.
The image is resized to match the input size of the model (256x256).
The image is prepared for prediction by reshaping it.
Finally, the model is used to make predictions on this test image.
