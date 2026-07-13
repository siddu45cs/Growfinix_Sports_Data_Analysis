import streamlit as st

from src.dashboard_data import DashboardData
from src.team_analysis import TeamAnalysis
from src.visualisation import Visualizer


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="IPL Sports Analytics Dashboard",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    dashboard = DashboardData()

    return dashboard.load_data()


matches, deliveries = load_data()

analysis = TeamAnalysis(matches, deliveries)

stats = analysis.team_statistics()


# --------------------------------------------------
# DASHBOARD STATS
# --------------------------------------------------

total_matches = len(matches)

total_teams = len(
    set(matches["team1"]).union(set(matches["team2"]))
)

total_players = deliveries["batsman"].nunique()

total_seasons = matches["season"].nunique()

total_venues = matches["venue"].nunique()

highest_score = (
    deliveries
    .groupby(["match_id", "batting_team"])["total_runs"]
    .sum()
    .max()
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🏏 IPL Analytics Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Team Analysis",
        "About"
    ]
)


# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    st.title("🏏 IPL Sports Analytics Dashboard")

    st.markdown("### IPL Data Analysis using Python, Pandas and Streamlit")

    st.divider()

    c1, c2, c3 = st.columns(3)

    c4, c5, c6 = st.columns(3)

    c1.metric("🏏 Matches", total_matches)
    c2.metric("👥 Teams", total_teams)
    c3.metric("🧑 Players", total_players)

    c4.metric("📅 Seasons", total_seasons)
    c5.metric("🏟 Venues", total_venues)
    c6.metric("🔥 Highest Score", highest_score)

    st.divider()

    st.subheader("🏆 Team Statistics")

    st.dataframe(
        stats,
        use_container_width=True
    )

    st.divider()

    st.subheader("📊 Team Wins")

    fig = Visualizer.team_wins_chart(stats)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("📈 Winning Percentage")

    fig2 = Visualizer.win_percentage_chart(stats)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ==================================================
# TEAM ANALYSIS
# ==================================================

elif page == "Team Analysis":

    st.title("📊 Team Analysis")

    teams = sorted(stats.index.tolist())

    team = st.selectbox(
        "Select Team",
        teams
    )

    st.subheader(team)

    st.dataframe(
        analysis.search_team(team),
        use_container_width=True
    )

    st.subheader("🏠 Home / Away Performance")

    st.json(
        analysis.home_away_performance(team)
    )

    st.subheader("📅 Season-wise Wins")

    st.bar_chart(
        analysis.season_wins(team)
    )

    st.subheader("🔥 Highest Team Scores")

    st.dataframe(
        analysis.highest_team_score(),
        use_container_width=True
    )

    st.subheader("📉 Lowest Team Scores")

    st.dataframe(
        analysis.lowest_team_score(),
        use_container_width=True
    )

    if st.button("Export Team Statistics"):

        analysis.export_statistics()

        st.success(
            "Statistics exported successfully!"
        )


# ==================================================
# ABOUT
# ==================================================

elif page == "About":

    st.title("ℹ About")

    st.write("""
# IPL Sports Analytics Dashboard

### Developed Using

- Python
- Pandas
- Streamlit
- Plotly

### Features

- Team Analysis
- Interactive Charts
- Winning Percentage
- Highest Score Analysis
- Home & Away Performance
- CSV Export

### Internship

Growfinix Python Development Internship
""")