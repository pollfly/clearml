Reporting Examples
---

The Reporting Examples demonstrate **ClearML**'s automatic and explicit reporting (uploading/logging) capabilities.  

* [3D Plots Reporting](3d_plots_reporting.py) - Reporting series as a surface plot and as a 3D scatter plot. The plots 
  are explicitly reported, using `Logger.report_surface` and `Logger.report_scatter3d` methods. 
* [Artifacts](artifacts.py) - Uploading objects (other than models) to storage as experiment artifacts. Pandas DataFranes,
  local files, dictionaries, image files, and folders are explicitly logged using the `Task.upload_artifact` method. 
  The Pandas object is registered as an object to watch using the `Task.register_artifact` method, and **ClearML** tracks
  the changes made to that object.
  * [Artifacts Retrieval](artifacts_retrieval.py) - Retrieving and printing another Task's artifacts. The [Artifacts](artifacts.py)
  script's artifacts are being retrieved so execute that script before executing this one.
* [Explicit Reporting - Jupyter Notebook](jupyter_logging_example.ipynb) - Several explicit reporting examples 
  running in a Jupyter Notebook, including scalars, plots, media (audio, HTML, images, and video), and text. Scalars
  are logged with the `Logger.report_scalar` methods. 2D and 3D scatter plots, confusion matrices, and historgrams are
  logged using the `Logger.report_scatter2d`, `Logger.report_scatter3d`, `Logger.report_matrix`, and `Logger.report_histogram`
  methods respectively. Audio, HTML, image, and video samples are logged using the `Logger.report_media` methods. Text
  is reported using the `Logger.report_text` method.
* [HTML Reporting](html_reporting.py) - Reporting local HTML files and HTML by URL by using the `Logger.report_media` method.
* [Hyperparameters Reporting](hyper_parameters.py) - Automatic logging of command line options from argparse, and
  TensorFlow Definitions. Explicitly reporting of parameter dictionaries using the `Task.connect` method.
* [Image Reporting](image_reporting.py) - Reporting images in several formats, including NumPy arrays, uint8, uint8 RGB, 
  PIL Image objects, and local files. The images are explicitly reported using the `Logger.report_image` method.
* [Matplotlib Manual Reporting](matplotlib_manual_reporting.py) - Reporting Matplotlib in **ClearML** by calling the `Logger.report_matplotlib_figure` 
  method.
* [Media Reporting](media_reporting.py) - Reporting images, audio, and video using the `Logger.report_media` method. Upload 
  from a local path, provide a BytesIO stream, or provide the URL of media already uploaded to some storage.
* [Configuring Models](model_config.py) - Configuring a model and defining label enumeration. Configuration files and dictionaries
  are explicitly logged using the Task.connect_configuration` method. A label enumeration dictionary is logged using the 
  `Task.connect_label_enumeration` dictionary. 
* [Pandas Reporting](pandas_reporting.py) - Reporting tabular data from Pandas DataFrames and CSV files as tables.
  Tabular data is reported using the `Logger.report_table` method. 
* [Plotly Reporting](plotly_reporting.py) - Reporting Plotly plots in **ClearML** by calling the `Logger.report_plotly` 
  method, and passing it a complex Plotly figure using the figure parameter.
* [Scalars Reporting](scalar_reporting.py) - Reporting scalars explicitly using the `Logger.report_scalar` method.
* [Scatter Hist Confusion Mat Reporting](scatter_hist_confusion_mat_reporting.py) - Reporting series as 2D plots 
  in a histogram, confusion matrix, and 2D scatter plot formats using the `Logger.report_histogram`, `Logger.report_matrix`, 
  and `Logger.report_scatter2d` methods respectively.  
* [Text Reporting](text_reporting.py) - Explicitly reporting text using the `Logger.report_text` method.
* [Using Artifacts](using_artifacts_example.py) - Uploading artifacts to a Task with the `Task.upload_artifact` method, 
  and then accessing and utilizing the artifacts with a different Task.

