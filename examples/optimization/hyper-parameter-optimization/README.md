Optimization Examples
---

These scripts demonstrate **ClearML**'s automated hyperparameter optimization.

* Hyperparameter Optimization - **ClearML**'s automated hyperparameter optimization.
    * [Hyper Parameter Optimizer](optimization/hyper-parameter-optimization/hyper_parameter_optimizer.py) - This script
      is the hyperparameter optimization controller. It makes use of **ClearML**'s `HyperParameterOptimizer` class. 
    * [Base Template Keras](optimization/hyper-parameter-optimization/base_template_keras_simple.py) - The experiment
    which is being optimized. The experiment will repeat with various values of specified hyperparameters, according to 
      the configurations set in the Hyper Parameter Optimizer script. 
    