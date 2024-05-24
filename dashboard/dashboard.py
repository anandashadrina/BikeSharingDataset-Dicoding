import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')
    
def create_daily_rentals_df(df):
    daily_rentals_df = df.resample(rule='D', on='dteday').agg({
        "registered": "sum",
        "casual": "sum",
        "cnt": "sum"
    })
    daily_rentals_df = daily_rentals_df.reset_index()
    daily_rentals_df.rename(columns={
        "registered": "total_registered",
        "casual": "total_casual",
        "cnt": "total_customer"
    }, inplace=True)
    
    return daily_rentals_df

def create_monthly_rentals_df(df):
    monthly_rentals_df = df.resample(rule='M', on='dteday').agg({
        "registered": "sum",
        "casual": "sum",
        "cnt": "sum"
    })
    monthly_rentals_df = monthly_rentals_df.reset_index()
    monthly_rentals_df.rename(columns={
        "registered": "total_registered",
        "casual": "total_casual",
        "cnt": "total_customer"
    }, inplace=True)
    
    return monthly_rentals_df

def create_byhour_df(df):
    byhour_df = df.groupby('hr')['cnt'].sum().reset_index()
    byhour_df.rename(columns={"cnt": "total_rentals"}, inplace=True)

    return byhour_df

def create_byseasons_df(df):
    byseason_df = df.groupby(by="season").cnt.sum().reset_index()
    byseason_df.rename(columns={
        "cnt": "Total_Costumer"
    }, inplace=True)
    
    return byseason_df

def create_byweather_df(df):
    byweather_df = df.groupby(by="weathersit").cnt.sum().reset_index()
    byweather_df.rename(columns={
        "cnt": "Total_Costumer"
    }, inplace=True)
    
    return byweather_df

def create_clustering(df):
    clustering = df.groupby(['weekday', 'hr'])['cnt'].sum().unstack()

    return clustering

all_df = pd.read_csv("https://github.com/anandashadrina/BikeSharingDataset-Dicoding/blob/main/dashboard/main_data.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    st.image("https://github.com/anandashadrina/BikeSharingDataset-Dicoding/blob/main/dashboard/logo.png")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]


byhour_df = create_byhour_df(main_df)
daily_rentals_df = create_daily_rentals_df(main_df)
monthly_rentals_df = create_monthly_rentals_df(main_df)
byhour_df = create_byhour_df(main_df)
byseason_df = create_byseasons_df(main_df)
byweather_df = create_byweather_df(main_df)
clustering = create_clustering(main_df)

st.header('Bike Sharing Dashboard 🚲')

st.subheader('Daily Rentals')
 
col1, col2, col3 = st.columns(3)
 
with col1:
    total_rentals = daily_rentals_df.total_customer.sum()
    st.metric("Total Rentals", value=total_rentals)
 
with col2:
    total_registered = daily_rentals_df.total_registered.sum()
    st.metric("Total Registered Customer", value=total_registered)

with col3:
    total_casual = daily_rentals_df.total_casual.sum()
    st.metric("Total Casual Customer", value=total_casual)

st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_rentals_df["dteday"],
    monthly_rentals_df["total_customer"],
    marker='o', 
    linewidth=2,
    color="skyblue"
)
ax.set_xlabel("Month", fontsize=15)
ax.set_ylabel("Total Customers", fontsize=15)
ax.set_title("Monthly Rentals (Total Customers)", fontsize=20)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
ax.grid(True)

st.pyplot(fig)

season_colors = {
    'Winter': 'lightskyblue',
    'Spring': 'lightgreen',
    'Summer': 'gold',
    'Fall': 'lightcoral'
}

weather_colors = {
    'Clear':'gold', 
    'Cloudy':'lightskyblue', 
    'Light Snow/Rain':'grey', 
    'Heavy Rain/Ice Pallets':'darkblue'
}

st.subheader("Rental Patterns")
 
col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(8,8))
    sizes = byseason_df['Total_Costumer'].values
    labels = byseason_df['season']
    colors_season = [season_colors[label] for label in labels]

    ax.pie(sizes, labels=labels, colors=colors_season, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops={'fontsize': 14})
    centre_circle = plt.Circle((0,0),0.65,fc='white')
    fig.gca().add_artist(centre_circle)

    ax.axis('equal')
    ax.set_title("Number of Customer based on Seasons", fontsize=20, pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    plt.show()

with col2:
    fig, ax = plt.subplots(figsize=(8,8))
    sizes = byweather_df['Total_Costumer'].values
    labels = byweather_df['weathersit']
    colors_weather = [weather_colors[label] for label in labels]

    ax.pie(sizes, labels=labels, colors=colors_weather, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops={'fontsize': 14})
    centre_circle = plt.Circle((0,0),0.65,fc='white')
    fig.gca().add_artist(centre_circle)

    ax.axis('equal')
    ax.set_title("Number of Customer based on Weather", fontsize=20, pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    plt.show()

st.subheader("Customer based on Hour")

plt.figure(figsize=(10, 6))
byhour_df.plot(kind='bar', color='skyblue', legend=False, edgecolor='none', linewidth=2)
plt.title('Total Bike Rentals by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Total Rentals')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
st.pyplot(plt)

st.subheader ("Customer Clustering by Day and Hour")

plt.figure(figsize=(12, 8))
sns.heatmap(clustering, cmap="YlGnBu", annot=False, fmt=".0f")
plt.title('Bike Rentals Heatmap by Weekday and Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')

st.pyplot(plt)

st.subheader('Registered Customer and Casual Customers')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_rentals_df["dteday"],
    monthly_rentals_df["total_registered"], 
    marker='o', 
    label='Registered Rentals')
plt.plot(
    monthly_rentals_df["dteday"], 
    monthly_rentals_df["total_casual"], 
    marker='o', 
    label='Casual Rentals')

ax.set_xlabel("Month", fontsize=15)
ax.set_ylabel("Total Customers", fontsize=15)
ax.set_title("Number of Customers)", fontsize=20)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
ax.legend(fontsize=12)
ax.grid(True)

st.pyplot(fig)

total_registered = daily_rentals_df['total_registered'].sum()
total_casual = daily_rentals_df['total_casual'].sum()

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(x=["Total Registered", "Total Casual"], y=[total_registered, total_casual], palette="pastel", ax=ax)

ax.set_xlabel("Customer Type", fontsize=15)
ax.set_ylabel("Total Customers", fontsize=15)
ax.set_title("Total of Registered and Casual Customers", fontsize=20)

for i, value in enumerate([total_registered, total_casual]):
    plt.text(i, value + 1000, str(value), ha='center', va='bottom')
st.pyplot(fig)

st.caption('Copyright © anandashadrina 2024')