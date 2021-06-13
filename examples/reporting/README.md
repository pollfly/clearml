Reporting Examples
---

The Reporting Examples demonstrate **ClearML**'s automatic and explicit reporting (uploading/logging) capabilities.  

* [3D Plots Reporting](3d_plots_reporting.py) - Reporting series as a surface plot and as a 3D scatter plot.
* [Artifacts](artifacts.py) - Uploading objects (other than models) to storage as experiment artifacts.
  * [Artifacts Retrieval](artifacts_retrieval.py) - Retrieving and printing another Task's artifacts. The [Artifacts](artifacts.py)
  script's artifacts are being retrieved so execute that script before executing this one.
* [Explicit Reporting - Jupyter Notebook](jupyter_logging_example.ipynb) - Several explicit reporting examples 
  running in a Jupyter Notebook, including scalars, plots, media (audio, HTML, images, and video), and text.
* [HTML Reporting](html_reporting.py) - Reporting local HTML files and HTML by URL.
* [Hyperparameters Reporting](hyper_parameters.py) - Automatic logging of command line options from argparse, 
  TensorFlow Definitions, and parameter dictionaries, which are explicitly connected to Tasks.
* [Image Reporting](image_reporting.py) - Reporting images in several formats, including NumPy arrays, uint8, uint8 RGB, PIL Image objects, and local files.
* [Matplotlib Manual Reporting](matplotlib_manual_reporting.py) - Reporting Matplotlib in **ClearML** by calling the `Logger.report_matplotlib_figure` method.
* [Media Reporting](media_reporting.py) - Reporting images, audio, and video. Upload from a local path, provide a BytesIO stream, 
  or provide the URL of media already uploaded to some storage.
* [Configuring Models](model_config.py) - Configuring a model and defining label enumeration.
* [Pandas Reporting](pandas_reporting.py) - Reporting tabular data from Pandas DataFrames and CSV files as tables.
* [Plotly Reporting](plotly_reporting.py) - Reporting Plotly plots in **ClearML** by calling the `Logger.report_plotly` 
  method, and passing it a complex Plotly figure using the figure parameter.
* [Scalars Reporting](scalar_reporting.py) - Reporting scalars.
* [Scatter Hist Confusion Mat Reporting](scatter_hist_confusion_mat_reporting.py) - Reporting series as 2D plots 
  in a histogram, confusion matrix, and 2D scatter plot formats.
* [Text Reporting](text_reporting.py) - Explicitly reporting (as compared to automatic logging) text.
* [Using Artifacts](using_artifacts_example.py) - Uploading artifacts to a Task, and then accessing and utilizing the artifacts 
  with a different Task.

