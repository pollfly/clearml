Frameworks Examples 
---

The examples in this folder demonstrate the integration of **ClearML** into scripts that utilize various frameworks. 

The examples include the following frameworks and examples:

### AutoKeras
* [AutoKeras IMDB example](autokeras/autokeras_imdb_example.py) - Integrating **ClearML** into code that uses [autokeras](https://github.com/keras-team/autokeras)


### Fastai

* [Fastai with Tensorboard](fastai/fastai_with_tensorboard.py) - Integrating **ClearML** into code which uses [fastai](https://github.com/fastai/fastai) 
  and TensorBoard.

### Hydra
* [Hydra](hydra/hydra_example.py) - Creating and updating a configuration object using Hydra and reporting it to a **ClearML** Task.


### Keras

* [Keras with Matplotlib - Jupyter Notebook](keras/jupyter.ipynb) - **ClearML** running in Jupyter Notebook with Keras, 
  Matplotlib, and automatic logging.
* [Keras with TensorBoard](keras/keras_tensorboard.py) - Integrating **ClearML** into code which uses Keras and TensorBoard.
* [Keras with TensorBoard - Jupyter Notebook](keras/jupyter_keras_TB_example.ipynb) - The "Keras with TensorBoard" example 
  in a Jupyter Notebook.

:::note
Keras examples include a folder of legacy examples for versions of TensorFlow older than v2.0. 
:::

<!--***NOT IN KERAS FOLDER OF GITHUB -- DOES THIS FIT ANYWHERE? * [Manual Model Upload](keras/) - **ClearML** tracking of a manually configured model created with Keras, including model checkpoints (snapshots), hyperparameters, and output to the console.-->

### Keras Tuner

* [Keras Tuner Cifar](kerastuner/keras_tuner_cifar.py) - Integrating **ClearML** into code which uses the Keras Tuner `Hyperband` 
  tuner to optimize hyperparameters for training a network on a CIFAR10 dataset. 

### Matplotlib

* [Matplotlib](matplotlib/matplotlib_example.py) - Integrating **ClearML** into code which uses Matplotlib to plot scatter 
  diagrams, and show images.
* [Matplotlib - Jupyter Notebook](matplotlib/jupyter_matplotlib_example.ipynb) - The "Matplotlib" example in a 
  Jupyter Notebook.

### PyTorch

These examples demonstrate integrating **ClearML** into code that uses PyTorch.
<!--* $$$[Manual Model Upload](pytorch/manual_model_upload.md) - **ClearML** tracking of a manually configured model 
created with PyTorch, including model checkpoints (snapshots), and output to the console.-->
* [PyTorch MNIST](pytorch/pytorch_mnist.py) - Integrating **ClearML** into code that trains a simple deep neural network 
  on the PyTorch built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist) dataset.
* [PyTorch TensorBoard Toy](pytorch/tensorboard_toy_pytorch.py) - **ClearML** with PyTorch and TensorBoard to log debug sample images.
* [PyTorch with Matplotlib](pytorch/pytorch_matplotlib.py) - **ClearML** with PyTorch and Matplotlib.
* [PyTorch with TensorBoard](pytorch/pytorch_tensorboard.py) - **ClearML** with PyTorch and TensorBoard.
* [PyTorch with TensorBoardX](pytorch/pytorch_tensorboardx.py) - **ClearML** with PyTorch and TensorBoardX.

#### Notebooks
Jupyter Notebooks that demonstrate integrating **ClearML** into PyTorch scripts that use various media.
##### Audio

* [Audio Preprocessing - Jupyter Notebook](pytorch/notebooks/audio/audio_preprocessing_example.ipynb) - Integrating 
  **ClearML** into a Jupyter Notebook that uses PyTorch and preprocesses audio samples.
* [Audio Classification - Jupyter Notebooks](pytorch/notebooks/audio/audio_classifier_UrbanSound8K.ipynb) - Integrating 
  **ClearML** into a Jupyter Notebook that uses PyTorch, TensorBoard, and TorchVision to train a neural network on the 
  UrbanSound8K dataset for **audio** classification.

##### Images

* [Hyperparameter Optimization - Jupyter Notebook](pytorch/notebooks/image/hyperparameter_search.ipynb) - Integrating 
  **ClearML** into a Jupyter Notebook that performs automated hyperparameter optimization.
* [Image Classification - Jupyter Notebook](pytorch/notebooks/image/image_classification_CIFAR10.ipynb) - Integrating 
  **ClearML** into a Jupyter Notebook that uses PyTorch, TensorBoard, and TorchVision to train a neural network on the 
  UrbanSound8K dataset for **image** classification.

##### Tables
$$$
* [Tabular Data Preprocessing](pytorch/notebooks/table/download_and_preprocessing.ipynb) - **ClearML** stores downloaded training as artifacts.
* See the pipeline example using tabular data, [Pipeline with Concurrent Steps - Tabular Data](pytorch/notebooks/table/train_tabular_predictor.ipynb ***CHECK IF THIS RIGHT< COULD BE THE TABULAR ML PIPELINE FILE).
      $$$ADD SOMEWHERE - * [Pipeline with Concurrent Steps - Tabular Data](pytorch/notebooks/table/tabular_training_pipeline.md) - A pipeline with nodes that run concurrently to preprocess two sets of data, train on each, and select the better model. The data is tabular.
* [Download and Split](pytorch/notebooks/table/download_and_split.ipynb)
* [Pick Best Model](pytorch/notebooks/table/pick_best_model.ipynb)
* [Preprocessing and Encoding](pytorch/notebooks/table/preprocessing_and_encoding.ipynb)
* [Tabular ML Pipeline](pytorch/notebooks/table/tabular_ml_pipeline.ipynb)

##### Text

* [Text Classification](pytorch/notebooks/text/text_classification_AG_NEWS.ipynb) - Integrating **ClearML** into Jupyter Notebook 
  that trains a network to classify text in the `torchtext` AG_NEWS dataset, and then applies the model to predict the 
  classification of sample text.

### Pytorch Lightening
* [Pytorch Lightening Example](pytorch-lightning/pytorch_lightning_example.py) - Integrating **ClearML** into code that 
uses PyTorch Lightening

### scikit-learn

* [scikit-learn with Joblib](scikit-learn/sklearn_joblib_example.py) - Integrating **ClearML** into code which uses `scikit-learn`
  and `joblib` to store a model and model snapshot, and Matplotlib to create a scatter diagram.
* [scikit-learn with Matplotlib](scikit-learn/sklearn_matplotlib_example.py) - Integrating **ClearML** into code that uses 
  `scikit-learn` to determine cross-validated training and test scores, and `matplotlib` to plot the learning curves. 
  **ClearML** automatically logs the scatter diagrams for the learning curves.

### TensorBoardX

* [TensorBoardX](tensorboardx/pytorch_tensorboardX.py) - Integrating **ClearML** into code which uses PyTorch and TensorBoardX.
* [TensorboardX Movie Example](tensorboardx/moviepy_tensorboardx.py) - $$$Integrating **ClearML** into code which uses PyTorch and TensorBoardX.

### TensorFlow

<!--* $$$ NOT THERE [Manual Model Upload](tensorflow/manual_model_upload.md) - **ClearML** tracking of a manually configured model created with TensorFlow, including model checkpoints (snapshots), hyperparameters, and output to the console.-->
* [TensorBoard PR Curve](tensorflow/tensorboard_pr_curve.py) - Integrating **ClearML** into code that uses TensorFlow and 
  TensorBoard.
* [TensorBoard Toy](tensorflow/tensorboard_toy.py) - **ClearML** automatic logging of TensorBoard scalars, histograms, 
  images, and text, as well as all other console output and TensorFlow Definitions.
* [TensorFlow MNIST](tensorflow/tensorflow_mnist.py) - Integrating **ClearML** into code which uses TensorFlow and Keras 
  to train a neural network on the Keras built-in [MNIST](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist.md) handwritten digits dataset.
* [absl flags](tensorflow/absl_flags.py) - Integrating **ClearML** into code that uses absl.flags and then automatically 
  logs the parameters to the Task. $$RIGHT LOCATION?

:::note
TensorFlow examples include legacy an examples folder for versions of TensorFlow older than v2.0. 
:::


### XGBoost

* [XGBoost](xgboost/xgboost_sample.py) - Integrating **ClearML** into code that trains a network on the scikit-learn 
  [iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.md#sklearn.datasets.load_iris) 
  classification dataset, and XGBoost.
