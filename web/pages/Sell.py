import streamlit as st
import db
from datetime import datetime

st.title("Sale")

cursor = db.get_cursor()
items = []
if "order" not in st.session_state:
    st.session_state["order"] = []

cursor.execute("SELECT ORDER_ID FROM ORDERS ORDER BY ORDER_ID DESC LIMIT 1")
order_no = 1
try:
    order_no = int(cursor.fetchone()[0]) + 1
    print(order_no)
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

if st.button("Remove Last Item"):
    st.session_state["order"].pop()

## Bill Generation
def perform_billing():
    bill = ["The Bill"]
    order = st.session_state["order"].copy()
    details = order.pop()
    bill.append(f"Item Price Quantity Total")
    sum = 0
    for i in order:
        cursor.execute(f"SELECT ITEM_NAME,SP FROM ITEMS WHERE ID={i[1]}")
        q = cursor.fetchone()
        total = q[1]*i[2]
        sum+=total
        bill.append(f"{q[0]}'\t'{q[1]}'\t'{i[2]}'\t'{total}")
        
    bill.append("Total Payable      "+str(sum))
    bill_print = '\n'.join(bill)
    print(bill_print)
    cursor.execute(f"INSERT INTO ORDERS(CUSTOMER_NAME,CUSTOMER_NO,ORDER_DATE,AMOUNT) VALUES\
    (\"{details[0]}\",{details[1]},\"{details[2]}\",{sum})")
    conn = db.get_connection()
    conn.commit()

    for i in order:
        cursor.execute(f"INSERT INTO ORDER_ITEMS(ORDER_ID,ID,Quantity) VALUES\
        ({i[0]},{i[1]},{i[2]})")

    conn.commit()
    st.session_state["order"]=[]
 
if st.button("Confirm Order"):
    st.session_state["order"].append([name,ph_no,datetime.today().strftime("%Y-%m-%d")])
    perform_billing()

if st.button("Cancell Order"):
    st.session_state["order"]=[]

