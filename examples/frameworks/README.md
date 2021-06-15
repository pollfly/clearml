Frameworks Examples 
---

ClearML offers extensive support and integrations of popular ML/DL frameworks.
The Frameworks Examples demonstrate how ClearML integrates transparently with available tools.   

ClearML interfaces transparently with different types of supported frameworks, including:
* Model building and development engines 
  * [Keras](#keras)
  * [scikit-learn](#scikit-learn) 
  * [PyTorch](#pytorch)
  * [Tensorflow](#tensorflow)
* High-level helper frameworks
  * [AutoKeras](#autokeras)
  * [Fast AI](#fastai)   
  * [PyTorch Ignite](#ignite)
  * [PyTorch Lightning](#pytorch-lightening)
* Logging instrumentation - Configuration and data management and visualization
  * [Matplotlib](#matplotlib)
  * [Hydra](#hydra) 
  * Tensorboard
  * [TensorBoardX](#tensorboardx)
* Hyperparameter Optimization
  * [Keras Tuner](#keras-tuner)
* Gradient Booster
  * [XGBoost](#xgboost) 
  * [LightGBM](#lightgbm)

The Examples folder include the following frameworks and examples:

### AutoKeras
* [AutoKeras IMDB example](autokeras/autokeras_imdb_example.py) - Demonstrates **ClearML**'s automagical logging in code 
  that uses [autokeras](https://github.com/keras-team/autokeras)


### Fastai

* [Fastai with Tensorboard](fastai/fastai_with_tensorboard.py) - **ClearML**'s automagical logging in code that uses [fastai](https://github.com/fastai/fastai) 
  and TensorBoard.

### Hydra
* [Hydra](hydra/hydra_example.py) - Creating and updating a configuration object using Hydra, which is automatically captured
  by **ClearML**.

### Ignite
* [Cifar Ignite](ignite/cifar_ignite.py) - Training a network on a CIFAR10 dataset using Ignite, demonstrating manual logging
of configuration to **ClearML** and **ClearML**'s automagical logging. 


### Keras

* [Keras with Matplotlib - Jupyter Notebook](keras/jupyter_keras_matplotlib.ipynb) - Integrating ClearML in Jupyter 
  Notebook that uses Keras and Matplotlib. Demonstrates automatic logging of models and TensorBoard outputs. 
* [Keras with TensorBoard](keras/keras_tensorboard.py) - Training a simple deep NN on the MNIST dataset using Keras. 
  Integrating **ClearML** into code which uses Keras and TensorBoard.
* [Keras with TensorBoard - Jupyter Notebook](keras/jupyter_keras_TB_example.ipynb) - The "Keras with TensorBoard" example 
  in a Jupyter Notebook.
  
:::note
Keras examples include a folder of legacy examples for versions of TensorFlow older than v2.0. 
:::

### Keras Tuner

* [Keras Tuner Cifar](kerastuner/keras_tuner_cifar.py) - Using Keras Tuner `Hyperband` 
  tuner to optimize hyperparameters for training a network on a CIFAR10 dataset. **ClearML** automatically logs the data.

### LightGBM
* [LightGBM Example](lightgbm/lightgbm_example.py) - **ClearML** automatically logs models created with LightGBM.


### Matplotlib

* [Matplotlib](matplotlib/matplotlib_example.py) - Using Matplotlib to plot scatter 
  diagrams, and show images, which are captured by **ClearML**.
* [Matplotlib - Jupyter Notebook](matplotlib/jupyter_matplotlib_example.ipynb) - The "Matplotlib" example in a 
  Jupyter Notebook.

### PyTorch

The examples below demonstrate **ClearML** automagical capabilities in scripts using PyTorch
* [PyTorch MNIST](pytorch/pytorch_mnist.py) - Training a simple deep neural network 
  on the PyTorch built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist) dataset. 
* [PyTorch TensorBoard Toy](pytorch/tensorboard_toy_pytorch.py) - PyTorch and TensorBoard to log debug sample images.
* [PyTorch with Matplotlib](pytorch/pytorch_matplotlib.py) - PyTorch and Matplotlib to log plots.
* [PyTorch with TensorBoard](pytorch/pytorch_tensorboard.py) - Training and network with PyTorch.
* [PyTorch with TensorBoardX](pytorch/pytorch_tensorboardx.py) - PyTorch and TensorBoardX.

#### Notebooks
Jupyter Notebooks that demonstrate integrating **ClearML** into PyTorch scripts that use various media.

##### Audio

* [Audio Preprocessing - Jupyter Notebook](pytorch/notebooks/audio/audio_preprocessing_example.ipynb) - Using 
  PyTorch and preprocessing audio samples that are logged to **ClearML**.
* [Audio Classification - Jupyter Notebooks](pytorch/notebooks/audio/audio_classifier_UrbanSound8K.ipynb) - Using PyTorch, 
  TensorBoard, and TorchVision to train a neural network on the 
  UrbanSound8K dataset for **audio** classification.

##### Images

* [Hyperparameter Optimization - Jupyter Notebook](pytorch/notebooks/image/hyperparameter_search.ipynb) - Performing 
  automated hyperparameter optimization.
* [Image Classification - Jupyter Notebook](pytorch/notebooks/image/image_classification_CIFAR10.ipynb) - Using PyTorch, 
  TensorBoard, and TorchVision to train a neural network on the UrbanSound8K dataset for **image** classification.

##### Tables

Demonstrates a pipeline with concurrent tasks using tabular data. 

* [Download and Split](pytorch/notebooks/table/download_and_split.ipynb) - Task to downloading data, which will be 
  processed in the Tabular ML Pipeline
* [Tabular ML Pipeline](pytorch/notebooks/table/tabular_ml_pipeline.ipynb) - The pipeline controller Task for a pipeline 
  with nodes that run concurrently to preprocess two sets of **tabular** data, train on each, and select the better model. The pipeline consists of the following
  steps:
  * [Preprocessing and Encoding](pytorch/notebooks/table/preprocessing_and_encoding.ipynb) - A data preprocessing Task. 
  * [Tabular Predictor](pytorch/notebooks/table/train_tabular_predictor.ipynb) - Training and validation of the model using
  the data from the previous step's artifacts.
  * [Pick Best Model](pytorch/notebooks/table/pick_best_model.ipynb) - A comparison Task to pick out the best model.  
  

##### Text

* [Text Classification](pytorch/notebooks/text/text_classification_AG_NEWS.ipynb) - Jupyter Notebook 
  that trains a network to classify text in the `torchtext` AG_NEWS dataset, and then applies the model to predict the 
  classification of sample text. **ClearML** logs the text.

### Pytorch Lightening
* [Pytorch Lightening Example](pytorch-lightning/pytorch_lightning_example.py) - **ClearML**'s automagical logging from a 
  script that uses PyTorch Lightening

### scikit-learn

* [scikit-learn with Joblib](scikit-learn/sklearn_joblib_example.py) - **ClearML** stores a model and model snapshot
  created in code that uses `scikit-learn` and `joblib`, as well as scatter plot created by Matplotlib.
* [scikit-learn with Matplotlib](scikit-learn/sklearn_matplotlib_example.py) - Using 
  `scikit-learn` to determine cross-validated training and test scores, and `matplotlib` to plot the learning curves. 
  **ClearML** automatically logs the scatter diagrams for the learning curves.

### TensorBoardX

* [TensorBoardX](tensorboardx/pytorch_tensorboardX.py) - Using PyTorch and TensorBoardX, with **ClearML**'s automagical logging
* [TensorBoardX Movie Example](tensorboardx/moviepy_tensorboardx.py) - Using PyTorch and TensorBoardX,
  which creates videos in TensorBoard that are logged automatically to **ClearML**.

### TensorFlow

The TensorFlow examples demonstrate **ClearML**'s automagical capabilities in scripts using TensorFlow.
* [TensorBoard PR Curve](tensorflow/tensorboard_pr_curve.py) - Using TensorFlow and 
  TensorBoard.
* [TensorBoard Toy](tensorflow/tensorboard_toy.py) - Kogging of TensorBoard scalars, histograms, 
  images, and text, as well as all other console output and TensorFlow Definitions.
* [TensorFlow MNIST](tensorflow/tensorflow_mnist.py) - Using TensorFlow and Keras 
  to train a neural network on the Keras built-in [MNIST](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist.md) 
  dataset.
* [absl flags](tensorflow/absl_flags.py) - Using `absl.flags` that are automatically logged by **ClearML** 

:::note
TensorFlow examples include a legacy examples folder for versions of TensorFlow older than v2.0. 
:::


### XGBoost

* [XGBoost](xgboost/xgboost_sample.py) - Training a network on the scikit-learn 
  [iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.md#sklearn.datasets.load_iris) 
  classification dataset, and XGBoost.
