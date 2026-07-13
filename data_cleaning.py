import pandas as pd


class DataCleaner:

    def __init__(self, matches, deliveries):
        self.matches = matches
        self.deliveries = deliveries

    # -----------------------------------
    # Dataset Information
    # -----------------------------------
    def dataset_info(self):

        print("\n========== MATCHES DATASET ==========")
        print(self.matches.info())

        print("\n========== DELIVERIES DATASET ==========")
        print(self.deliveries.info())

    # -----------------------------------
    # Missing Values
    # -----------------------------------
    def check_missing_values(self):

        print("\nMissing Values in Matches Dataset")
        print(self.matches.isnull().sum())

        print("\nMissing Values in Deliveries Dataset")
        print(self.deliveries.isnull().sum())

    # -----------------------------------
    # Remove Duplicates
    # -----------------------------------
    def remove_duplicates(self):

        matches_before = len(self.matches)
        deliveries_before = len(self.deliveries)

        self.matches.drop_duplicates(inplace=True)
        self.deliveries.drop_duplicates(inplace=True)

        matches_removed = matches_before - len(self.matches)
        deliveries_removed = deliveries_before - len(self.deliveries)

        print(f"\n✓ Removed {matches_removed} duplicate rows from matches dataset")
        print(f"✓ Removed {deliveries_removed} duplicate rows from deliveries dataset")

    # -----------------------------------
    # Standardize Column Names
    # -----------------------------------
    def standardize_column_names(self):

        self.matches.columns = (
            self.matches.columns
            .str.lower()
            .str.strip()
        )

        self.deliveries.columns = (
            self.deliveries.columns
            .str.lower()
            .str.strip()
        )

        print("✓ Column names standardized")

    # -----------------------------------
    # Convert Date Column
    # -----------------------------------
    def convert_date(self):

        if "date" in self.matches.columns:

            self.matches["date"] = pd.to_datetime(
                self.matches["date"],
                dayfirst=True,
                errors="coerce"
            )

            print("✓ Date column converted successfully")

    # -----------------------------------
    # Standardize Team Names
    # -----------------------------------
    def standardize_team_names(self):

        replacements = {

            "Delhi Daredevils": "Delhi Capitals",

            "Kings XI Punjab": "Punjab Kings",

            "Rising Pune Supergiant":
                "Rising Pune Supergiants"

        }

        self.matches.replace(replacements, inplace=True)
        self.deliveries.replace(replacements, inplace=True)

        print("✓ Team names standardized")

    # -----------------------------------
    # Remove Matches Without Result
    # -----------------------------------
    def remove_invalid_matches(self):

        if "winner" in self.matches.columns:

            before = len(self.matches)

            self.matches = self.matches[
                self.matches["winner"].notna()
            ]

            removed = before - len(self.matches)

            print(f"✓ Removed {removed} matches with no winner")

    # -----------------------------------
    # Data Quality Report
    # -----------------------------------
    def data_quality_report(self):

        print("\n" + "=" * 50)
        print("DATA QUALITY REPORT")
        print("=" * 50)

        print(f"\nMatches Shape     : {self.matches.shape}")
        print(f"Deliveries Shape  : {self.deliveries.shape}")

        print("\nMatches Columns:")
        print(list(self.matches.columns))

        print("\nDeliveries Columns:")
        print(list(self.deliveries.columns))

    # -----------------------------------
    # Main Cleaning Pipeline
    # -----------------------------------
    def clean(self):

        self.dataset_info()

        self.check_missing_values()

        self.remove_duplicates()

        self.standardize_column_names()

        self.convert_date()

        self.standardize_team_names()

        self.remove_invalid_matches()

        self.data_quality_report()

        print("\n✓ DATA CLEANING COMPLETED SUCCESSFULLY")

        return self.matches, self.deliveries