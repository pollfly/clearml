Frameworks Examples 
---

ClearML offers extensive support and integrations of popular ML/DL frameworks.

The Frameworks Examples demonstrate how ClearML interfaces transparently with different types of supported frameworks, 
including:
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
  
<!--In many of the examples, depending on the library used, **ClearML** automatically captures a wide range of artifacts and 
outputs from the code. ClearML automatically logs information when standard libraries, like TensorFlow, are used, otherwise, 
information can also be logged explicitly. -->

The following frameworks and examples are included:

### AutoKeras
* [AutoKeras IMDB example](autokeras/autokeras_imdb_example.py) - Training text classification networks on the 
  Keras built-in [IMDB](https://keras.io/api/datasets/imdb/) dataset, using the [autokeras](https://github.com/keras-team/autokeras) 
  `TextClassifier` class. **ClearML** automatically logs TensorFlow definitions and all TensorBoard outputs, including
  the model and scalars.

### Fastai
* [Fastai with Tensorboard](fastai/fastai_with_tensorboard.py) - Training a simple deep neural network on the [fastai](https://github.com/fastai/fastai) 
  built-in MNIST dataset. **ClearML** automatically logs TensorBoard outputs, including a histogram, from the fastai 
  `LearnerTensorboardWriter` callback.

### Hydra
* [Hydra](hydra/hydra_example.py) - Creating a configuration object using Hydra, which is automatically captured
  by **ClearML**. Text is explicitly reported using the `Logger.report_text` method.

### Ignite 
* [Cifar Ignite](ignite/cifar_ignite.py) - Training a network on a CIFAR10 dataset, using Ignite's `TensorboardLogger`, and 
the handlers that can be attached to it. Scalars are logged with `TensorboardLogger` and the model is saved using 
  `torch.save`, both of which **ClearML** automatically logs. Using ClearML's `StorageManager`, the dataset is cached with 
  the `get_local_copy` method. Parameters are explicitly logged using the `task.connect` method.  
  

### Keras
* [Keras with Matplotlib - Jupyter Notebook](keras/jupyter_keras_matplotlib.ipynb) - In Jupyter Notebook,
training a simple deep neural network on the Keras built-in [MNIST](https://keras.io/api/datasets/mnist/#load_data-function) 
  dataset. ClearML automatically logs TensorFlow Definitions. A parameter dictionary is logged explicitly by connecting 
  it to the Task with the `Task.connect` method. The script calls Matplotlib methods to create several sample plots and to 
  log debug sample images, and TensorBoard methods to plot histograms for layer density. These plots and images are 
  automatically logged by **ClearML**.
   
* [Keras with TensorBoard](keras/keras_tensorboard.py) - Training a simple deep NN on the 
  [MNIST](https://keras.io/api/datasets/mnist/#load_data-function) dataset using Keras. **ClearML** automatically logs 
  the argparse arguments and TensorFlow Definitions. In the experiment code, a configuration dictionary is connected to 
  the Task by calling the `Task.connect` method.

* [Keras with TensorBoard - Jupyter Notebook](keras/jupyter_keras_TB_example.ipynb) - The "Keras with TensorBoard" example 
  in a Jupyter Notebook.
  
:::note
Keras examples include a folder of legacy examples for versions of TensorFlow older than v2.0. 
:::

### Keras Tuner
* [Keras Tuner Cifar](kerastuner/keras_tuner_cifar.py) - Using Keras Tuner `Hyperband` 
  tuner to optimize hyperparameters for training a network on a CIFAR10 dataset. When the `Hyperband` object is created, 
  the `ClearMLTunerLogger` is specified as the Keras Tuner logger. **ClearML** automatically logs scalars and a tabular 
  summary of hyperparameters tested and their metrics. **ClearML** also automatically logs the parameters of each experiment 
  run in the hyperparameter search separately.


### LightGBM
* [LightGBM Example](lightgbm/lightgbm_example.py) - Training and loading a model using **LightGBM**. **ClearML** automatically
logs all information logged by LightLGB, including parameters, the model, and metrics.


### Matplotlib

* [Matplotlib](matplotlib/matplotlib_example.py) - Using Matplotlib to plot scatter diagrams, and show images, which are 
  automatically captured by **ClearML**.
  
* [Matplotlib - Jupyter Notebook](matplotlib/jupyter_matplotlib_example.ipynb) - The "Matplotlib" example in a 
  Jupyter Notebook.

### PyTorch

* [Pytorch Distributed](pytorch/pytorch_distributed_example.py) - Using the PyTorch Distributed Communications Package,
  which initializes a main Task and spawns subprocesses, each for an instance of that Task. 
  The Task in each subprocess trains a neural network over a partitioned dataset, and reports artifacts, scalars, and 
  hyperparameters to the main Task. The artifacts and scalars are explicitly reported with `Task.upload_artifact` and 
  `Logger.report_scalar` methods respectively. A parameter dictionary is logged explicitly with the `Task.connect` method. 
  **ClearML** automatically logs the command line options defined using argparse.

  
* [PyTorch MNIST](pytorch/pytorch_mnist.py) - Training a simple deep neural network on the PyTorch built-in 
  [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist) dataset. **ClearML** automatically logs the command line 
  options defined with argparse. The code explicitly reports to ClearML the loss and accuracy scalars with the 
  `Logger.report_scalar` method.
  
* [PyTorch TensorBoard Toy](pytorch/tensorboard_toy_pytorch.py) - Logging debug sample images with Pytorch and TensorBoard. 
  The code instantiates a TensorBoard `SummaryWriter` object to log debug sample images, which **ClearML** captures. 
  
* [PyTorch with Matplotlib](pytorch/pytorch_matplotlib.py) - Logging plots with PyTorch and Matplotlib.
The script calls Matplotlib methods to show images, which **ClearML** automatically logs as debug samples.

* [PyTorch with TensorBoard](pytorch/pytorch_tensorboard.py) - Training a simple deep neural network on the PyTorch built-in 
  [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist) dataset. A TensorBoard `SummaryWriter` object is created
  to log scalars, debug samples, and a text message, which **ClearML** automatically logs. **ClearML** also automatically 
  logs TensorFlow Definitions.

* [PyTorch with TensorBoardX](pytorch/pytorch_tensorboardx.py) - Training a simple deep neural network on the PyTorch 
  built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist) dataset. Creates a TensorBoardX `SummaryWriter` 
  object to log scalars, debug samples, and a text message, which **ClearML** captures. **ClearML** also automatically 
  logs the command line options defined with argparse.

#### Notebooks
Jupyter Notebooks that demonstrate integrating **ClearML** into PyTorch scripts that use various media.

##### Audio

* [Audio Preprocessing - Jupyter Notebook](pytorch/notebooks/audio/audio_preprocessing_example.ipynb) - Using 
  PyTorch and preprocessing audio samples that are logged to **ClearML**. The code reports audio samples by calling TensorBoard 
  methods, and the spectrogram visualizations by calling Matplotlib methods. The samples and visualization are automatically
  captured by **ClearML**. Parameters are explicitly logged by using the `Task.connect` method.
  
* [Audio Classification - Jupyter Notebooks](pytorch/notebooks/audio/audio_classifier_UrbanSound8K.ipynb) - Using PyTorch, 
  TensorBoard, and TorchVision to train a neural network on the UrbanSound8K **audio** classification dataset.
  The code uses TensorBoard methods to report scalars, audio debug samples, and spectrogram visualizations. The spectrogram 
  visualizations are plotted by calling Matplotlib methods. All the Tensorboard outputs are automatically logged by **ClearML**. 
  Parameters are explicitly reported using the `Task.connect` method. 
  
##### Images

* [Hyperparameter Optimization - Jupyter Notebook](pytorch/notebooks/image/hyperparameter_search.ipynb) - Performing 
  automated hyperparameter optimization. The code creates a **ClearML** `HyperParameterOptimizer` object, which is a search 
  controller using the `OptimizerBOHB` search strategy. The example maximizes total accuracy by finding 
  an optimal batch size, base learning rate, and dropout. **ClearML** automatically logs the optimization's top performing 
  experiments.
  
* [Image Classification - Jupyter Notebook](pytorch/notebooks/image/image_classification_CIFAR10.ipynb) - Using PyTorch, 
  TensorBoard, and TorchVision to train a neural network on the UrbanSound8K **image** classification dataset. 
  **ClearML** automatically logs TensorBoard outputs, including scalars and image debug samples, as well as the model. 
  Parameters are explicitly logged using `Task.connect`.

##### Tables

The scripts below demonstrate a pipeline with concurrent tasks using tabular data. 

* [Download and Split](pytorch/notebooks/table/download_and_split.ipynb) - Task to download data, which will be 
  processed in the Tabular ML Pipeline.
* [Tabular ML Pipeline](pytorch/notebooks/table/tabular_ml_pipeline.ipynb) - The pipeline controller Task for a pipeline 
  with nodes that run concurrently to preprocess two sets of **tabular** data, train on each, and select the better model. 
  
  The pipeline consists of the following steps:
  * [Preprocessing and Encoding](pytorch/notebooks/table/preprocessing_and_encoding.ipynb) - A data preprocessing Task. 
  * [Tabular Predictor](pytorch/notebooks/table/train_tabular_predictor.ipynb) - Training and validation of the model using
  the data from the previous step's artifacts.
  * [Pick Best Model](pytorch/notebooks/table/pick_best_model.ipynb) - A comparison Task to pick out the best model.  
  
##### Text

* [Text Classification](pytorch/notebooks/text/text_classification_AG_NEWS.ipynb) - Training a network to classify **text** 
  in the `torchtext` AG_NEWS dataset, and then applying the model on a sample text. 
  Text, scalars, and console output are logged by calling TensorBoard methods, which are automatically captured by **ClearML**. 
  **ClearML** also automatically logs the command line options defined with argparse. A parameter dictionary is logged 
  explicitly with the `Task.connect` method.


### Pytorch Lightening
* [Pytorch Lightening Example](pytorch-lightning/pytorch_lightning_example.py) - Training a neural network on the MNIST dataset, 
  using Pytorch Lightning. **ClearML** automatically captures the models and artifacts output from
  PyTorch Lightning methods.

### scikit-learn

* [scikit-learn with Joblib](scikit-learn/sklearn_joblib_example.py) - Training a model using the [iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.md#sklearn.datasets.load_iris) 
  classification dataset. **ClearML** automatically logs a model and model snapshot created in code that uses `scikit-learn` 
  and `joblib`, as well as a scatter plot created by Matplotlib.
  
* [scikit-learn with Matplotlib](scikit-learn/sklearn_matplotlib_example.py) - Using 
  `scikit-learn` to determine cross-validated training and test scores, and Matplotlib to plot the learning curves. 
  **ClearML** automatically logs the scatter diagrams for the learning curves.
  
### TensorBoardX

* [TensorBoardX](tensorboardx/pytorch_tensorboardX.py) - Training a simple deep neural network on the PyTorch built-in MNIST dataset.
The code creates a TensorBoardX `SummaryWriter` object to log scalars, debug samples, and a text message to the console, 
  all of which **ClearML** automatically logs. **ClearML** also automatically logs the command line options defined with 
  argparse.
  
* [TensorBoardX Movie Example](tensorboardx/moviepy_tensorboardx.py) - Using PyTorch to create video.
  The code creates a TensorBoardX `SummaryWriter` object to log text and a video, which is automatically captured by **ClearML**
  as debug samples. 

### TensorFlow

The TensorFlow examples demonstrate **ClearML**'s automagical capabilities in scripts using TensorFlow.

* [TensorBoard PR Curve](tensorflow/tensorboard_pr_curve.py) - Computing the probability of 
  generated colors belonging to a certain class. Tensorflow methods generate PR curves using the probabilities computed. 
  **ClearML** automatically logs the TensorBoard output, TensorFlow Definitions, and output to the console.
  
* [TensorBoard Toy](tensorflow/tensorboard_toy.py) - Demonstrating **ClearML**'s automatic logging of TensorBoard scalars, 
  histograms, images, and text, as well as all other console output and TensorFlow Definitions.
  
* [TensorFlow MNIST](tensorflow/tensorflow_mnist.py) - Using TensorFlow and Keras to train a neural network on the Keras 
  built-in [MNIST](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist.md) 
  dataset. Model checkpoints, TensorFlow definitions, and scalars are logged using TensorFlow methods, and these are automatically
  captured by **ClearML**.
  
* [absl flags](tensorflow/absl_flags.py) - Using `absl.flags` that are automatically logged by **ClearML** 


:::note
TensorFlow examples include a legacy examples folder for versions of TensorFlow older than v2.0. 
:::


### XGBoost

* [XGBoost](xgboost/xgboost_sample.py) - Training a network on the scikit-learn 
  [iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.md#sklearn.datasets.load_iris) 
  classification dataset. XGBoost loads and saves a model, dumps a model to JSON or text file, plots feature importance 
  and a tree, and used scikit-learn to score accuracy. **ClearML** automatically logs all of XGBoost's outputs.
