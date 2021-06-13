Optimization Examples
---

These Optimization Examples demonstrate **ClearML**'s automated hyperparameter optimization.

* [Hyper Parameter Optimizer](hyper_parameter_optimizer.py) - This script
      is the hyperparameter optimization controller. It makes use of **ClearML**'s `HyperParameterOptimizer` class. It
  optimizes the [Base Template Keras](base_template_keras_simple.py) script. 
  
* [Base Template Keras](base_template_keras_simple.py) - The experiment that is being optimized. The experiment will 
  repeat with various values of specified hyperparameters, according to the configurations set in the [Hyper Parameter Optimizer](hyper_parameter_optimizer.py) 
  script. 
    