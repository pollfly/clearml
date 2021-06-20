Distributed Examples
---

The Distributed Examples demonstrate distributed training using **ClearML**. 

The Examples include:
* [Subprocess](subprocess_example.py) - Creating multiple subprocesses that interact with and report to a main Task.
* [PyTorch Distributed](pytorch_distributed_example.py) - Integrating **ClearML** into code that uses `torch.distributed`. 
  The script spawns Tasks in subprocesses that train a network, and report artifacts, scalars, and hyperparameters to the main Task.

