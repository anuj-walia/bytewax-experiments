import numpy as np
class WindowedArray:
    """Windowed Numpy Array.
    Create a numpy array to run windowed statistics on.
    """

    def __init__(self, window_size: int) -> None:
        """Initialize the windowed array.
        Args:
            window_size (int): The size of the window.
        """

        self.last_n = np.empty(0, dtype=float)
        self.n = window_size


    def push(self, value: float) -> None:
        """Push a value into the windowed array.
        Args:
            value (float): The value to push into the array.
        """

        if np.isscalar(value) and np.isreal(value):
            self.last_n = np.insert(self.last_n, 0, value)
            try:
                self.last_n = np.delete(self.last_n, self.n)
            except IndexError:
                pass


    def impute_value(self) -> float:
        """Impute the next value in the windowed array.
        Returns:
            tuple: A tuple containing the original value and the imputed value.
        """

        return np.nanmean(self.last_n)
