!!! example "Задание"
    Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
    клиент получает http-сообщение, содержащее html-страницу, которую сервер
    подгружает из файла index.html. Обязательно использовать библиотеку socket

=== "Сервер"

    ``` py
    import socket

    HOST = 'localhost'
    PORT = 5005
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
    
        while True:
            conn, addr = s.accept()
            with conn:
                print('Подключен клиент:', addr)
                data = conn.recv(1024)
                if data:
                    response = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
                    with open('index.html', 'rb') as f:
                        response += f.read()
                    conn.sendall(response)
    ```
    Описание работы -  
    1 - В серверной части мы создает сервер на TCP-сокете  
    который будет принимать запросы и отвечать на них файлом index.html  
    Если файл index.html находится в той же директории, что и скрипт сервера, то   
    при обращении к серверу по адресу http://localhost:8000/ будет открыта эта страница.  
    Далее связываемся с указанным портом и начинаем бесконечный цикл ожидания подключений от клиентов.

    
=== "Клиент"

    ``` py
    import socket

    HOST = 'localhost'
    PORT = 5005
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
        data = s.recv(1024)
        if data:
            html = data.split(b'\r\n\r\n')[1].decode('utf-8')
            print(html)
    ```
    Описание работы - 
    2 - Клиентская часть подключается к серверу на порту 8000  
    Отправляет запрос на получение страницы index.html.
    В ответ клиент получает  
    http-сообщение, содержащее html-страницу, которую можно распарсить и использовать в дальнейшей работе.
    Когда ответ приходит, клиентская часть выводит результат на экран.
    
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab1/task3_client.png)  
    Результат в консоли клиента