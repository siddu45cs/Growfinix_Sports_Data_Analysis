class Menu:

    @staticmethod
    def display():

        print("\n" + "=" * 65)
        print("          IPL SPORTS ANALYTICS DASHBOARD")
        print("=" * 65)

        print("1. Team Performance Analysis")
        print("2. Player Performance Analysis")
        print("3. Team Comparison")
        print("4. Toss Analysis")
        print("5. Venue Analysis")
        print("6. Season Analysis")
        print("7. Score Analysis")
        print("8. Interactive Visualizations")
        print("9. Export Reports")
        print("10. Dashboard Summary")
        print("0. Exit")

        print("=" * 65)

    @staticmethod
    def get_choice():

        while True:

            try:

                choice = int(input("\nEnter your choice : "))

                if 0 <= choice <= 10:
                    return choice

                print("Please enter a number between 0 and 10.")

            except ValueError:

                print("Invalid input. Please enter a number.")