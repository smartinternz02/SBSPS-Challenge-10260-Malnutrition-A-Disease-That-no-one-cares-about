import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go

# Creating Home Page
st.set_page_config(
    page_title="Malnutrition",
    page_icon=":dna:"
)

st.sidebar.title(":dna: Malnutrition")
st.markdown("##")

# Extracting Data
def jls_extract_def():
    return r"C:\Users\Ravindra KVB\Desktop\vamsi\Sem-7\IBM\country-wise-average.csv"

data = pd.read_csv(jls_extract_def())



date = pd.read_excel(r"C:\Users\Ravindra KVB\Desktop\vamsi\Sem-7\IBM\Malnutrition_foods-dataset.xlsx")


df = data[['Country',"Wasting","Overweight","Stunting","Underweight"]]

# Home Page Main Design
st.title(":dna: Malnutrition\n")
st.subheader('You can select your Country and get the current Statistics of Malnutrition.')
country = st.multiselect(
    "Select the Country:",
    options=df["Country"].unique()
)
# st.dataframe(df)
df_select = df.query(
    "Country == @country"
)
df_selection = data.query(
    "Country == @country"
)
# st.dataframe(df_select)

income = round(df_selection['Income Classification'].mean(),1)
average_rating = round(df_selection["Severe Wasting"].mean(), 1)
try:
    star_rating = ":star:" * int(average_rating)
except (ValueError, TypeError):
    star_rating = 0
st.subheader("Income Classification")
st.subheader(f"{income}")

st.subheader("Average Severe Wasting:")
st.subheader(f"{average_rating} {star_rating}")

## Code to plot graph

category_names = list(df_select.columns)
if not df_select.empty:
    category_values = df_select.iloc[0].values

    fig = go.Figure(data=[go.Pie(labels=category_names, values=category_values)])

    fig.update_layout(title='Pie Chart of the Country')

    st.plotly_chart(fig)

    cap_cou = [country[0] + country[1:].lower() for country in country]
    df_selected = date.query("Country == @cap_cou[0]")
    st.text(f'The Resource avialble in {cap_cou[0]} are mentioned in the below table:')
    st.dataframe(df_selected)