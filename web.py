import streamlit as st
from module import function


todos = function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase Your Productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo... ", on_change=add_todo, key='new_todo')