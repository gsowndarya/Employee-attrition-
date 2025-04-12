import streamlit as st
import pickle
import numpy as np

# Load the models
with open('emp_model.pkl', 'rb') as file:
    attrition_model = pickle.load(file)

with open('emp_model_pr.pkl', 'rb') as file:
    performance_model = pickle.load(file)

# Page config
st.set_page_config(page_title="Employee Insights Predictor", layout="wide")
st.title("🔍 Employee Insights Predictor")
st.markdown("This app predicts **Employee Attrition** and **Performance Evaluation** based on input features.")

# Tabs for Separate Inputs
tab1, tab2 = st.tabs(["🚪 Attrition Prediction", "📊 Performance Rating Prediction"])

with tab1:
    st.subheader("🚪 Predict Employee Attrition")

    age = st.slider("Age", 18, 60, 30)
    business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
    daily_rate = st.number_input("Daily Rate", min_value=100, max_value=2000, value=800)
    department = st.selectbox("Department", ["Research & Development", "Human Resources", "Sales"])
    distance_from_home = st.slider("Distance From Home (in km)", 1, 30, 10)
    education = st.selectbox("Education (1=Below College, 5=Doctor)", [1, 2, 3, 4, 5])
    education_field = st.selectbox("Education Field", ["Human Resources", "Life Sciences", "Marketing", "Medical", "Other", "Technical Degree"])
    environmental_satisfaction = st.selectbox("Environmental Satisfaction (1=Low, 4=Very High)", [1, 2, 3, 4])
    gender = st.selectbox("Gender", ["Male", "Female"])
    hourly_rate = st.number_input("Hourly Rate", min_value=30, max_value=150, value=50)
    job_involvement = st.selectbox("Job Involvement (1=Low, 4=High)", [1, 2, 3, 4])
    job_level = st.selectbox("Job Level (1=Low, 5=High)", [1, 2, 3, 4, 5])
    job_role = st.selectbox("Job Role", [
        "Healthcare Representative", "Human Resources", "Laboratory Technician", "Manager",
        "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Representative"
    ])
    job_satisfaction = st.selectbox("Job Satisfaction (1=Low, 4=High)", [1, 2, 3, 4])
    marital_status = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])
    monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=7000, value=5000)
    monthly_rate = st.number_input("Monthly Rate", min_value=2000, max_value=27000, value=15000)
    num_com_work = st.selectbox("Number of Companies Worked", list(range(10)))
    overtime = st.selectbox("OverTime", ["Yes", "No"])
    percentage_salary_hike = st.slider("Percentage Salary Hike", 11, 25, 18)
    performance_rating = st.selectbox("Performance Rating (3=Good, 4=Best)", [3, 4])
    relationship_satisfaction = st.selectbox("Relationship Satisfaction (1=Low, 4=High)", [1, 2, 3, 4])
    stock_option_level = st.selectbox("Stock Option Level (0=None, 3=High)", [0, 1, 2, 3])
    total_working_years = st.slider("Total Working Years", 0, 40, 3)
    training_times_last_year = st.selectbox("Training Times Last Year", list(range(7)))
    work_life_balance = st.selectbox("Work Life Balance (1=Low, 4=Very High)", [1, 2, 3, 4])
    years_at_company = st.slider("Years at Company", 0, 40, 5)
    years_in_current_role = st.slider("Years in Current Role", 0, 18, 2)
    years_since_last_promotion = st.slider("Years Since Last Promotion", 0, 15, 2)
    years_with_current_manager = st.slider("Years with Current Manager", 0, 17, 2)

    # Encoding categorical variables
    encoded = [
        1 if business_travel == "Travel_Rarely" else 0,
        1 if business_travel == "Travel_Frequently" else 0,
        1 if department == "Research & Development" else 0,
        1 if department == "Sales" else 0,
        1 if education_field == "Life Sciences" else 0,
        1 if education_field == "Marketing" else 0,
        1 if education_field == "Medical" else 0,
        1 if education_field == "Other" else 0,
        1 if education_field == "Technical Degree" else 0,
        1 if job_role == "Human Resources" else 0,
        1 if job_role == "Laboratory Technician" else 0,
        1 if job_role == "Manager" else 0,
        1 if job_role == "Manufacturing Director" else 0,
        1 if job_role == "Research Director" else 0,
        1 if job_role == "Research Scientist" else 0,
        1 if job_role == "Sales Executive" else 0,
        1 if job_role == "Sales Representative" else 0,
        1 if marital_status == "Married" else 0,
        1 if marital_status == "Single" else 0,
        1 if gender == "Male" else 0,
        1 if overtime == "Yes" else 0
    ]

    attrition_features = [
        age, daily_rate, distance_from_home, education, environmental_satisfaction,
        hourly_rate, job_involvement, job_level, job_satisfaction, monthly_income,
        monthly_rate, num_com_work, percentage_salary_hike, performance_rating,
        relationship_satisfaction, stock_option_level, total_working_years,
        training_times_last_year, work_life_balance, years_at_company,
        years_in_current_role, years_since_last_promotion, years_with_current_manager
    ] + encoded

    if st.button("🔮 Predict Attrition"):
        prediction = attrition_model.predict([attrition_features])[0]
        if prediction == 1:
            st.error("⚠️ Employee is likely to leave the company.")
        else:
            st.success("✅ Employee is likely to stay in the company.")

