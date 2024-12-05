import os
import pandas as pd
import streamlit as st
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() 

# Configuring the Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text if hasattr(response, 'text') else response[0]  

# Function to retrieve query results from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    columns = [description[0] for description in cur.description]  # Get column names from cursor description
    conn.commit()
    conn.close()
    return rows, columns

# Define your simplified prompt for Gemini AI
prompt = [
    """
    You are an expert at converting natural language questions into SQL queries. The database has these tables:

    1. USERS: user_id, name, email, phone.
    2. PRODUCTS: product_id, name, category, price, stock.
    3. ORDERS: order_id, user_id, order_date, total_amount.
    4. ORDER_ITEMS: order_item_id, order_id, product_id, quantity.

    Convert the following questions into SQL queries:

    Examples:
    - "List all users' names and emails." -> SELECT name, email FROM users;

    Return only the SQL query, no additional explanation or formatting.
    """
]

# Streamlit App UI
st.set_page_config(page_title="Text to SQL Generator App")
st.header("Text to SQL Generator App")

question = st.text_input("Input your question here:", key="input")

submit = st.button("Generate")

if submit:
    # Get response from Gemini AI based on the input question
    response = get_gemini_response(question, prompt)
    # Ensure response is in string form
    if isinstance(response, list):
        response = ''.join(response)
    
    # Display the generated SQL query
    st.subheader("Generated SQL Query:")
    st.write(response)
    
    # Execute the SQL query on the database
    result, columns = read_sql_query(response, "ecommerce.db")
    
    # Display the results
    st.subheader("Query Results:")
    if result:
        df = pd.DataFrame(result, columns=columns)  
        st.write(df)
    else:
        st.write("No results found.")
