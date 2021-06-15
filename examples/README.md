Examples
---

To help learn and use **ClearML**, example scripts are provided. 

The examples include: 
* Ready to run examples - These demonstrate **ClearML Python Package**, **ClearML Web UI**, and **ClearML Server** features. 
  These scripts are pre-loaded in the **ClearML Server**  in the `ClearML Examples` project. Their status is *Published*,
and they can be cloned, edited, and enqueued.
  
* Configurable services examples - These perform various customizable functions (for example, Task status alerts and old 
  Task cleanup), which continue running on **ClearML Server**. 
  They execute in [ClearML Agent services mode](https://clear.ml/docs/latest/docs/clearml_agent#services-mode). 
  
Each examples folder contains a ``requirements.txt`` file for the scripts in that folder.

The Examples folder includes the following sections: 
* [Advanced](advanced/README.md) - Additional ClearML tools.
* [Automation](automation/README.md) - Automating processes when using ClearML.
* [ClearML Agent](clearml_agent/README.md) - Usage examples of ClearML Agent.
* [Distributed](distributed/README.md) - Distributed training using ClearML.
* [Frameworks](frameworks/README.md) - Using **ClearML** with other Python packages, including:
  * AutoKeras
  * Fastai
  * Hydra
  * Keras (includes legacy examples of TensorFlow older than v2.0.)
  * Keras Tuner
  * Matplotlib 
  * PyTorch 
  * Pytorch Lightening 
  * scikit-learn 
  * TensorBoardX 
  * TensorFlow (includes legacy examples of TensorFlow older than v2.0.)
  * XGBoost 
* [Optimization](optimization/hyper-parameter-optimization/README.md) - **ClearML**'s automated hyperparameter optimization.  
* [Pipeline](pipeline/README.md) - A basic pipeline to download data, process it, and a train a network. 
* [Reporting](reporting/README.md)  - **ClearML**'s automatic and explicit reporting capabilities.
* [Services](services/README.md) - Configurable services - autoscaler, cleanup, monitoring.
