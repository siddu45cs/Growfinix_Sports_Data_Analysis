from src.data_loader import DataLoader
from src.data_cleaning import DataCleaner
from src.team_analysis import TeamAnalysis
from src.menu import Menu


class IPLDashboard:
    """
    IPL Sports Analytics Dashboard

    This class acts as the controller of the application.
    It loads the data, initializes all analysis modules,
    and controls the application flow.
    """

    def __init__(self):

        # Data
        self.matches = None
        self.deliveries = None

        # Analysis Modules
        self.team_analysis = None

    # ----------------------------------------
    # Initialize System
    # ----------------------------------------

    def initialize(self):

        print("\nLoading IPL Datasets...\n")

        # Load datasets
        loader = DataLoader()

        matches = loader.load_matches()
        deliveries = loader.load_deliveries()

        # Clean datasets
        cleaner = DataCleaner(matches, deliveries)

        self.matches, self.deliveries = cleaner.clean()

        # Initialize modules
        self.team_analysis = TeamAnalysis(
            self.matches,
            self.deliveries
        )

        print("\n✓ IPL Dashboard Initialized Successfully!")

    # ----------------------------------------
    # Team Analysis Menu
    # ----------------------------------------

    def team_menu(self):

        while True:

            print("\n" + "=" * 50)
            print("        TEAM PERFORMANCE ANALYSIS")
            print("=" * 50)

            print("1. View Team Statistics")
            print("2. Top 5 Teams")
            print("3. Search Team")
            print("4. Team Rankings")
            print("5. Home/Away Performance")
            print("6. Highest Team Scores")
            print("7. Lowest Team Scores")
            print("8. Export Statistics")
            print("0. Back")

            choice = input("\nEnter Choice : ")

            if choice == "1":

                print(self.team_analysis.team_statistics())

            elif choice == "2":

                print(self.team_analysis.top_teams())

            elif choice == "3":

                team = input("\nEnter Team Name : ")

                print(self.team_analysis.search_team(team))

            elif choice == "4":

                print(self.team_analysis.team_ranking())

            elif choice == "5":

                team = input("\nEnter Team Name : ")

                print(
                    self.team_analysis.home_away_performance(team)
                )

            elif choice == "6":

                print(
                    self.team_analysis.highest_team_score()
                )

            elif choice == "7":

                print(
                    self.team_analysis.lowest_team_score()
                )

            elif choice == "8":

                self.team_analysis.export_statistics()

            elif choice == "0":

                break

            else:

                print("Invalid Choice!")

    # ----------------------------------------
    # Main Dashboard
    # ----------------------------------------

    def run(self):

        self.initialize()

        while True:

            Menu.display()

            choice = Menu.get_choice()

            if choice == 1:

                self.team_menu()

            elif choice == 2:

                print("\nPlayer Analysis Module Coming Soon...")

            elif choice == 3:

                print("\nTeam Comparison Module Coming Soon...")

            elif choice == 4:

                print("\nToss Analysis Module Coming Soon...")

            elif choice == 5:

                print("\nVenue Analysis Module Coming Soon...")

            elif choice == 6:

                print("\nSeason Analysis Module Coming Soon...")

            elif choice == 7:

                print("\nScore Analysis Module Coming Soon...")

            elif choice == 8:

                print("\nVisualization Module Coming Soon...")

            elif choice == 9:

                self.team_analysis.export_statistics()

            elif choice == 10:

                print("\nDashboard Summary Coming Soon...")

            elif choice == 0:

                print("\nThank You for Using IPL Sports Analytics Dashboard")

                break

            else:

                print("Invalid Choice!")