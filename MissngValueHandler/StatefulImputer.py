from WindowedArray import WindowedArray
class StatefulImputer:
    """
    Impute values while maintaining state.
    This class is a stateful object that encapsulates a
    WindowedArray and provides a method that uses this
    array to impute values.
    The impute_value method of this object is passed to
    op.stateful_map, so the state is maintained across
    calls to this method.
    """

    def __init__(self, window_size):
        """Initialize the stateful imputer.
        Args:
            window_size (int): The size of the window.
        """

        self.windowed_array = WindowedArray(window_size)


    def impute_value(self, key, value):
        """Impute the value in the windowed array."""

        return self.windowed_array.impute_value(value)


