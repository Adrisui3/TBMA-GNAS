from threading import Lock

from .default_values import DEFAULT_HYPERPARAMETERS
from .dimension_ratio import DimensionRatio
from .hyperparameter import HyperParameter


class HyperParameters:
    def __init__(self):
        self.lock = Lock()
        self.ratio = HyperParameter(values=[DimensionRatio.EQUAL, DimensionRatio.REDUCE])
        self.specific_parameters = {
            layer_name: {param_name: HyperParameter(values=DEFAULT_HYPERPARAMETERS[layer_name][param_name]) for
                         param_name in DEFAULT_HYPERPARAMETERS[layer_name].keys()} for layer_name in
            DEFAULT_HYPERPARAMETERS.keys()}

    def query_for_layer(self, layer: str) -> tuple[DimensionRatio, dict]:
        with self.lock:
            return self.ratio.query(), {param_name: self.specific_parameters[layer][param_name].query() for param_name
                                        in
                                        self.specific_parameters[layer].keys()}

    def learn_for_layer(self, layer: str, prev_values: dict, positive: bool) -> None:
        with self.lock:
            for param_name, prev_value in prev_values:
                self.specific_parameters[layer][param_name].learn(prev_value, positive)
