import pandas as pd


class TeamAnalysis:
    """
    Team Performance Analysis Module
    --------------------------------
    This class performs various analyses on IPL teams.
    """

    def __init__(self, matches, deliveries):
        self.matches = matches
        self.deliveries = deliveries

    # -------------------------------------------------
    # Total Matches Played by Each Team
    # -------------------------------------------------
    def total_matches_played(self):
        teams = pd.concat([
            self.matches["team1"],
            self.matches["team2"]
        ])

        return teams.value_counts().sort_index()

    # -------------------------------------------------
    # Total Wins
    # -------------------------------------------------
    def total_wins(self):
        return self.matches["winner"].value_counts().sort_index()

    # -------------------------------------------------
    # Team Statistics
    # -------------------------------------------------
    def team_statistics(self):

        matches = self.total_matches_played()

        wins = self.total_wins()

        stats = pd.DataFrame({
            "Matches": matches,
            "Wins": wins
        })

        stats = stats.fillna(0)

        stats["Wins"] = stats["Wins"].astype(int)

        stats["Losses"] = stats["Matches"] - stats["Wins"]

        stats["Win Percentage"] = (
            stats["Wins"] /
            stats["Matches"] * 100
        ).round(2)

        stats = stats.sort_values(
            by="Wins",
            ascending=False
        )

        return stats

    # -------------------------------------------------
    # Top N Teams
    # -------------------------------------------------
    def top_teams(self, n=5):
        return self.team_statistics().head(n)

    # -------------------------------------------------
    # Search Team
    # -------------------------------------------------
    def search_team(self, team_name):

        stats = self.team_statistics()

        if team_name in stats.index:
            return stats.loc[team_name]

        return "Team Not Found"

    # -------------------------------------------------
    # Team Matches
    # -------------------------------------------------
    def team_matches(self, team_name):

        return self.matches[
            (self.matches["team1"] == team_name) |
            (self.matches["team2"] == team_name)
        ]

    # -------------------------------------------------
    # Season-wise Wins
    # -------------------------------------------------
    def season_wins(self, team_name):

        season = self.matches[
            self.matches["winner"] == team_name
        ]

        return season.groupby("season").size()

    # -------------------------------------------------
    # Home vs Away Performance
    # -------------------------------------------------
    def home_away_performance(self, team_name):

        home_matches = self.matches[
            self.matches["team1"] == team_name
        ]

        away_matches = self.matches[
            self.matches["team2"] == team_name
        ]

        home_wins = home_matches[
            home_matches["winner"] == team_name
        ].shape[0]

        away_wins = away_matches[
            away_matches["winner"] == team_name
        ].shape[0]

        return {
            "Home Matches": len(home_matches),
            "Home Wins": home_wins,
            "Away Matches": len(away_matches),
            "Away Wins": away_wins
        }

    # -------------------------------------------------
    # Highest Team Score
    # -------------------------------------------------
    def highest_team_score(self):

        scores = (
            self.deliveries
            .groupby(["match_id", "batting_team"])["total_runs"]
            .sum()
            .reset_index()
        )

        return scores.sort_values(
            by="total_runs",
            ascending=False
        ).head(10)

    # -------------------------------------------------
    # Lowest Team Score
    # -------------------------------------------------
    def lowest_team_score(self):

        scores = (
            self.deliveries
            .groupby(["match_id", "batting_team"])["total_runs"]
            .sum()
            .reset_index()
        )

        return scores.sort_values(
            by="total_runs"
        ).head(10)

    # -------------------------------------------------
    # Team Ranking
    # -------------------------------------------------
    def team_ranking(self):

        stats = self.team_statistics()

        stats["Rank"] = range(
            1,
            len(stats) + 1
        )

        return stats

    # -------------------------------------------------
    # Export Statistics
    # -------------------------------------------------
    def export_statistics(
            self,
            filename="outputs/exported_csv/team_statistics.csv"):

        stats = self.team_statistics()

        stats.to_csv(filename)

        print(f"\nStatistics exported to {filename}")