with tab2:
    st.subheader("📊 Predict Performance Rating")

    # Inputs only for performance prediction
    job_involvement_pr = st.selectbox("Job Involvement", [1, 2, 3, 4], key="pr_involve")
    job_satisfaction_pr = st.selectbox("Job Satisfaction", [1, 2, 3, 4], key="pr_sat")
    environmental_satisfaction_pr = st.selectbox("Environmental Satisfaction", [1, 2, 3, 4], key="pr_env")
    relationship_satisfaction_pr = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4], key="pr_rel")
    job_level_pr = st.selectbox("Job Level", [1, 2, 3, 4, 5], key="pr_lvl")
    monthly_income_pr = st.number_input("Monthly Income", min_value=1000, max_value=7000, value=5000, key="pr_income")
    total_working_years_pr = st.slider("Total Working Years", 0, 40, 3, key="pr_total")
    training_times_last_year_pr = st.selectbox("Training Times Last Year", list(range(7)), key="pr_train")
    work_life_balance_pr = st.selectbox("Work Life Balance", [1, 2, 3, 4], key="pr_wlb")
    years_at_company_pr = st.slider("Years at Company", 0, 40, 5, key="pr_yac")
    years_in_current_role_pr = st.slider("Years in Current Role", 0, 18, 2, key="pr_ycr")
    years_since_last_promotion_pr = st.slider("Years Since Last Promotion", 0, 15, 2, key="pr_yslp")
    years_with_current_manager_pr = st.slider("Years with Current Manager", 0, 17, 2, key="pr_ywcm")
    overtime_pr = st.selectbox("OverTime", ["Yes", "No"], key="pr_ot")
    distance_from_home_pr = st.slider("Distance From Home", 1, 30, 10, key="pr_dist")
    percentage_salary_hike_pr = st.slider("Percentage Salary Hike", 11, 25, 18, key="pr_hike")

    performance_features = [
        job_involvement_pr, job_satisfaction_pr, environmental_satisfaction_pr, relationship_satisfaction_pr,
        job_level_pr, monthly_income_pr, total_working_years_pr, training_times_last_year_pr,
        work_life_balance_pr, years_at_company_pr, years_in_current_role_pr,
        years_since_last_promotion_pr, years_with_current_manager_pr,
        1 if overtime_pr == "Yes" else 0, distance_from_home_pr, percentage_salary_hike_pr
    ]

    if st.button("📈 Predict Performance Rating"):
        prediction = performance_model.predict([performance_features])[0]
        if prediction == 1:
            st.success("🌟 The employee is a top performer. (Rating: 4)")
        else:
            st.info("👍 The employee is a good performer. (Rating: 3)")



