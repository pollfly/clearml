Examples
---

To help learn and use **ClearML**, we provide example scripts. 

The examples include: 
* Ready to run examples - These demonstrate **ClearML Python Package**, **ClearML Web UI**, and **ClearML Server** features, 
  including **ClearML** automatic logging, explicit reporting, integrating **ClearML** into code with frameworks and visualization 
  tools, automation, and optimization. These scripts are pre-loaded in the **ClearML Server**  in the `ClearML Examples` project. Their status is *Published*,
and they can be cloned, edited, and enqueued.
  
* Configurable services examples - These perform various functions (for example, Task status alerts and old Task cleanup), 
  which continue running on **ClearML Server**. They execute in [ClearML Agent services mode](../../docs/concepts_fundamentals/concepts_fundamentals_clearml_server.md#clearml-agent-services-container). 
  
Each examples folder in the GitHub ``clearml`` repository contains a ``requirements.txt`` file for example scripts in that folder.

The Examples folder includes the following: 
* [Advanced](advanced/README.md) - Additional ClearML tools.
* [Automation](automation/README.md) - Tools to automate processes when using ClearML.
* [ClearML Agent](clearml_agent/README.md) - Usage of ClearML Agent.
* [Distributed](distributed/README.md) - Distributed training using ClearML.
* [Frameworks](frameworks/README.md) - Examples of integrating **ClearML** into code that uses various frameworks, including:
  * AutoKeras
  * Fastai
  * Hydra
  * Keras (includes legacy examples folder for versions of TensorFlow older than v2.0.)
  * Keras Tuner
  * Matplotlib 
  * PyTorch 
  * Pytorch Lightening 
  * scikit-learn 
  * TensorBoardX 
  * TensorFlow (includes legacy examples folder for versions of TensorFlow older than v2.0.)
  * XGBoost 
* [Optimization](optimization/hyper-parameter-optimization/README.md) - Automated hyperparameter optimization  
* [Pipeline](pipeline/README.md) - A basic pipeline to download data, process it, and a train a network. The data is serialized.
* [Reporting](reporting/README.md)  - **ClearML**'s automatic and explicit reporting capabilities.
* [Services](services/README.md) - Configurable services - autoscaler, cleanup, monitoring.
