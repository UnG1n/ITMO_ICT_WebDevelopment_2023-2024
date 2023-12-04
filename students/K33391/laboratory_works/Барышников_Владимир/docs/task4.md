!!! example "Задание"
    Реализовать двухпользовательский или многопользовательский чат. 
    Обязательно использовать библиотеку threading.

=== "Сервер"

    ``` py
    import socket
    import threading
    
    # Словарь для хранения клиентских соединений
    clients = {}
    
    def handle_client(client_socket, client_address):
        """
        Обработчик клиентского соединения.
        """
        # Получаем имя пользователя от клиента
        username = client_socket.recv(1024).decode()
    
        # Сохраняем клиентское соединение в словаре
        clients[username] = client_socket
    
        # Отправляем приветственное сообщение клиенту
        client_socket.send(f"Добро пожаловать, {username}!".encode())
    
        while True:
            # Получаем сообщение от клиента
            message = client_socket.recv(1024).decode()
    
            # Если клиент отключился, удаляем его соединение из словаря
            if not message:
                del clients[username]
                break
    
            # Отправляем сообщение всем остальным клиентам
            for name, socket in clients.items():
                if name != username:
                    socket.send(f"{username}: {message}".encode())
    
        # Закрываем клиентское соединение
        client_socket.close()
    
        def start_server():
            """
            Запуск сервера.
            """
            # Создаем TCP-сокет и связываем его с адресом 127.0.0.1:8888
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('127.0.0.1', 8888))
            server_socket.listen()
        
            while True:
                # Принимаем новое клиентское соединение
                client_socket, client_address = server_socket.accept()
        
                # Запускаем обработчик клиентского соединения в отдельном потоке
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()
        
        if __name__ == '__main__':
            start_server()

    ```
    Описание работы -  
    1 - Серверная часть  
    Функция handle_client обрабатывает клиентские соединения,  
    сохраняет их в словаре clients и отправляет сообщения между клиентами.
    Функция start_server создает TCP-сокет, связывается с указанным IP-адресом и портом  
    После чего начинает бесконечный цикл ожидания подключений от клиентов.  
    Когда клиент подключается, запускается обработчик клиентского соединения в отдельном потоке.  
    (подробнее сами действия описываются комментариями в коде)
    
=== "Клиент 1"

    ``` py
    import socket
    import threading
    
    def receive_messages(client_socket):
        """
        Функция для получения сообщений от сервера.
        """
        while True:
            message = client_socket.recv(1024).decode()
            print(message)
    
    def start_client():
        """
        Запуск клиента.
        """
        # Создаем TCP-сокет и подключаемся к серверу
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 8888))
    
        # Получаем имя пользователя от пользователя и отправляем его на сервер
        username = input("Введите ваше имя: ")
        client_socket.send(username.encode())
    
        # Запускаем поток для получения сообщений от сервера
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()
    
        while True:
            # Отправляем сообщение на сервер
            message = input()
            client_socket.send(message.encode())
    
    if __name__ == '__main__':
        start_client()

    ```
    Описание работы -  
    2 - Клиентские части между собой не отличаются  
    Используем модуль socket для создания TCP-сокета и подключения к серверу.  
    Функция receive_messages запускается в отдельном потоке и ожидает получения сообщений от сервера.  
    Функция start_client запускает клиентское приложение, запрашивает имя пользователя, подключается к серверу и запускает поток для получения сообщений от сервера.  
    Затем в бесконечном цикле ожидает ввода сообщения от пользователя и отправляет его на сервер.  
    Когда ответ приходит, клиентская часть выводит результат на экран.
    
    ![](http://localhost:8000/img/lab1/task4_client1.png)  
    Результат в консоли клиента1

=== "Клиент 2"

    ``` py
    import socket
    import threading
    
    def receive_messages(client_socket):
        """
        Функция для получения сообщений от сервера.
        """
        while True:
            message = client_socket.recv(1024).decode()
            print(message)
    
    def start_client():
        """
        Запуск клиента.
        """
        # Создаем TCP-сокет и подключаемся к серверу
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 8888))
    
        # Получаем имя пользователя от пользователя и отправляем его на сервер
        username = input("Введите ваше имя: ")
        client_socket.send(username.encode())
    
        # Запускаем поток для получения сообщений от сервера
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()
    
        while True:
            # Отправляем сообщение на сервер
            message = input()
            client_socket.send(message.encode())
    
    if __name__ == '__main__':
        start_client()

    ```

    Описание работы -  
    2 - Клиентские части между собой не отличаются  
    Используем модуль socket для создания TCP-сокета и подключения к серверу.  
    Функция receive_messages запускается в отдельном потоке и ожидает получения сообщений от сервера.  
    Функция start_client запускает клиентское приложение, запрашивает имя пользователя, подключается к серверу и запускает поток для получения сообщений от сервера.  
    Затем в бесконечном цикле ожидает ввода сообщения от пользователя и отправляет его на сервер.  
    Когда ответ приходит, клиентская часть выводит результат на экран.

    ![](http://localhost:8000/img/lab1/task4_client2.png)  
    Результат в консоли клиента2