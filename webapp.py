import streamlit as st
import functions

tasks = functions.get_tasks()
print(tasks)
def add_task():
    new_task = st.session_state["new_task"]+"\n"
    tasks.append(new_task)
    functions.write_tasks(tasks)


st.title("To-do app")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task,key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()

task_input = st.text_input(label="", placeholder="Enter a To-do",
                         on_change=add_task, key="new_task")

