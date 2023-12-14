import streamlit as st
import pandas as pd
import db


def add_title():
    st.title("Add Stock")
    if 'added_stock' not in st.session_state:
        st.session_state['added_stock'] = []

def show_items_menu():
    items = db.get_items()
    st.write("Select Item")
    item = st.selectbox("Please Select one of the following items",items)
    quantity = st.number_input("Quantity",step=1,min_value=1)
    st.session_state["new_stock"] = [item.split()[0],quantity]

def add_buttons():
    if st.button("Add Item"):
        st.session_state['added_stock'].append(st.session_state["new_stock"])
    if st.button("Remove Last Item"):
        st.session_state["added_stock"].pop()
    if st.button("Cancel adding stock"):
        st.session_state["added_stock"] = []
    if st.button("Confirm Added Stock"):
        if st.session_state["added_stock"]:
            for i in st.session_state["added_stock"]:
                db.add_items(i[0],i[1])
            st.session_state["added_stock"] = []
            st.success("Items Added to Inventory")
        else:
            st.error("No Item to add")


def show_added_stock():
    cursor=db.get_cursor()
    order = st.session_state["added_stock"]
    ord = []
    for i in order:
        cursor.execute(f"SELECT ITEM_NAME FROM ITEMS WHERE ID={i[1]}")
        q = cursor.fetchone()
        ord.append([q[0],i[1]])

    df = pd.DataFrame(ord
        ,columns=("Item Name","Quantity")
    )
    st.table(df)


add_title()
show_items_menu()
add_buttons()
show_added_stock()

