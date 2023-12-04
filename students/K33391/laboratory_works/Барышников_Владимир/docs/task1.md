!!! example "Задание"
    Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
    сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
    Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
    отобразиться у клиента.
    Обязательно использовать библиотеку socket
    Реализовать с помощью протокола UDP

=== "Сервер"

    ``` py
    import socket

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5004
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    
    while True:
        data, addr = sock.recvfrom(1024)
        print("received message:", data.decode("utf-8"))
        sock.sendto(b"Hello, client", addr)
    ```
    Описание работы -  
    1 - В серверной части мы создаем UDP сокет связываем его с указанным IP-адресом и портом  
    После чего начинаем бесконечный цикл ожидания сообщений от клиентов  
    Когда сервер получает он выводит его на экран и отправляет ответ "Hello, client" обратно на адрес клиента.  
      
    ![](http://localhost:8000/img/lab1/task1_serv.png)  
    Результат в консоли сервера


    
=== "Клиент"

    ``` py
    import socket

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5004
    MESSAGE = "Hello, server"
    print("message:", MESSAGE)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024)
    print("received message:", data.decode("utf-8"))
    ```
    Описание работы -  
    2 - Клиентская часть кода создает UDP-сокет и отправляет сообщение "Hello, server" на указанный 
    IP-адрес и порт.  
    После чего мы ждем отве от сервера и выводим полученное сообщение.

    ![](http://localhost:8000/img/lab1/task1_client.png)  
    Результат в консоли клиента

