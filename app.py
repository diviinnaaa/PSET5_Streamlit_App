import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Interactive Data Visualization",
    page_icon="📊",
    layout="centered",
)

st.title("📊 Interactive Data Visualization")
st.write(
    "Use the controls to enter values and explore how different chart types "
    "visualize the same data."
)

st.sidebar.header("Customize your chart")

chart_type = st.sidebar.selectbox(
    "Select visualization",
    ["Bar chart", "Line chart", "Pie chart"],
)

chart_title = st.sidebar.text_input(
    "Enter a chart title",
    "Monthly Study Hours",
)

st.sidebar.subheader("Enter your data")

months = ["January", "February", "March", "April", "May"]
default_values = [12, 18, 15, 22, 20]
values = []

for month, default in zip(months, default_values):
    values.append(
        st.sidebar.number_input(
            f"{month}",
            min_value=0,
            max_value=500,
            value=default,
            step=1,
        )
    )

data = pd.DataFrame({"Month": months, "Study Hours": values})

st.subheader(chart_title)
st.caption("Edit the inputs in the sidebar. The visualization updates automatically.")

if chart_type == "Bar chart":
    figure = px.bar(
        data,
        x="Month",
        y="Study Hours",
        title=chart_title,
        text="Study Hours",
    )
elif chart_type == "Line chart":
    figure = px.line(
        data,
        x="Month",
        y="Study Hours",
        title=chart_title,
        markers=True,
    )
else:
    figure = px.pie(
        data,
        names="Month",
        values="Study Hours",
        title=chart_title,
    )

st.plotly_chart(figure, width="stretch")

st.subheader("Your data")
st.dataframe(data, width="stretch", hide_index=True)

total_hours = sum(values)
average_hours = total_hours / len(values)

metric1, metric2 = st.columns(2)
metric1.metric("Total study hours", total_hours)
metric2.metric("Average per month", f"{average_hours:.1f}")

st.info(
    "This application demonstrates interactive user input through a dropdown, "
    "a text field, and numeric inputs, with a visualization that responds to "
    "the selected options and entered values."
)