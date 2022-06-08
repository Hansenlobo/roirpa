import streamlit as st

st.set_page_config(
    page_title="Feasibility browser title")

st.title("Feasibility Calculator")



with st.expander("Process Input"):
    # intTotalProcess = st.number_input("Number of business process the RPA Bot will automate : ", min_value=0, format='%d')



    input_percentage_scanned = st.selectbox(
    'What percentage of your input is in scanned format? ',
    ('0-15%', '16-30%','31-50%','51-80%','81-100%',))

    access_input = st.selectbox(
    'Do you have access to the scanned data in electronic format? ',
    ('Yes', 'No',))

    input_copy = st.selectbox(
    'What percentage of your input is electronic format which allows Ctrl C and Ctrl V? ',
    ('0-15%', '16-30%','31-50%','51-80%','81-100%',))

    input_unstructure = st.selectbox(
    'What percentage of your input is unstructered i.e. free flow text? ',
    ('0-15%', '16-30%','31-50%','51-80%','81-100%',))

    # st.write('You selected:', option)
    std_template = st.selectbox(
    'In case of structured data do we have standard Template/layout? ',
    ('Yes', 'No',))
    input_updates = st.selectbox(
    'Are there frequent updates in template?',
    ('Very Rare', 'Yearly','Quarterly','Monthly','Weekly',))

with st.expander("Technical Feasibility"):
    input_citrix = st.selectbox(
    'Does Process involve working in Citirix? ',
    ('Yes', 'No',))
    input_citrix_1 = st.selectbox(
    'Can you do Ctrl+C  of the data field you want to read and do Ctrl+V on the application you want to move the data?',
    ('Yes', 'No',))
    input_citrix_2 = st.selectbox(
    'Can the data be extracted from any other system? ',
    ('Yes', 'No',))

    input_judmental_decision = st.selectbox(
    'Does the process include judgemental decision making, considering multiple criteria? ',
    ('Yes', 'No',))


    input_volumne_dependency = st.selectbox(
    'What Percentage of Volume has dependency on clarification from customer through calls/emails? ',
    ('Select','0-15%', '16-30%','31-50%','51-80%','81-100%',))




    if input_volumne_dependency.find("-"):
        print("Done")
        if access_input=="Yes":
            access=True
        else:
            access=False
        if access:
            if input_percentage_scanned=="0-15%":
                val_1=5
            elif input_percentage_scanned=="16-30%":
                val_1=5
            elif input_percentage_scanned=="31-50%":
                val_1=3
            elif input_percentage_scanned=="51-80%":
                val_1=1
            else:
                val_1=1
        else:
            if input_percentage_scanned=="0-15%":
                val_1=5
            elif input_percentage_scanned=="16-30%":
                val_1=4
            elif input_percentage_scanned=="31-50%":
                val_1=1
            elif input_percentage_scanned=="51-80%":
                val_1=1
            else:
                val_1=1

        if input_copy=="0-15%":
            val_2=1
        elif input_copy=="16-30%":
            val_2=2
        elif input_copy=="31-50%":
            val_2=3
        elif input_copy=="51-80%":
            val_2=4
        else:
            val_2=5
        
        if input_unstructure=="0-15%":
            val_3=5
        elif input_unstructure=="16-30%":
            val_3=5
        elif input_unstructure=="31-50%":
            val_3=4
        elif input_unstructure=="51-80%":
            val_3=1
        else:
            val_3=1




        if std_template=="Yes":
            access=True
        else:
            access=False
        if access:
            if input_updates=="Very Rare":
                val_4=5
            elif input_updates=="Yearly":
                val_4=5
            elif input_updates=="Quarterly":
                val_4=3
            elif input_updates=="Monthly":
                val_4=1
            else:
                val_4=1
        else:
            if input_updates=="Very Rare":
                val_4=1
            elif input_updates=="Yearly":
                val_4=1
            elif input_updates=="Quarterly":
                val_4=1
            elif input_updates=="Monthly":
                val_4=1
            else:
                val_4=1


        if input_judmental_decision=="Yes":
            input_judmental=True
        else:
            input_judmental=False
        if input_judmental==True:
            val_6=1
        else:
            val_6=5


        if input_volumne_dependency=="0-15%":
            val_7=5
        elif input_volumne_dependency=="16-30%":
            val_7=4
        elif input_volumne_dependency=="31-50%":
            val_7=3
        elif input_volumne_dependency=="51-80%":
            val_7=2
        else:
            val_7=1


        if input_citrix=="Yes":
            input_citrix=True
        else:
            input_citrix=False

        if input_citrix_1=="Yes":
            input_citrix_1=True
        else:
            input_citrix_1=False

        if input_citrix_2=="Yes":
            input_citrix_2=True
        else:
            input_citrix_2=False


        if input_citrix==True and input_citrix_1==True and input_citrix_2 ==False:
            val_5=5
        elif input_citrix==True and input_citrix_1==False and input_citrix_2 ==False:
            val_5=1
        elif input_citrix==True and input_citrix_1==False and input_citrix_2 ==True:
            val_5=3
        else:
            val_5=5

                

        print(val_5)

        total_sum=val_1+val_2+val_3+val_4+val_5+val_6+val_7
        print(total_sum)
        # st.write('You selected:', total_sum)