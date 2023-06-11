from mysql import connector
import streamlit as st


def connect_db(user,secret,host="localhost",port="8081"):
    if is_connected():
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
        st.session_state['cursor'] = cursor
        st.session_state['connection'] = connection
        st.session_state['is_connected'] = True

    except connector.Error as err:
        st.session_state['is_connected'] = False
        print(f"Error: {err}")


def disconnect():
    if is_connected():
        st.session_state['cursor'].close()
        st.session_state['connection'].close()
        st.session_state['is_connected'] = False
        st.success("Logged Out")
    else:
        st.error("Already Logged Out")
        return

def is_connected():
    if 'is_connected' in st.session_state and st.session_state['is_connected']:
        return True
    else:
        return False

