# Malaria-Parasites-Detection
This code implements a malaria disease detection model using a Convolutional Neural Network (CNN) with data augmentation. The dataset consists of two classes: "Infected" and "Uninfected" cell images. 
Import Necessary Libraries: Import required Python libraries, including TensorFlow, Keras, NumPy, pandas, Matplotlib, and Seaborn.
Load the Dataset: The cell images are loaded from the specified directory and labeled accordingly. The data is then organized into a Pandas DataFrame.
Split the Dataset: The dataset is divided into training and testing sets using the train_test_split function from sklearn.model_selection.
Preprocess the Images: Images are preprocessed using the ImageDataGenerator class from Keras, which applies data augmentation techniques like rescaling, shearing, zooming, and horizontal flipping.
Build the CNN Model: A sequential model is created, consisting of convolutional and pooling layers, followed by fully connected layers with dropout regularization. The model is compiled using the Adam optimizer and binary cross-entropy loss.
Train the Model: The model is trained on the training dataset with early stopping criteria to prevent overfitting.
Evaluate the Model: The trained model is evaluated on the test dataset, and its accuracy and loss are printed.
Plot Accuracy Trend: The training and validation accuracy trends are plotted using Matplotlib and saved as an image named "Tr&V accuracy.png."
Plot Loss and Accuracy Trend: The training loss and accuracy trends are plotted using Matplotlib and saved as an image named "Malaria Model.png."
Please note that the dataset path (data_dir) needs to be adjusted to the appropriate location in your local system.
