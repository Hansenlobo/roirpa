import streamlit as st
from PIL import Image

st.set_page_config(page_title="Feasibility browser title")

image = Image.open('img/sunrise.png')

st.image(image, )

st.title("Feasibility Calculator")

# db

import sqlite3


con1 = sqlite3.connect('testing_11.db')
# 1-true
# 0-false

cur1 = con1.cursor()
# cur1.execute('''CREATE TABLE fesDb (access_input INTEGER, input_percentage_scanned TEXT, input_copy TEXT, input_unstructure TEXT, std_template INTEGER,input_updates TEXT,input_judmental_decision INTEGER,input_volumne_dependency TEXT,input_citrix INTEGER,input_citrix_1 INTEGER,input_citrix_2 INTEGER)''')
print("complted")


with st.expander("Process Input"):
    # intTotalProcess = st.number_input("Number of business process the RPA Bot will automate : ", min_value=0, format='%d')
    input_percentage_scanned = st.selectbox(
    'What percentage of your input is in scanned format? ',
    ('0-15%', '16-30%','31-50%','51-80%','81-100%',))


    access_input = st.selectbox(
    'Do you have access to the scanned data in electronic format? ',
    ('Yes', 'No',))
    if access_input=="Yes":
        access_input=1
    else:  
        access_input=0 


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
    if std_template=="Yes":
        std_template=1
    else:  
        std_template=0 
    
    input_updates = st.selectbox(
    'Are there frequent updates in template?',
    ('Very Rare', 'Yearly','Quarterly','Monthly','Weekly',))

with st.expander("Technical Feasibility"):
    input_citrix = st.selectbox(
    'Does Process involve working in Citirix? ',
    ('Yes', 'No',))
    if input_citrix=="Yes":
        input_citrix=1
    else:  
        input_citrix=0 
    input_citrix_1 = st.selectbox(
    'Can you do Ctrl+C  of the data field you want to read and do Ctrl+V on the application you want to move the data?',
    ('Yes', 'No',))
    if input_citrix_1=="Yes":
        input_citrix_1=1
    else:  
        input_citrix_1=0 
    input_citrix_2 = st.selectbox(
    'Can the data be extracted from any other system? ',
    ('Yes', 'No',))
    if input_citrix_2=="Yes":
        input_citrix_2=1
    else:  
        input_citrix_2=0 

    input_judmental_decision = st.selectbox(
    'Does the process include judgemental decision making, considering multiple criteria? ',
    ('Yes', 'No',))
    if input_judmental_decision=="Yes":
        input_judmental_decision=1
    else:  
        input_judmental_decision=0 

    input_volumne_dependency = st.selectbox(
    'What Percentage of Volume has dependency on clarification from customer through calls/emails? ',
    ('Select','0-15%', '16-30%','31-50%','51-80%','81-100%',))




if "%" in input_volumne_dependency:
    global total_sum
    total_sum=0
    cur1.execute("INSERT INTO fesDb VALUES (?,?,?,?,?,?,?,?,?,?,?)",(access_input,input_percentage_scanned,input_copy,input_unstructure,std_template,input_updates,input_judmental_decision,input_volumne_dependency,input_citrix,input_citrix_1,input_citrix_2))
    con1.commit()
    print("saving")

    last_row = cur1.execute('select * from fesDb').fetchall()[-1]

    print(last_row)


    if last_row[0]==1:
        access=True
    else:
        access=False
    if access:
        if last_row[1]=="0-15%":
            val_1=5
        elif last_row[1]=="16-30%":
            val_1=5
        elif last_row[1]=="31-50%":
            val_1=3
        elif last_row[1]=="51-80%":
            val_1=1
        else:
            val_1=1
    else:
        if last_row[1]=="0-15%":
            val_1=5
        elif last_row[1]=="16-30%":
            val_1=4
        elif last_row[1]=="31-50%":
            val_1=1
        elif last_row[1]=="51-80%":
            val_1=1
        else:
            val_1=1
    
    if last_row[2]=="0-15%":
        val_2=1
    elif last_row[2]=="16-30%":
        val_2=2
    elif last_row[2]=="31-50%":
        val_2=3
    elif last_row[2]=="51-80%":
        val_2=4
    else:
        val_2=5
        
    if last_row[3]=="0-15%":
        val_3=5
    elif last_row[3]=="16-30%":
        val_3=5
    elif last_row[3]=="31-50%":
        val_3=4
    elif last_row[3]=="51-80%":
        val_3=1
    else:
        val_3=1



    print(val_1)


    if last_row[4]==1:
        access=True
    else:
        access=False
    if access:
        if last_row[5]=="Very Rare":
            val_4=5
        elif last_row[5]=="Yearly":
            val_4=5
        elif last_row[5]=="Quarterly":
            val_4=3
        elif last_row[5]=="Monthly":
            val_4=1
        else:
            val_4=1
    else:
        if last_row[5]=="Very Rare":
            val_4=1
        elif last_row[5]=="Yearly":
            val_4=1
        elif last_row[5]=="Quarterly":
            val_4=1
        elif last_row[5]=="Monthly":
            val_4=1
        else:
            val_4=1


    if last_row[6]=="Yes":
        input_judmental=True
    else:
        input_judmental=False
    if input_judmental==True:
        val_6=1
    else:
        val_6=5

    if last_row[7]=="0-15%":
        val_7=5
    elif last_row[7]=="16-30%":
        val_7=4
    elif last_row[7]=="31-50%":
        val_7=3
    elif last_row[7]=="51-80%":
        val_7=2
    else:
        val_7=1
    
    if last_row[8]==1:
        input_citrix=True
    else:
        input_citrix=False

    if last_row[9]==1:
        input_citrix_1=True
    else:
        input_citrix_1=False

    if last_row[10]==1:
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
    
    total_sum=val_1+val_2+val_3+val_4+val_5+val_6+val_7
    print(total_sum)


    st.write(total_sum)
    if total_sum>29 and total_sum<35:
        st.write("Good for automation")
    elif total_sum>15 and total_sum<28:
        st.write("Automation is possible but with some challenges")
    elif total_sum>0 and total_sum<14:
        st.write("It is not a good candidate for Automation")
# def runme():
#         cur1.execute("INSERT INTO fesDb VALUES (?,?,?,?,?,?,?,?,?,?,?)",(access_input,input_percentage_scanned,input_copy,input_unstructure,std_template,input_updates,input_judmental_decision,input_volumne_dependency,input_citrix,input_citrix_1,input_citrix_2))
#         con1.commit()
#         print("saving")

# if "%" in input_volumne_dependency:
#     runme()

import webbrowser

url = 'http://192.168.0.113:8502'

if st.button('Go To roi calculator'):
    webbrowser.open_new_tab(url)