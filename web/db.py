from mysql import connector
import streamlit as st


def connect_db(user,secret,host="localhost",port="8081"):
    if 'is_connected' in st.session_state and st.session_state['is_connected']:
        st.error("Already Connected Please Log Out")
        return

    conn_params = {
        "user":user,
        "password":secret,
        "host":host,
        "port":port,
        "database":"SHOP"
    }
    try: 
        connection = connector.connect(**conn_params)
        cursor = connection.cursor()
        is_connected=True
        if 'cursor' not in st.session_state:
            st.session_state['cursor'] = cursor
        if 'connection' not in st.session_state:
            st.session_state['connection'] = connection
        if 'is_connected' not in st.session_state:
            st.session_state['is_connected'] = is_connected


    except connector.Error as err:
        st.session_state['is_connected'] = False
        print(f"Error: {err}")


def disconnect():
    if 'is_connected' in st.session_state and st.session_state['is_connected']==False:
        st.error("Already Logged Out")
        return
    try:
        st.session_state['cursor'].close()
        st.session_state['connection'].close()
        st.session_state['is_connected'] = False
        st.success("Logged Out")
    except:
        st.error("Already Logged Out")
