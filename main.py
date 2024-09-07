import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt



# Set up the page configuration
st.set_page_config(page_title="SRPL Construction")

def load_data(db_path, table_name):
    """Load data from SQLite database table into a pandas DataFrame."""
    try:
        conn = sqlite3.connect(db_path)
        # Properly quote table name to handle special characters
        query = f'SELECT * FROM "{table_name}"'
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

def Land_detail():
     if Submit and proj =="CCCPL":
        data=pd.read_csv("CCCPL_Land.csv")  
        st.write(data) 
        #print(data.info())
        unique_values = data['Permission_details_or_Status_of_Acquistion'].unique()
        #st.write(unique_values)

        # Display the unique values in a selectbox
        selected_value = st.selectbox("Select",['Select..']+ list(unique_values))
        if selected_value != 'Select..':
            count1=data[data["Permission_details_or_Status_of_Acquistion"]==selected_value].shape[0]
            st.write("You have selected:", count1)
        
        show=st.button("Show detail")
        if show:
            st.table(data[data["Permission_details_or_Status_of_Acquistion"]==selected_value])        
     
     
     else:
        st.write()
       
          
            
# Main menu in the sidebar
with st.sidebar:
    page = option_menu(
        menu_title="SRPL Construction",  # Main menu title
        options=["Home", "Pre-Construction", "Construction", "Post-Construction"],
        icons=["house", "hammer", "tools", "folder"],  # Icons for each option
        menu_icon="cast",  # Icon for the menu
        default_index=0,   # Default selected item
        orientation="vertical"  # Menu orientation
    )

