import streamlit as st
import pickle
import numpy as np

# Load the trained logistic regression model
with open('emp_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="Employee Attrition Predictor", layout="wide")

# Sidebar Inputs
st.sidebar.title("🛠️ User Input Features")
age = st.sidebar.slider("Age", 18, 60, 30)
business_travel = st.sidebar.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
daily_rate = st.sidebar.number_input("Daily Rate", min_value=100, max_value=2000, value=800)
department = st.sidebar.selectbox("Department", ["Research & Development", "Human Resources", "Sales"])
distance_from_home = st.sidebar.slider("Distance From Home (in km)", 1, 30, 10)
education = st.sidebar.selectbox("Education (1=Below College, 5=Doctor)", [1, 2, 3, 4, 5])
education_field = st.sidebar.selectbox("Education Field", ["Human Resources", "Life Sciences", "Marketing", "Medical", "Other", "Technical Degree"])
environmental_satisfaction = st.sidebar.selectbox("Environmental Satisfaction (1=Low, 4=Very High)", [1, 2, 3, 4])
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
hourly_rate = st.sidebar.number_input("Hourly Rate", min_value=30, max_value=150, value=50)
job_involvement = st.sidebar.selectbox("Job Involvement (1=Low, 4=High)", [1, 2, 3, 4])
job_level = st.sidebar.selectbox("Job Level (1=Low, 5=High)", [1, 2, 3, 4, 5])
job_role = st.sidebar.selectbox("Job Role", [
    "Healthcare Representative", "Human Resources", "Laboratory Technician", "Manager",
    "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Representative"
])
job_satisfaction = st.sidebar.selectbox("Job Satisfaction (1=Low, 4=High)", [1, 2, 3, 4])
marital_status = st.sidebar.selectbox("Marital Status", ["Divorced", "Married", "Single"])
monthly_income = st.sidebar.number_input("Monthly Income", min_value=1000, max_value=7000, value=5000)
monthly_rate = st.sidebar.number_input("Monthly Rate", min_value=2000, max_value=27000, value=15000)
num_com_work = st.sidebar.selectbox("Numbers of Companies Worked (0=Low, 8=More)", list(range(10)))
overtime = st.sidebar.selectbox("OverTime", ["Yes", "No"])
percentage_salary_hike = st.sidebar.slider("Percentage Salary Hike", 11, 25, 18)
performance_rating = st.sidebar.selectbox("Performance Rating (3=Good, 4=Best)", [3, 4])
relationship_satisfaction = st.sidebar.selectbox("Relationship Satisfaction (1=Low, 4=High)", [1, 2, 3, 4])
stock_option_level = st.sidebar.selectbox("Stock Option Level (0=None, 3=High)", [0, 1, 2, 3])
total_working_years = st.sidebar.slider("Total Working Years", 0, 40, 3)
training_times_last_year = st.sidebar.selectbox("Training Times Last Year", list(range(7)))
work_life_balance = st.sidebar.selectbox("Work Life Balance (1=Low, 4=Very High)", [1, 2, 3, 4])
years_at_company = st.sidebar.slider("Years at Company", 0, 40, 5)
years_in_current_role = st.sidebar.slider("Years in Current Role", 0, 18, 2)
years_since_last_promotion = st.sidebar.slider("Years Since Last Promotion", 0, 15, 2)
years_with_current_manager = st.sidebar.slider("Years with Current Manager", 0, 17, 2)

# Encoding categorical variables
encoded = []

# Business Travel
encoded.extend([
    1 if business_travel == "Travel_Rarely" else 0,
    1 if business_travel == "Travel_Frequently" else 0
])

# Department
encoded.extend([
    1 if department == "Research & Development" else 0,
    1 if department == "Sales" else 0
])

# Education Field
encoded.extend([
    1 if education_field == "Life Sciences" else 0,
    1 if education_field == "Marketing" else 0,
    1 if education_field == "Medical" else 0,
    1 if education_field == "Other" else 0,
    1 if education_field == "Technical Degree" else 0
])

# Job Role
encoded.extend([
    1 if job_role == "Human Resources" else 0,
    1 if job_role == "Laboratory Technician" else 0,
    1 if job_role == "Manager" else 0,
    1 if job_role == "Manufacturing Director" else 0,
    1 if job_role == "Research Director" else 0,
    1 if job_role == "Research Scientist" else 0,
    1 if job_role == "Sales Executive" else 0,
    1 if job_role == "Sales Representative" else 0
])

# Marital Status
encoded.extend([
    1 if marital_status == "Married" else 0,
    1 if marital_status == "Single" else 0
])

# Gender & OverTime
encoded.append(1 if gender == "Male" else 0)
encoded.append(1 if overtime == "Yes" else 0)

# Combine all features
input_data = np.array([[
    age, daily_rate, distance_from_home, education, environmental_satisfaction,
    hourly_rate, job_involvement, job_level, job_satisfaction, monthly_income,
    monthly_rate, num_com_work, percentage_salary_hike, performance_rating,
    relationship_satisfaction, stock_option_level, total_working_years,
    training_times_last_year, work_life_balance, years_at_company,
    years_in_current_role, years_since_last_promotion, years_with_current_manager
] + encoded])

# App main content
st.markdown("<h1 style='text-align: center;'>🚨 Employee Attrition Predictor</h1>", unsafe_allow_html=True)
st.write("This model predicts whether an employee is likely to stay or leave based on the given features.")

# Predict and show result
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    

    if prediction == 1:
        st.markdown(f"<h2 style='text-align: center; color: red;'>⚠️ Employee is likely to leave.</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center; color: green;'>✅ Employee is likely to stay.</h2>", unsafe_allow_html=True)
    
    

# Input summary
st.markdown("### 🔍 Full Input Summary")
st.json({
    "Age": age,
    "Business Travel": business_travel,
    "Department": department,
    "Distance From Home": distance_from_home,
    "Education": education,
    "Education Field": education_field,
    "Environmental Satisfaction": environmental_satisfaction,
    "Gender": gender,
    "Job Involvement": job_involvement,
    "Job Level": job_level,
    "Job Role": job_role,
    "Job Satisfaction": job_satisfaction,
    "Marital Status": marital_status,
    "Monthly Income": monthly_income,
    "Number of Companies Worked": num_com_work,
    "OverTime": "Yes" if overtime == 1 else "No",
    "Percent Salary Hike": percentage_salary_hike,
    "Performance Rating": performance_rating,
    "Relationship Satisfaction": relationship_satisfaction,
    "Stock Option Level": stock_option_level,
    "Total Working Years": total_working_years,
    "Training Times Last Year": training_times_last_year,
    "Work Life Balance": work_life_balance,
    "Years at Company": years_at_company,
    "Years in Current Role": years_in_current_role,
    "Years Since Last Promotion": years_since_last_promotion,
    "Years with Current Manager": years_with_current_manager
})



