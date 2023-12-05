!!! example "Задание"
    Реализовать с помощью протокола TCP клиентскую и серверную часть приложения. Клиент запрашивает у
    сервера выполнение Теоремы Пифагора, параметры, которые вводятся с
    клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
    клиенту. Обязательно использовать библиотеку socket

=== "Сервер"

    ``` py
    import socket
    import math
    
    TCP_IP = "127.0.0.1"
    TCP_PORT = 5005
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print("Connection address:", addr)
        data = conn.recv(1024)
        if not data:
            break
        values = data.decode("utf-8").split()[1:]
        a = int(values[0])
        b = int(values[1])
        c = math.sqrt(a**2 + b**2)
        result = "The length of the hypotenuse is: " + str(c)
        conn.sendall(bytes(result, "utf-8"))
        conn.close()
    ```

    Описание работы -  
    1 - В серверной части мы создает TCP-сокет  
    Далее связываемся с указанным IP-адресом и портом   
    После чего также как в первом задании начинаем бесконечный цикл ожидания подключений от клиентов.  
    Когда клиент подключается,  сервер получает сообщение с длинами катетов   
    вычисляет гипотенузу и отправляет результат обратно клиенту. Затем соединение закрывается.

=== "Клиент"

    ``` py
    import socket

    TCP_IP = "127.0.0.1"
    TCP_PORT = 5005
    
    a = input("Enter the length of the first cathetus: ")
    b = input("Enter the length of the second cathetus: ")
    
    MESSAGE = "PYTHAGOREAN_THEOREM " + a + " " + b

    print("message:", MESSAGE)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    sock.sendall(bytes(MESSAGE, "utf-8"))
    
    data = sock.recv(1024)
    print("received message:", data.decode("utf-8"))
    
    sock.close()
    ```
  
    Описание работы - 
    2 - Клиентская часть реализует сервер-клиентское взаимодействие по протоколу TCP.  
    Мы запрашиваем у пользователя длины двух катетов для вычисления гипотенузы по теореме Пифагора.  
    Затем создаем TCP-сокет, подключаемся к серверу с указанным IP-адресом и портом,  
    Отправляем сообщение с длинами катетов и ждем ответа от сервера.  
    Когда ответ приходит, клиентская часть выводит результат на экран.  
    
    
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab1/task2_client.png)  
    Результат в консоли клиента