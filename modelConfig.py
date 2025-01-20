# Configure model here
from enum import Enum

class ModelConfig(str, Enum):
    TINY = "tiny"
    BASE = "base"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"