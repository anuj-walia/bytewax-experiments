import random
from bytewax.inputs import DynamicSource, StatelessSourcePartition
import numpy as np
class RandomNumpyData(StatelessSourcePartition):
    """Generate a random sequence of numbers with missing values.
    Data Source that generates a sequence
    of 100 numbers, where every 5th number is
    missing (represented by np.nan),
    and the rest are random integers between 0 and 10.
    """

    def __init__(self):
        """Initialize the data source."""
        self._it = enumerate(range(100))


    def next_batch(self):
        """Generate the next batch of data.
        Returns:
            list: A list of tuples containing the data.
                If the index of the item is divisible by 5,
                the data is np.nan, otherwise it is a random
        """

        i, item = next(self._it)
        if i % 5 == 0:
            return [("data", np.nan)]
        else:
            return [("data", random.randint(0, 10))]


class RandomNumpyInput(DynamicSource):
    """Generate random data based on worker distribution.
    Class encapsulating dynamic data generation
    based on worker distribution in distributed processing
    """

    def build(self, step_id, _worker_index, _worker_count):
        """Build the data source."""
        return RandomNumpyData()
