from torch_geometric import nn as geom_nn

DEFAULT_HYPERPARAMETERS = {
    geom_nn.GATv2Conv.__name__: {
        "heads": [1, 2, 3, 4, 5, 6, 7, 8],
        "negative_slope": [0.1, 0.2, 0.3],
        "dropout": [0, 0.15, 0.25],
        "concat": [True, False]
    },

    geom_nn.GCNConv.__name__: {
        "improved": [True, False],
        "normalize": [True, False]
    }
}
