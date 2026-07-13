import pandas as pd
import os


class DataLoader:
    """
    Class to load IPL datasets.
    """

    def __init__(self, data_folder="data"):
        self.data_folder = data_folder

    def load_matches(self):
        """Load matches dataset."""
        path = os.path.join(self.data_folder, "matches.csv")

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        return pd.read_csv(path)

    def load_deliveries(self):
        """Load deliveries dataset."""
        path = os.path.join(self.data_folder, "deliveries.csv")

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        return pd.read_csv(path)