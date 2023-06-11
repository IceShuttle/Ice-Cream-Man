import streamlit as st
import db
from datetime import datetime

st.title("Sale")

cursor = db.get_cursor()
items = []
if "order" not in st.session_state:
    st.session_state["order"] = []

cursor.execute("SELECT ORDER_ID FROM ORDERS ORDER BY ORDER_ID DESC LIMIT 1")
order_no = 0
try:
    order_no = int(cursor.fetchone()) + 1
except:
    pass

name = st.text_input("Customer's Name")
ph_no = st.text_input("Customer's Phone Number")

def get_items():
    global cursor,items
    cursor.execute("SELECT ID,ITEM_NAME FROM ITEMS;")
    items = cursor.fetchall()
    for i,v in enumerate(items):
        items[i] = str(v[0])+" ) "+str(v[1])

get_items()
st.write("Select Item")
item = st.selectbox("Please Select one of the following items",items)

quantity = st.number_input("Quantity",value=1,step=1)

if st.button("Add Item"):
    id = item.split()[0]
    st.session_state["order"].append([order_no,id,quantity])

if st.button("Get Bill"):
    st.session_state["order"].append([name,ph_no,datetime.today().strftime("%Y/%m/%d")])
    st.write(str(st.session_state["order"]))

