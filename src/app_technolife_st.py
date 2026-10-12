import streamlit as st
import sqlite3

conn = sqlite3.connect("MobileProduct.db")

cursor = conn.cursor()
products = cursor.execute("Select * from MobileData").fetchall()

cols = st.columns(4)
for i in range(len(products)):
    with cols[i%4]:
        st.image(products[i][2])
        st.write(products[i][0])
        st.write(products[i][i])
        st.menu_button("View", products[i][-1])