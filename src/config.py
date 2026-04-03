# src/config.py

from omegaconf import OmegaConf


def load_config(env: str = "dev"):
    """
    Load and merge base + environment config
    """

    base_config = OmegaConf.load("config/base.yaml")
    env_config = OmegaConf.load(f"config/{env}.yaml")

    config = OmegaConf.merge(base_config, env_config)

    return config