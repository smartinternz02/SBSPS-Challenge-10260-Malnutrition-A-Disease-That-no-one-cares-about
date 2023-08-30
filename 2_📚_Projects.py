import streamlit as st
import pandas as pd

st.title(":dna: Malnutrition")
st.subheader('A Disease That no one cares about')
st.text('You can check your personal Malnutrition Status.')
st.sidebar.title(":dna: Malnutrition")

# Extracting Data

def jls_extract_def():
    return r"C:\Users\Ravindra KVB\Desktop\vamsi\Sem-7\IBM\Malnutrition_foods-dataset.xlsx"


data = pd.read_excel(jls_extract_def())

age = st.slider('Age',min_value=0, max_value=100, value = 25)
sex = st.selectbox('Sex', options = ['Male','Female'])
country = st.multiselect(
    "Select the Country:",
    options=data["Country"].unique()
)
weight = st.slider('Weight', value = 135, min_value= 1, max_value= 140)
height = st.slider('Height', value = 160, min_value = 40, max_value = 220)


# Main Code

def calculate_bmi(weight, height):
    # Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)
    h=height/100
    bmi = int(weight / ( h** 2))
    return bmi

def calculate_z_score(value, mean, standard_deviation):
    # Calculate the z-score using the formula: (value - mean) / standard_deviation
    z_score = (value - mean) / standard_deviation
    return z_score

def classify_nutrition(bmi, age, sex):
    if age < 5:
        return 0

    if age >= 5:
        if sex == 'Male':
            # BMI classification for adults (18+ years)
            if bmi < 16:
                return -1
            elif 16 <= bmi < 25:
                return 0
            else:
                return 1
        
        elif sex == 'Female':
            # BMI classification for adults (18+ years)
            if bmi < 16:
                return -1
            elif 16 <= bmi < 24:
                return 0
            else:
                return 1
    

def classify_height_for_age_z_score(height, age, sex):
    # Example mean and standard deviation values for demonstration purposes
    # In reality, you would use actual growth chart data
    if sex == 'Male':
        mean_height = 100.0
        std_deviation_height = 10.0
    else:
        mean_height = 95.0
        std_deviation_height = 8.0
    
    # Calculate the z-score for height
    z_score = calculate_z_score(height, mean_height, std_deviation_height)
    
    if age >= 5 and z_score < -2:
        return 1
    else:
        return 0

def classify_weight_for_height_z_score(weight, height, sex):
    # Example mean and standard deviation values for demonstration purposes
    # In reality, you would use actual growth chart data
    if sex == 'Male':
        mean_weight = 45.0
        std_deviation_weight = 2.0
    else:
        mean_weight = 40.0
        std_deviation_weight = 1.5
    
    # Calculate the z-score for weight-for-height
    z_score = calculate_z_score(weight, mean_weight, std_deviation_weight)
    
    if z_score < -2:
        return 1
    else:
        return 0

l=[]
s=""

bmi = calculate_bmi(weight, height)
bmi_classification = classify_nutrition(bmi, age, sex)
height_for_age_classification = classify_height_for_age_z_score(height, age, sex)
weight_for_height_classification = classify_weight_for_height_z_score(weight, height, sex)

if(bmi_classification==-1):
    s+="UnderWeight "
    l.append("Underweight")
elif(bmi_classification==1):
    s+="OverWeight "
    l.append("Overweight")
if(height_for_age_classification==1):
    s+="Stunted "
    l.append("Stunting")
if(weight_for_height_classification==1):
    s+="Wasted "
    l.append("Wasting")
if(s==""):
    s="No Malnutrition"
st.title(f"Your Malnutrition status is : {s}")
# Conclusion
if(l==[]):
    st.text('Congratulations you are not suffering from any malnutrition')
    st.text('Try to maintain the same diet')
else:
    c_data = set()
    st.text(f'Sorry to say you are suffering from the malnutrion {s}.\n Follow the below step - ')
    for j in l:
        if (country ):
            k = data.loc[data['Country'] == country[0],j]
        else:
            k = []
        # k = data.loc[data['Country'] == country[0], j]
        for l in k:
            c_data.add(l)
    ns = set()
    for o in c_data:
        temp = o.split(", ")
        for p in temp:
            ns.add(p)
    if country :
        st.subheader(f'To overcome Malnutrition in {country[0]} you must follow the below diet plan:')
        for i in ns:
            st.text(i)
    else:
        st.text('Choose the country you belongs too...')
