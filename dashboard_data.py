from src.data_loader import DataLoader
from src.data_cleaning import DataCleaner


class DashboardData:

    def __init__(self):
        self.matches = None
        self.deliveries = None

    def load_data(self):

        loader = DataLoader()

        matches = loader.load_matches()
        deliveries = loader.load_deliveries()

        cleaner = DataCleaner(matches, deliveries)

        self.matches, self.deliveries = cleaner.clean()

        return self.matches, self.deliveries