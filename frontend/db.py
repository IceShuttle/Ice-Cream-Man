from mysql import connector
import streamlit as st


def connect_db(user,passwd,host="localhost",port="8081"):
    if is_connected():
        st.error("Already Connected Please Log Out")
        return

    conn_params = {
        "user":user,
        "password":passwd,
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

def get_cursor():
    if  "cursor" in st.session_state:
        return st.session_state['cursor']

def get_connection():
    if  "connection" in st.session_state:
        return st.session_state['connection']

def add_items(id,quantity):
    cursor=get_cursor()
    cursor.execute(f"SELECT QUANTITY FROM ITEMS WHERE ID={id}")
    row = cursor.fetchone()
    final_quantity = row[0] + quantity
    cursor.execute(f"UPDATE ITEMS SET QUANTITY = {final_quantity} WHERE ID={id}")
    get_connection().commit()

def remove_items(id,quantity):
    cursor=get_cursor()
    cursor.execute(f"SELECT QUANTITY FROM ITEMS WHERE ID={id}")
    row = cursor.fetchone()
    final_quantity = row[0] - quantity
    cursor.execute(f"UPDATE ITEMS SET QUANTITY = {final_quantity} WHERE ID={id}")
    get_connection().commit()

def get_items():
    cursor=get_cursor()
    cursor.execute("SELECT ID,ITEM_NAME FROM ITEMS;")
    items = cursor.fetchall()
    for i,v in enumerate(items):
        items[i] = str(v[0])+" ) "+str(v[1])
    return items

def is_connected():
    if 'is_connected' in st.session_state:
        return st.session_state['is_connected']
    else:
        return False

def get_total_orders():
    cursor=get_cursor()
    order_no = 0
    try:
        cursor.execute("SELECT ORDER_ID FROM ORDERS ORDER BY ORDER_ID DESC LIMIT 1")
        order_no = int(cursor.fetchone()[0])
    except:
        if not cursor:
            st.error("Please Login")
    return order_no


