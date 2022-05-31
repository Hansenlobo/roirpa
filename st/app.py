import streamlit as st
st.title("RPA ROI Analysis") 
st.subheader("Enter details below")

# with st.form("my_form"):
#     # Part 1
#     # Process Profile (To ensure your process assessments are clearly and consistently labelled, please complete the following details): 
#     process_title = st.text_input("Name for the process",placeholder="Process Title") 
#     opportunity_type = st.selectbox(
#      'Select the type of function the process performs?',
#      ('Analysis', 'Migration', 'Operational data processing ','System integration','Other'))
#     business_function = st.selectbox(
#      'In which part of your business is this process performed?',
#      ('Customer Care', 'Finance', 'Human Resources','IT','Operations','Shared Services', 'Supply Chain','Legal', 'Others'))
#     process_analyst = st.text_input("The person responsible for assessing this process.",placeholder="Process analyst") 
#     process_owner = st.text_input("The person currently responsible for this process, or the person who referred it as a candidate for automation.",placeholder="Process Owner") 
#     process_id = st.text_input("This ID will prefix the process title and could be useful when analysing the process discovery results.",placeholder="Process ID") 
#     process_description = st.text_input("Enter any extra information about the process that others might find useful.",placeholder="Process Description") 
#     Reason_Automation = st.text_input("To help you later when prioritizing implementation, select the main reason for automating the process.",placeholder="Primary Reason for Automation") 
#     tags = st.text_input("Adding some additional tags will help you when filtering a list of processes later.",placeholder="tags") 
    
#     # Part 2
#     # Automation Potential (To help us assess the automation potential, please answer the following questions as accurately as possible)
#     is_step_documented= st.selectbox(
#     ' Is each step of the process already well defined and fully documented? ',
#      ('Yes','No','I dont know'))
#     same_steps_repeated= st.selectbox(
#     ' How frequently are the same steps in the process repeated?',
#      ('Always','Mostly', 'Sometimes','Never','I dont know'))
#     how_many_people_perform_this = st.text_input("The number provided should include all people involved, either in the whole process or only part of it. Digital workers improve productivity, accuracy, and consistency when compared to several people working on the same process. .",placeholder="Approximately how many people regularly perform all or part of this process as part of their job role?")
#     periods_exceptionally_high_demand= st.selectbox(
#     ' Is this process likely to experience periods of exceptionally high demand?',
#      ('Always', 'Sometimes','Never','I dont know'))
#     diff_applications_used_process = st.text_input("Digital workers offer the greatest potential for processes that use multiple applications. For example, a sales enquiry process may involve using a web-based tool as well as Excel spreadsheets for pricing comparisons..",placeholder="Approximately how many different applications are used during the process?")
#     distince_app_scressn_process = st.text_input("For example, are multiple monitors used at the same time? Digital workers navigate multiple screens more efficiently than people.",placeholder="Approximately how many distinct application screens are used during the process?")
#     percesnt_process_automated = st.text_input("Most processes contain some elements that cannot be automated. For example, the beginning of a customer enquiry will always involve a customer telephone call (5% of the process), after which the resulting quotes can be automated (95% of the process).",placeholder="Approximately what percentage of the end-to-end process could be automated? This percentage value will be used to calculate the potential time and cost savings.")
#     data_used_structured_digital_format= st.selectbox(
#      'How much of the data used in the process is in a structured digital format?',
#      ('All Data is structured and digital', 'Most Data is structured and digital','Some Data is structured and digital','None Data is structured and digital','I dont know'))
#     steps_process = st.text_input("Digital workers greatly improve productivity, accuracy, and consistency when there is a high volume of steps in the process. For example, a process requires 10 steps provided all necessary information is available. Missing information might require an email enquiry which would add two further steps to the process..",placeholder="Approximately how many individual steps are included in the entire process – including all possible outcomes?")


#     # Part 3
#     # Ease of implementation(This final set of questions will help us assess how easy it will be to automate your process.)
#     percent_of_application_have_no_direct_access_user_interface=st.text_input("Approximately what percentage of the applications used during the process have no direct access to a user interface?")
#     steps_reuse=process_frequency = st.selectbox(
#      'How many steps in the process could reuse existing objects? ',
#      ('All', 'Most', 'Some','A New set of object is required','I Dont Know'))
#     applications_system_security_during_process_accessed =st.text_input("Can the applications and any system security measures used during the process be accessed by a bot?") 
#     automated_process_before= st.selectbox(
#      'Have you automated a process like this one before?',
#      ('Yes', 'No','I Dont Know'))
#     existing_performace_measurements= st.selectbox(
#      'Are there existing performance measurements in place for the manual process?',
#      ('Every Part of process', 'Large Amount of Process','Approx half of process'))
#     test_data_available= st.selectbox(
#      'Is there test data available for use in the design of this process?',
#      ('Yes', 'No','I Dont Know'))







#     # Part 4
#     #Benefit opportunity calculation(To calculate the potential cost and time saving benefits of automating this process)

#     number_of_working_days_per_year= st.text_input("The average number of working days per year for one full-time employee performing this process",placeholder="250")
#     time_taken_to_perform_task=st.text_input("The average time taken to perform the complete process once")
#     process_frequency = st.selectbox(
#      'How regularly is the process performed?',
#      ('Daily', 'Weekly', 'Fortnightly','Monthly','Anually'))
#     process_volume=st.text_input("The average number of times in total this process is completed during the period selected above")
#     number_of_working_days_per_day= st.text_input("The average number of productive working hours per day for that employee",placeholder="546")
#     average_FTE_cost=st.text_input("What currency is the employee paid in?")
#     average_total_annual_cost_employee=st.text_input("The average total annual cost of that employee (this should include salary and benefits)")


#     # part 5 Roi placeholder="546")
#     intTotalProcess=st.text_input("Number of business process the RPA Bot will automate",placeholder="")
#     intTotalEmployee=st.text_input("How many FTEs currently work on the task(s)?",placeholder="")
#     intTotalTime=st.text_input("What percentage of the FTE(s) daily time is spent on this task?",placeholder="")
#     intSalary=st.text_input("What is the average fully loaded salary of the FTE(s) performing this task?",placeholder="")
#     intCostBot=st.text_input("Est. Cost Per Bot implementation",placeholder="")
#     intMaintainanceCost=st.text_input("Estmated Maintenance",placeholder="")



#     submitted = st.form_submit_button("Submit")

#     if submitted:
#         st.write("Age", average_total_annual_cost_employee, "name", average_FTE_cost)


with st.expander("Calculate ROI"):
    with st.form("my_form"):
        intTotalProcess=st.text_input("Number of business process the RPA Bot will automate",placeholder="")
        intTotalEmployee=st.text_input("How many FTEs currently work on the task(s)?",placeholder="")
        intTotalTime=st.text_input("What percentage of the FTE(s) daily time is spent on this task?",placeholder="")
        intSalary=st.text_input("What is the average fully loaded salary of the FTE(s) performing this task?",placeholder="")
        intCostBot=st.text_input("Est. Cost Per Bot implementation",placeholder="")
        intMaintainanceCost=st.text_input("Estmated Maintenance",placeholder="")

        submitted = st.form_submit_button("Submit")

        if submitted:
            for i in range(0,3):
                st.write(int(intMaintainanceCost)*12)
    