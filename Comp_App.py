import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
import random

@st.cache_data

def main_page():
    st.markdown("# Rooster AI 🤖")
    st.sidebar.markdown("# Rooster AI Homepage")
    st.image('https://64.media.tumblr.com/595cb6e0b70c359827d754ca72474904/tumblr_mheg3ghaqx1qjqccyo1_640.gifv')

def page2():
    np.random.seed(42)
    st.markdown("# User Activity 📝")
    st.sidebar.markdown("#  User Activity")
    df = pd.DataFrame({'A':np.arange(5)})
    df['B'] = df.A.apply(lambda x: np.random.rand(25))
    df['C'] = df.A.apply(lambda x: np.random.choice([True, False]))
    
    st.data_editor(
    df,
    column_config={'A':st.column_config.NumberColumn(
            "ID", min_value=0, max_value=120, format="# %d"
        ),"B": st.column_config.BarChartColumn(
        "Activity (daily)",
        help="The user's activity in the last 25 days",
        width="medium",
        y_min=0,
        y_max=1),
        'C':st.column_config.CheckboxColumn("Is Active?", help="Is the user active?")},
    use_container_width=True,
    hide_index=True,
    num_rows="fixed",
    )
    # st.dataframe(df,column_config=
    #              {'A':st.column_config.NumberColumn(
    #         "ID", min_value=0, max_value=120, format="# %d"
    #     ),"B": st.column_config.BarChartColumn(
    #     "Activity (daily)",
    #     help="The user's activity in the last 25 days",
    #     width="medium",
    #     y_min=0,
    #     y_max=1),
    #     'C':st.column_config.CheckboxColumn("Is Active?", help="Is the user active?")})

def page3():
    st.markdown("# Sales Forecast 📈")
    st.sidebar.markdown("# Sales Forecast")
    chart_data = pd.DataFrame(np.random.randint(1000,5000,(20, 3)), columns=["Oreo", "Lotus", "H&S"])
    st.line_chart(chart_data)


def page4():
    st.markdown("# Inventory Planning 📚")
    st.sidebar.markdown("# Inventory Planning")

    # Show a spinner during a process
    with st.spinner(text='Planning Inventory...'):
       time.sleep(3)
    
    st.balloons()

    class Program:
        progress: int = 0

        def increment(self):
            self.progress += 1
            time.sleep(0.05)


    my_bar = st.progress(0, text="Planning in progress. Please wait...")

    p = Program()

    while p.progress < 100:
        p.increment()
        my_bar.progress(p.progress, text=f"Loading: {p.progress}%")
        
    st.snow()

    # Define product names
    products = ['Lotus', 'Oreo', 'H&S']

    # Generate random future purchase dates
    def generate_purchase_date():
        today = datetime.today()
        future_date = today + timedelta(days=random.randint(3, 7))
        return future_date

    # Define store IDs
    store_ids = ['Store1', 'Store2', 'Store3']

    # Define inventory management type
    inventory_management_types = ['FIFO', 'LIFO', 'FEFO']

    # Define safety stock in days
    safety_stocks = [5, 7, 3]

    # Create DataFrame
    data = {'Store_ID': [], 'Product': [], 'Date': [], 'Inventory_Management': [], 'Safety_Stock(days)': []}
    for store_id in store_ids:
        for product in products:
            purchase_date = generate_purchase_date()
            inventory_management = random.choice(inventory_management_types)
            safety_stock = random.choice(safety_stocks)
            data['Store_ID'].append(store_id)
            data['Product'].append(product)
            data['Date'].append(purchase_date)
            data['Inventory_Management'].append(inventory_management)
            data['Safety_Stock(days)'].append(safety_stock)

    df = pd.DataFrame(data)

    st.dataframe(df)

page_names_to_funcs = {
    "Rooster Homepage": main_page,
    "User Activity": page2,
    "Sales Forecast": page3,
    "Inventory Planning": page4,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()