# Main content based on menu selection
if page == "Home":
    html_code = """
    <style>
        .custom-title {
            font-family: 'Arial', sans-serif;
            color: #1f77b4; /* Change this to your desired color */
            font-size: 36px; /* Adjust font size as needed */
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
    <div class="custom-title">
        Welcome to the SRPL Construction White Oil Pipeline Project (CCCPL) Home Page!<br><br>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    
    st.write("White Oil Product Pipeline Project - Common Corridor Pipeline Projects Section")

elif page == "Pre-Construction":
    # Display a submenu if "Pre-Construction" is selected
    st.title("Page is under construction")

elif page == "Construction":
    st.markdown('<h2 style="text-decoration: underline;">Common Corridor Pipeline Project</h2>', unsafe_allow_html=True)
    data1=pd.read_csv("CCCPL_WO.csv")
    selected = st.selectbox(
        "Construction details about CCCPL:",
        ['Select','Show work order details', 'Dashboard','Materials', 'MIS reports', 'Billing']
                            )
    if selected == 'Show work order details':
        st.dataframe(data1)
    
    elif selected == 'Dashboard':
        st.write("You are in Dashboard Page")
    
    elif selected == 'Materials':
        st.write("You are in Materials Page")


################# MIS reports Section ##################
    elif selected == 'MIS reports':
        st.write("You are in MIS reports Page")
        select=st.selectbox("Select Reports", ['Select','ACE','PLN'])
        if select == 'ACE':
            df=pd.read_csv('24LineA.csv')
            show_pipebook=st.checkbox("Show Pipebook")
            if show_pipebook:
                st.dataframe(df)
            select2=st.selectbox("Show the progress",['Stringing','Welding','Joint_Coating'])
            if select2=="Stringing":
                str_scope=8036
                #st.write(str_scope)
                if 'Str_Rpt' in df.columns and 'Actual_Length_m' in df.columns:
                    # Filter rows where 'Str_Rpt' has non-null values
                    filtered_df = df[df['Str_Rpt'].notna()]
                    # Calculate the sum of 'Actual_Length_m' in the filtered DataFrame
                    str_length = filtered_df['Actual_Length_m'].sum()
                    str_length=round(str_length,2)
                    st.write(f"Total Length of Stringing in m: {str_length}")
                     # Prepare data for bar chart
                    bar_data = pd.DataFrame({
                        'Category': ['Scope', 'Actual Length'],
                        'Value': [str_scope, str_length]
                    })
                    # Display the bar chart
                    #st.bar_chart(bar_data.set_index('Category'))
                    # Plot using matplotlib
                    fig, ax = plt.subplots()
                    bars=ax.bar(bar_data['Category'], bar_data['Value'], color=['blue', 'orange'])
                    for bar in bars:
                        yval = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
                    ax.set_title('Comparison of Scope and Actual Length')
                    ax.set_xlabel('Category')
                    ax.set_ylabel('Value')
                     # Adding the legend manually for clarity
                    ax.legend(['Scope', 'Actual Length'], loc='upper right')

                    # Display the plot in Streamlit
                    st.pyplot(fig)
                    
            if select2=="Welding":
                str_scope=8036
                #st.write(str_scope)
                if 'weld_Rpt' in df.columns and 'Actual_Length_m' in df.columns:
                    # Filter rows where 'Str_Rpt' has non-null values
                    filtered_df = df[df['weld_Rpt'].notna()]
                    # Calculate the sum of 'Actual_Length_m' in the filtered DataFrame
                    str_length = filtered_df['Actual_Length_m'].sum()
                    str_length=round(str_length,2)
                    st.write(f"Total Length of Welding in m: {str_length}")
                     # Prepare data for bar chart
                    bar_data = pd.DataFrame({
                        'Category': ['Scope', 'Actual Length'],
                        'Value': [str_scope, str_length],
                        
                    })
                    # Display the bar chart
                    #st.bar_chart(bar_data.set_index('Category'))  
                    
                    # Plot using matplotlib
                    fig, ax = plt.subplots()
                    bars=ax.bar(bar_data['Category'], bar_data['Value'], color=['blue', 'orange'])
                    for bar in bars:
                        yval = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
                    ax.set_title('Comparison of Scope and Actual Length')
                    ax.set_xlabel('Category')
                    ax.set_ylabel('Value')
                     # Adding the legend manually for clarity
                    ax.legend(['Scope', 'Actual Length'], loc='upper right')

                    # Display the plot in Streamlit
                    st.pyplot(fig)
                                
                     
            if select2=="Joint_Coating":
                str_scope=8036
                #st.write(str_scope)
                if 'JC_Rpt' in df.columns and 'Actual_Length_m' in df.columns:
                    # Filter rows where 'Str_Rpt' has non-null values
                    filtered_df = df[df['JC_Rpt'].notna()]
                    # Calculate the sum of 'Actual_Length_m' in the filtered DataFrame
                    str_length = filtered_df['Actual_Length_m'].sum()
                    str_length=round(str_length,2)
                    st.write(f"Total Length of Joint coating in m: {str_length}")
                     # Prepare data for bar chart
                    bar_data = pd.DataFrame({
                        'Category': ['Scope', 'Actual Length'],
                        'Value': [str_scope, str_length]
                    })
                    # Display the bar chart
                    #st.bar_chart(bar_data.set_index('Category'))      
                    # Plot using matplotlib
                    fig, ax = plt.subplots()
                    bars=ax.bar(bar_data['Category'], bar_data['Value'], color=['blue', 'orange'])
                    for bar in bars:
                        yval = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
                    ax.set_title('Comparison of Scope and Actual Length')
                    ax.set_xlabel('Category')
                    ax.set_ylabel('Value')
                     # Adding the legend manually for clarity
                    ax.legend(['Scope', 'Actual Length'], loc='upper right')

                    # Display the plot in Streamlit
                    st.pyplot(fig)                        
                
        

#############  MIS Reports Section ########################
    
    elif selected == 'Billing':
        st.write("You are in Billing Page") 
        
    else:
        st.write()
  
                                
elif page == "Post-Construction":                                
    st.title("Page is under construction")