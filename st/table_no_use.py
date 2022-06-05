import streamlit as st
import pandas as pd
li_1=[162.5, 1225.0, 1387.5, 1550.0, 1712.5]
li_2=[262.5, 2225.0, 2387.5, 2550.0, 2712.5]
li_3=[362.5, 3225.0, 3387.5, 3550.0, 7312.5]
li_4=[462.5, 4225.0, 4387.5, 4550.0, 4712.5]
li_5=[562.5, 5225.0, 5387.5, 5550.0, 5712.5]
li_6=[662.5, 6225.0, 6387.5, 6550.0, 6712.5]

df = pd.DataFrame(
    list(zip(li_1, li_2,li_3,li_4,li_5,li_6)),
    columns=('Year %d' % i for i in range(6)), index=['Current Costs for FTEs', 'Hours Per week for FTEs', 'Cost per Week for FTEs','Net ROI','Annual Accrued ROI'])




st.table(df)