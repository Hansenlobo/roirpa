# 1.1

# access=True
# input_format="0-15%"
access_input=input("Access Type: Yes / No")
input_percentage_scanned=input("What percentage of your input is in scanned format? ")
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




# 1.2

input_copy=input("What percentage of your input is electronic format which allows Ctrl C and Ctrl V? ")
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

# 1.3
input_unstructure=input("What percentage of your input is unstructered i.e. free flow text? ")
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


# 1.4

std_template=input("In case of structured data do we have standard Template/layout? Yes/ No")
input_updates=input("Are there frequent updates in template? ")
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






# 2.4
input_judmental_decision=input("Does the process include judgemental decision making, considering multiple criteria? ")
if input_judmental_decision=="Yes":
    input_judmental=True
else:
    input_judmental=False
if input_judmental==True:
    val_6=1
else:
    val_6=5

# 2.5
input_volumne_dependency=input("What Percentage of Volume has dependency on clarification from customer through calls/emails?")
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

input_citrix= input("Does Process involve working in Citirix? ")
input_citrix_1=input("Can you do Ctrl+C  of the data field you want to read and do Ctrl+V on the application you want to move the data?")
input_citrix_2=input("Can the data be extracted from any other system?")

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





# YES - yes - yes - 5
# YES - yes - no  - 5
# YES  no   no -  1
# NO no no=5
# NO no yes=5
# NO yes yes =5

# yes no yes =3

