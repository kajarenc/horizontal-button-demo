import streamlit as st

st.radio("Label1", ["Apple", "Banana"])

st.radio("Label2", ["Female", "Male"], horizontal=True)

st.radio("Horizontal radio buttons", ["These", "radios", "are", "horizontal!"], horizontal=True)


discussion_example = {
    5: "Home",
    4: "Tutorial: Select the best option from the list of the categories given",
    3: "Tutorial: Select the worst option from the list of the categories mentioned here",
    2: "Overview",
    1: "Stratified KPIs analysis"
    }

st.radio("Label3", discussion_example.values())

st.radio("Label4", discussion_example.values(), horizontal=True)

st.sidebar.radio("Label5", ["Apple", "Banana"])

st.sidebar.radio("Label6", ["Female", "Male"], horizontal=True)



st.sidebar.radio("Label7", discussion_example.values())

st.sidebar.radio("Label8", discussion_example.values(), horizontal=True)

