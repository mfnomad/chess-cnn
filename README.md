# Chess AI

## 🏆 Project Overview

The goal of this project is to develop a chess-move predicting AI using  a Convolutional Neural Network (CNN)  architecture trained on a large dataset of chess moves. The goal is to predict optimal moves based on board positions.

## 🚀 Features

- **Deep Learning Model**: Uses a CNN for board evaluatiotion. Takes as Input the current chess board state and outputs an integer, which can be mapped to a corresponding map using a integer-> move dictionary.
- **9-Channel Board Representation**: Encodes chess positions for neural network processing.
- Trained on GPUs using a VM in the cloud provided by **Kaggle Notebooks**


## 📂 Project Structure

```
📦 chess-cnn
├── 📁 data                  
├── 📁 models                
├── 📁 src                   
│   ├── chess-ai.ipynb                  
├── 📄 README.md              
└── 📄 LICENSE                
```

