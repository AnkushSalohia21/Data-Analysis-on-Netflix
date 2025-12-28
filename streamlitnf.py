#===================================================
# Libraries
#===================================================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
#===================================================
# Options
#===================================================
st.set_page_config(layout="wide",page_title="Data Analiysis of Netflix",page_icon='🎬')
st.title("Data Analiysis of Netflix 🎬")
st.sidebar.title("OPTIONS.")
section = st.sidebar.radio("Go to", ["Introduction","Dataset Representation","2D Graphs Visualization","3D Graph Representation","Conclusion"])
#===================================================
# Introduction
#===================================================
if section == "Introduction":
    st.header("Introduction")
    st.write("Netflix is a prominent international streaming service that has an extensive collection of films and television series across various genres, languages, and geographies. " \
    "The growing trend in digital entertainment and an increasing number of streaming platforms make it essential to analyze content patterns and audience preference data for informed business strategies." \
    " This project applies data science for trend analysis and pattern recognition on the Netflix content data to derive insights on its content strategy." \
    " The data consists of information on content (whether movie or television series), year of release, length of content in minutes, ratings on a five-star scale, and countries and genres of content creation. " \
    "Data preprocessing was applied to mitigate any inconsistencies in the data and to make key factors uniform to ensure valid results. " \
    "Analysis of the data was performed through statistical analysis and data visualization to derive trends from data on content over the period, comparison between films and television series, and geographic and genre segmentation. " \
    "Analysis of various correlations associated with content release year, length in minutes, and star ratings on the impact of their presence on content creation and availability was also performed. " \
    "For convenience and to provide an intuitive experience for stakeholders to analyze and visualize data through this project, an interactive dashboard was built on the Streamlit environment to facilitate dynamic data analysis and visualization with the use of bar charts, scatter plots, and graphs for advanced data visualization in 3D. " \
    "This project is an example of data analysis and visualization being used for informed content strategy as an informed business move for streaming platforms in the growing trend of digital entertainment on the market.")
    st.image("netflix logo.png")
#===================================================
# Dataset Representation
#===================================================
elif section == "Dataset Representation":
    st.header("Firstly have a look on dataset of Netflix")
    df=pd.read_csv("Netflix.csv")
    st.dataframe(df)
    st.header("Description")
    st.write("Dataset Description This is a data set that holds Netflix subscription-related information at an individual-level customer basis. " \
    "It includes information such as User ID, category of subscription (Basic, Standard, Premium), monthly revenue per customer, and more, which would help determine pricing strategy. " \
    "It is to be noted that this data set holds critical time-related variables such as join dates, last payment dates, which can help in determining customer retention.Moreover, the demographic fields age, gender, and country can analyze the preferred actions of viewers in various regions and age groups. " \
    "Information on devices used—smartphone, tablet, laptop computer, and smart TV—also aids in the analysis of the viewing behavior of consumers. " \
    "Plan duration adds another layer of data that can also analyze the subscription trends of viewers. This data can be considered aptly suited for the exploratory analysis of viewer behavior on Netflix.")
#===================================================
# 2D Graphs Visualization
#===================================================
elif section == "2D Graphs Visualization":
    st.set_page_config(layout="wide",page_title="Multiple Graphs")
    st.header("Here we are representing some 2 dimentional graphs based on our dataset .")
    df=pd.read_csv('Netflix.csv')
        
        # 1. Bar Chart – Subscription Type Distribution
    st.subheader("1. Subscription Type Distribution")
    st.write("This bar chart shows the number of users for each subscription type. "
             "It helps in understanding which Netflix plan (Basic, Standard, or Premium) "
             "is most popular among users.")
    fig1 = px.bar(df, x="Subscription Type")
    st.plotly_chart(fig1, use_container_width=True)
    

        # 2. Pie Chart – Device Usage
    st.subheader("2. Device Usage Distribution")
    st.write("This pie chart represents the proportion of users using different devices "
             "such as smartphones, laptops, tablets, and smart TVs to access Netflix. "
             "It highlights the most preferred streaming device.")
    fig2 = px.pie(df, names="Device")
    st.plotly_chart(fig2, use_container_width=True)


        # 3. Scatter Plot – Age vs Monthly Revenue
    st.subheader("3. Age vs Monthly Revenue")
    st.write("This scatter plot shows the relationship between users' age and the monthly "
             "revenue they generate. Different colors indicate subscription types, "
             "helping to compare spending patterns across age groups.")
    fig3 = px.scatter(df,x="Age",y="Monthly Revenue",color="Subscription Type")
    st.plotly_chart(fig3, use_container_width=True)


        # 4. Line Chart – Revenue Trend Over Time
    st.subheader("4. Revenue Trend Over Time")
    st.write("This line chart displays changes in monthly revenue over time based on "
             "users' joining dates. It helps in analyzing revenue growth and identifying "
             "trends in Netflix subscriptions.")
    fig4 = px.line(df.sort_values("Join Date").tail(100),x="Join Date",y="Monthly Revenue")
    st.plotly_chart(fig4, use_container_width=True)

        # 5. Box Plot – Revenue by Subscription Type
    st.subheader("5. Revenue Distribution by Subscription Type")
    st.write("This box plot compares the distribution of monthly revenue across different "
             "subscription types. It shows revenue consistency, variation, and potential "
             "outliers for each plan.")
    fig5 = px.box(df,x="Subscription Type",y="Monthly Revenue")
    st.plotly_chart(fig5, use_container_width=True)

        #6. Bar Chart - User Destibution
    st.subheader("6. Country-wise User Distribution")
    st.write("This bar chart shows the number of Netflix users from different countries. "
             "It helps in identifying regions with higher user engagement and understanding "
             "Netflixs global reach.")
    fig6 = px.bar(df,x="Country",title="Users by Country")
    st.plotly_chart(fig6, use_container_width=True)
        
        
        #7. Pie Chart - Gender Destibution
    st.subheader("7. Gender Distribution of Users")
    st.write("This pie chart represents the distribution of Netflix users based on gender. "
             "It helps in understanding the gender-wise composition of Netflix subscribers.")
    fig7 = px.pie(df,names="Gender",title="Gender Distribution")
    st.plotly_chart(fig7, use_container_width=True)
