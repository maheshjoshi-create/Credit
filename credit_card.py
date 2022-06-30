# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:10:30 2022

@author: user
"""

import pickle
import numpy as np 
import streamlit as st
import time
import pandas as pd



loaded_model=pickle.load(open(r'trained_model.sav','rb'))

def convert_df(df):
     return df.to_csv(index = False).encode('utf-8')
 
def func(input):
    input_as_numpy_array = np.asarray(input)
    input_reshape=  input_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_reshape)
    print (prediction)
    if(prediction[0]==0):
        return'This person will not default'
    else:
        return'This person will default'
    
def main():
    
    st.sidebar.image(r"aress_logo.jpg", use_column_width=True)
    col2,col3  = st.columns(2)
    with col2:
        st.title('Credit Card Defaulter Prediction')
    with col3:
        st.image(r'credit_card_image.jpg',width=250)
    
    LIMIT_BAL = st.text_input('Limit Balance Available')
    PAY_0 = st.text_input('pay_0')
    PAY_2 = st.text_input('pay_2')
    PAY_3 = st.text_input('pay_3')
    PAY_4 = st.text_input('pay_4')
    PAY_5 = st.text_input('pay_5')
    PAY_6 = st.text_input('pay_6')
    BILL_AMT5 = st.text_input('Bill_Amount_5')
    PAY_AMT2 = st.text_input('pay_amount_2')
    
    try:
        if LIMIT_BAL and PAY_0 and PAY_2 and PAY_3 and PAY_4 and PAY_5 and PAY_6 and BILL_AMT5 and PAY_AMT2!=[]:
        
            Payment =''
            if st.button('Please click for prediction'):
                Payment = func([LIMIT_BAL,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT5,PAY_AMT2])
                with st.spinner('Wait for it...'):
                    time.sleep(5)
                    st.success(Payment)
                    if Payment=='This person will not default':
                        st.snow()
                    else:
                        st.image("better_luck.jpg")

        else:
            st.write("please enter all values")
    except:
        st.write("please enter only integer values")
        pass
    
    st.info('You can upload the file for prediction')
   
    uploaded_file = st.file_uploader("Choose a csv file for making prediction")
    if uploaded_file is not None:
     try:
        try:
            df = pd.read_csv(uploaded_file)
        except:
            df = pd.read_excel(uploaded_file)
     except:
        st.write("Please upload the CSV or Excel file only")
        
     try:
        if st.button('Please click for prediction'):
            with st.spinner('Wait for it...'):
                prediction = []
                df1 = df[['LIMIT_BAL','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','BILL_AMT5','PAY_AMT2']]
                for i in range(len(df1)):
                    Payment = func(df1.iloc[0].tolist())
                    prediction.append(Payment)
                df['Prediction']= prediction
                try:
                    df = df.drop(['default payment next month'],axis=1)
                except:
                    df = df
                csv = convert_df(df)
                st.download_button(label="Download File With the prediction as CSV",data=csv,file_name='File With the prediction.csv',mime='text/csv')  
                st.success("Prediction for the file is done")
                st.snow()             
     except:
         st.success('CSV file does not match with required columns')
         
#     try:
#         html_string = "<div class='tableauPlaceholder' id='viz1656509306208' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;PO&#47;POCTableauAnalysisupdates&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='POCTableauAnalysisupdates&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;PO&#47;POCTableauAnalysisupdates&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1656509306208');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='1727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
#         st.sidebar.write(f'''<a target="_self" href="https://public.tableau.com/app/profile/ram3105/viz/POCTableauAnalysisupdates/Dashboard1?publish=yes"><button>Dashboard 1 </button></a>''',unsafe_allow_html=True)
#         st.sidebar.write(html_string, unsafe_allow_html=True)

#     except:
#         st.write("problem with the tableau link")
    
       
if __name__== '__main__':
    main()
