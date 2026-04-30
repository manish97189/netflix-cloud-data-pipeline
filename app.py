import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Netflix Dark Theme
st.set_page_config(page_title="Netflix Cloud Data Pipeline", layout="wide")

# Custom CSS to make it look exactly like Netflix
st.markdown("""
    <style>
    .stApp {
        background-color: #141414;
        color: white;
    }
    h1, h2, h3 {
        color: #E50914; 
    }
    div[data-testid="stMetricValue"] {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Netflix Global Content Strategy Pipeline")
st.markdown("*Data processed via AWS S3 → AWS Glue Parquet ETL → Amazon Athena*")
st.markdown("---")

# 2. Load the Athena Data
@st.cache_data
def load_data():
    split_df = pd.read_csv("content_split.csv")
    timeline_df = pd.read_csv("timeline.csv")
    countries_df = pd.read_csv("top_countries.csv")
    genres_df = pd.read_csv("top_genres.csv")
    return split_df, timeline_df, countries_df, genres_df

split_df, timeline_df, countries_df, genres_df = load_data()

# 3. KPI Scorecards (Top Row)
total_titles = split_df['total_titles'].sum()
movies_count = split_df[split_df['type'] == 'Movie']['total_titles'].values[0]
tv_count = split_df[split_df['type'] == 'TV Show']['total_titles'].values[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Content on Platform", f"{total_titles:,}")
col2.metric("Total Movies", f"{movies_count:,}")
col3.metric("Total TV Shows", f"{tv_count:,}")

st.markdown("---")

# 4. Charts: Row 1 (Donut and Bar Chart)
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Content Split")
    fig_donut = px.pie(split_df, values='total_titles', names='type', hole=0.5,
                       color_discrete_sequence=['#E50914', '#564d4d'])
    fig_donut.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig_donut, use_container_width=True)

with col_right:
    st.subheader("Top 10 Genres Worldwide")
    fig_genres = px.bar(genres_df, x='genre_count', y='individual_genre', orientation='h',
                        color_discrete_sequence=['#E50914'])
    # Sort bars so the biggest is on top
    fig_genres.update_layout(yaxis={'categoryorder':'total ascending'}, 
                             paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig_genres, use_container_width=True)

st.markdown("---")

# 5. Charts: Row 2 (Area Chart for Timeline)
st.subheader("Content Growth Over Time (Post-2000)")
fig_timeline = px.area(timeline_df, x='release_year', y='total_releases', color='type',
                       color_discrete_sequence=['#E50914', '#ffffff'])
fig_timeline.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
st.plotly_chart(fig_timeline, use_container_width=True)

st.markdown("---")

# 6. Charts: Row 3 (Countries)
st.subheader("Top Content Producing Countries")
fig_countries = px.bar(countries_df, x='country', y='total_content',
                       color_discrete_sequence=['#E50914'])
fig_countries.update_layout(xaxis={'categoryorder':'total descending'}, 
                            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
st.plotly_chart(fig_countries, use_container_width=True)