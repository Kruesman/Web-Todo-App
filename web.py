import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = sl.session_state['new_todo']
    todos.append(todo_local + '\n')
    functions.write_todos(todos)
    sl.session_state['new_todo'] = ''


sl.title("My Todo App")
sl.subheader("This is my todo app")
sl.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

sl.text_input("", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')