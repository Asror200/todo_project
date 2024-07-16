import service
from colorama import Fore

from utils import Response
from form import UserRegisterForm


def print_response(response: Response):
    color = Fore.GREEN if response.status_code == 200 else Fore.RED
    print(color + response.data + Fore.RESET)


def login_page() -> None:
    username: str = input('Enter your username: ')
    password: str = input('Enter your password: ')
    response: str | int = service.login(username, password)
    print_response(response)

def register_page_admin():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    form = UserRegisterForm(username, password)
    response = service.register_admin(form)
    print_response(response)

def register_page():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    form = UserRegisterForm(username, password)
    response = service.register(form)
    print_response(response)


def logout_page() -> None:
    response: str | int = service.logout()
    print_response(response)


def add_todo() -> None:
    name:str = input('Enter name: ')
    description: str = input('Enter description: ')
    response: str | int = service.todo_add(name, description)
    print_response(response)



def update_todo() -> None:
    todo_list = service.get_all_todos()
    if isinstance(todo_list,Response):# Responsdan kelgan messsageni o'tqazib yubormaslik uchun ishlatildi
        return print_response(todo_list)
    print(todo_list)
    todo_id: str = input('Enter todo id you want to update; ')
    name: str = input('Enter new title; ')
    description: str = input('Enter new description; ')
    response: str = service.todo_update(name, todo_id, description)
    print_response(response) 


def delete_todo():
    todo_list = service.get_all_todos()
    if isinstance(todo_list,Response):# Responsdan kelgan messsageni o'tqazib yubormaslik uchun ishlatildi
        return print_response(todo_list)
    print(todo_list)
    todo_id = input('Enter todo id you want to delete; ')
    response = service.todo_delete(todo_id)
    print_response(response)


def block_user():
    user_list = service.get_all_users()
    if isinstance(user_list, Response):# Responsdan kelgan messsageni o'tqazib yubormaslik uchun ishlatildi
        return print_response(user_list)
    print(user_list)
    user_id = input('Enter user id you want to block; ')
    response = service.user_block(user_id)
    print_response(response)

while True:
    user_or_todo = input(Fore.LIGHTBLUE_EX + '1 : To process user data\n2 : To process todo data\nq : Exit\nEnter your choice; ' + Fore.RESET).capitalize()
    if user_or_todo == '1':
        choice = input(Fore.LIGHTGREEN_EX+'1 : To register\n2 : To login\n3 : To block\n4 : To logout\nEnter your choise; '+Fore.RESET)    
        if choice == '1':
            choice = input('1 : As admin\n2 : As user\nEnter your choice; ')
            if choice == '1':
                register_page_admin()
            elif choice == '2':
                register_page()
        elif choice == '2':
            login_page()
        elif choice == '3':
            block_user()
        elif choice == '4':
            logout_page()
    elif user_or_todo == '2':
        choice = input(Fore.LIGHTYELLOW_EX+'1 : To add todo\n2 : To update todo\n3 : To delete todo\nEnter your choice; '+Fore.RESET)
        if choice == '1':
            add_todo()
        elif choice == '2':
            update_todo()
        elif choice == '3':
            delete_todo()
        
    elif user_or_todo == 'Q':
        break
