# ClearML - Hydra Example
#
import hydra
import time
from omegaconf import OmegaConf

from clearml import Task


@hydra.main(config_path="config_files", config_name="config")
def my_app(cfg):
    # type (DictConfig) -> None
    task = Task.init(project_name="Hydra test/addition", task_name="Hydra configuration")
    logger = task.get_logger()
    logger.report_text("You can view your full hydra configuration under Configuration tab in the UI")
    print(OmegaConf.to_yaml(cfg))
    for i in range(40):
        logger.report_scalar(title="title", series="number", value=cfg.foo.number+i, iteration=i)
    logger.report_single_value(name="number", value=13)
    print("my metric name:")
    time.sleep(5)
    print(task.get_reported_scalars())
    print("single value:")
    time.sleep(5)
    print(task.get_reported_single_values())

if __name__ == "__main__":
    my_app()
