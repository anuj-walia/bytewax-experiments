from typing import Optional, Tuple
import bytewax.operators as op
import numpy as np
from bytewax.connectors.stdio import StdOutSink
from bytewax.dataflow import Dataflow

from MissngValueHandler.WindowedArray import WindowedArray
from RandomData import RandomNumpyInput



flow = Dataflow("map_eg")
input_stream = op.input("input", flow, RandomNumpyInput())
def mapper(
    window: Optional[WindowedArray], orig_value: float
) -> Tuple[Optional[WindowedArray], Tuple[float, float]]:
    """Impute missing values in a stream of numbers."""
    if window is None:
        window = WindowedArray(10)
    if not np.isnan(orig_value):
        window.push(orig_value)
        new_value = orig_value
    else:
        new_value = window.impute_value()  # Calculate derived value.

    return (window, (orig_value, new_value))

imputed_stream = op.stateful_map("impute", input_stream, mapper)
op.output("output", imputed_stream, StdOutSink())
