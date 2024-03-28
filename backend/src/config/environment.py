from enum import Enum


class Environment(str, Enum):
    integration = "Integration"
    production = "Production"
