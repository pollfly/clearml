Pipeline Examples
---

* [Pipeline Controller](pipeline/pipeline_controller.py) - The pipeline controller script for a basic pipeline, which 
  demonstrates a basic pipeline. The controller overrides parameters in steps and connects the artifacts of a previous 
  step to the next step. The following are the three steps in the pipeline:
    * [Step 1](pipeline/step1_dataset_artifact.py) - script that downloads data
    * [Step 2](pipeline/step2_data_processing.py) - script that processes data 
    * [Step 3](pipeline/step3_train_model.py) - script that trains a network
    