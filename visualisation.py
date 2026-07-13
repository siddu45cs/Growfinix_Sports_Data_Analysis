import plotly.express as px


class Visualizer:

    @staticmethod
    def team_wins_chart(stats):

        stats = stats.sort_values("Wins", ascending=False)

        fig = px.bar(
            stats,
            x=stats.index,
            y="Wins",
            text="Wins",
            color="Wins",
            title="Top Teams by Wins"
        )

        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Team",
            yaxis_title="Wins"
        )

        return fig


    @staticmethod
    def win_percentage_chart(stats):

        stats = stats.sort_values(
            "Win Percentage",
            ascending=False
        )

        fig = px.bar(
            stats,
            x=stats.index,
            y="Win Percentage",
            text="Win Percentage",
            color="Win Percentage",
            title="Winning Percentage"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        return fig