#===================================================
# 3D Graph Representation
#===================================================
elif section == "3D Graph Representation":
    df=pd.read_csv("Netflix.csv")
    st.header("Now we are representing 3 dimentional graph based on our dataset ")
    import plotly.express as px
    import plotly.graph_objects as go
    # DATA FIX
    df["User ID"] = pd.to_numeric(df["User ID"], errors="coerce")
    df["Monthly Revenue"] = pd.to_numeric(df["Monthly Revenue"], errors="coerce")
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df = df.dropna(subset=["User ID", "Monthly Revenue", "Age"])


    # 3D SCATTER PLOT
    fig1 = px.scatter_3d(df.head(500),x="Monthly Revenue",y="Age",z="User ID",color="Subscription Type",title="1. 3D Scatter: Revenue vs Age vs User Top 500")
    st.plotly_chart(fig1, use_container_width=True)
    st.write("Description:- This 3D scatter plot visualizes the relationship between Revenue, Age, and User ID. " \
    "Data points are color-coded by subscription types—Basic, Premium, and Standard—revealing a dense, uniform distribution across the dataset.")

    # 3D LINE PLOT
    df_sorted = df.sort_values("Age")
    fig2 = px.line_3d(df_sorted.head(300),x="Age",y="Monthly Revenue",z="User ID",color="Subscription Type",title="2. 3D Line: Age → Revenue → Users Top 300")
    st.plotly_chart(fig2, use_container_width=True)
    st.write("Desription:- This 3D line graph visualizes the relationship between Age, Monthly Revenue, and User ID. " \
    "It uses colored lines (red and blue) to represent different subscription tiers, showing a highly dense and complex data distribution.")

    # 3D SURFACE PLOT
    pivot = df.pivot_table(values="Monthly Revenue",index="Age",columns="User ID",aggfunc="mean").fillna(0)
    fig3 = go.Figure(
        data=[go.Surface(z=pivot.values)])
    fig3.update_layout(title="3. 3D Surface: Revenue Density",
        scene=dict(
                    xaxis_title="User ID Index",
                    yaxis_title="Age Index",
                    zaxis_title="Monthly Revenue"))
    st.plotly_chart(fig3, use_container_width=True)
    st.write("Description:- This 3D mesh graph visualizes revenue distribution patterns. " \
            "The vertical axis represents Monthly Revenue, while the base axes track the User ID Index and a secondary metric. " \
            "The color gradient, shifting from cool blue to warm orange, highlights the density and peaks in revenue across the user base, revealing consistent trends and high-performing segments within the data.")

    # 3D MESH PLOT
    fig4 = go.Figure(
        data=[go.Mesh3d(x=df["Age"],y=df["Monthly Revenue"],z=df["User ID"],opacity=0.6)])
    fig4.update_layout(title="4. 3D Mesh: Age vs Revenue vs User")
    st.plotly_chart(fig4, use_container_width=True)
    st.write("Description:- This 3D mesh plot visualizes the relationship between age, user data, and revenue. " \
    "The blue surface highlights revenue fluctuations, identifying specific age groups and user segments that drive the highest financial impact")

    # 3D SCATTER (SIZE-BASED – Bubble Effect)
    fig5 = px.scatter_3d(df,x="Age",y="Monthly Revenue",z="User ID",size="Monthly Revenue",color="Country",title="5. 3D Bubble: Revenue Impact by Country")
    st.plotly_chart(fig5, use_container_width=True)
    st.write("Description:- This 3D bubble chart visualizes revenue impact across different countries." \
    "It plots User ID, Monthly Revenue, and Age on three axes, using colored spheres to represent data density and regional distributions.")
#===================================================
# Conclusion
#===================================================
elif section == "Conclusion":
    st.header('Conclusion')
    st.write("This Netflix data analysis project is a successful demonstration of how data science methods can be employed to unlock valuable key findings from practical, real-world data collected from a streaming service. " \
    "By appropriate cleaning, preprocessing, and exploratory data analysis, the project identifies key findings about distribution, patterns, and user preference with a regional or channel perspective. " \
    "Analysis figures out the dominance of movies over the service, concurrently focusing equally strongly on the steady growth of TV Series, thereby supporting the idea of Netflixs transition towards developing user engagement strategies through episodic series. " \
    "Insights from a country perspective or genre prospect demonstrate how Netflix is equally concentrated on supporting global markets in addition to regional markets, concurrently showing a marked preference for genres like drama, comedy, or documentaries. Analysis from a perspective involving ratings or show lengths also identifies overall target audience concentration, thereby predominantly focusing on the younger audience or adults. " \
    "Technically, the project is successful in employing Python libraries such as Pandas, Matplotlib, Seaborn, Plotly, or Streamlit in developing visual representations as well as a dashboard. " \
    "The Streamlit dashboard application also shows additional superiority in user experience, enabling interactive exploration of the entire dataset through necessary filters or charts. " \
    "This project therefore supports key appreciation for appropriate application of data analysis, visualization, or other related concepts from the entertainment industry, thereby being a successful academic project or addition to a portfolio for a data science analyst.")
    st.image("thankk.jpeg")