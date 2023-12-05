!!! example "Задание"
    Необходимо написать простой web-сервер для обработки GET и POST http запросов 
    средствами Python и библиотеки socket. Сервер должен принимать и записывать 
    информацию о дисциплине и оценке по дисциплине. Отдавать информацию обо всех оценах по дисциплине в виде html-страницы.

=== "Сервер"

    ``` py
    import socket
    import json
    import sys
    from collections import namedtuple
    from typing import Any
    
    
    class MyHTTPServer:
        data = []
        Grade = namedtuple("Grade", ["discipline", "value"])
    
        def __init__(self, host: str, port: int):
            self.host = host
            self.port = port
    
        def serve_forever(self) -> None:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host, self.port))
                s.listen(10)
                s.settimeout(0.5)
                while True:
                    try:
                        conn, address = s.accept()
                        with conn:
                            conn.settimeout(0.5)
                            try:
                                self.serve_client(conn)
                            except socket.timeout:
                                pass
                    except socket.timeout:
                        pass
    
        def serve_client(self, conn: socket.socket) -> None:
            request = conn.recv(1024).decode()
            if request:
                method, path, version = self.parse_request(request)
                headers = self.parse_headers(request)
    
                if method == "GET":
                    self.handle_get_request(path, conn)
                elif method == "POST":
                    body = self.parse_body(request)
                    self.handle_post_request(path, body, conn)
    
        @staticmethod
        def parse_request(request: str) -> tuple[str, str, str]:
            lines = request.split("\r\n")
            method, path, version = lines[0].split(" ")
            return method, path, version
    
        @staticmethod
        def parse_headers(request: str) -> dict[str, str]:
            lines = request.split("\r\n")
            headers = {}
            for line in lines[1:]:
                if line == "":
                    break
                key, value = line.split(": ")
                headers[key] = value
            return headers
    
        @staticmethod
        def parse_body(request: str) -> dict[Any]:
            lines = request.split("\r\n")
            i = lines.index("")
            if len(lines) > i + 1:
                body = "\r\n".join(lines[i + 1 :])
                return json.loads(body)
            return {}
    
        def handle_get_request(self, path: str, conn: socket.socket) -> None:
            if path == "/":
                with open("index.html", encoding="utf-8") as f:
                    html_file = f.read()
    
                grades = "<br>".join(
                    f"{grade.discipline}: {grade.value}" for grade in self.data
                )
                html_file = html_file.replace("GRADES", grades)
                self.send_response(conn, html_file)
            else:
                with open("not_found.html", encoding="utf-8") as f:
                    html_file = f.read()
                self.send_response(conn, html_file, status_code="404 Not Found")
    
        def handle_post_request(
            self, path: str, body: dict, conn: socket.socket
        ) -> None:
            if path == "/":
                discipline = body.get("discipline", "")
                grade = body.get("grade", "")
                self.data.append(self.Grade(discipline, grade))
    
                self.send_response(conn, "")
            else:
                with open("not_found.html", encoding="utf-8") as f:
                    html_file = f.read()
                self.send_response(conn, html_file, status_code="404 Not Found")
    
        @staticmethod
        def send_response(conn, response: str, status_code: str = "200 OK") -> None:
            response_headers = {
                "Content-Type": "text/html; charset=utf-8",
                "Connection": "close",
            }
            response_headers_raw = "".join(
                f"{k}: {v}\r\n" for k, v in response_headers.items()
            )
            conn.sendall(
                (
                    f"""HTTP/1.1 {status_code}\r\n"""
                    + response_headers_raw
                    + "\r\n"
                    + response
                ).encode("utf-8")
            )
    
    
    if __name__ == "__main__":
        host = "127.0.0.1"
        port = 8080
        serv = MyHTTPServer(host, port)
        try:
            serv.serve_forever()
        except KeyboardInterrupt:
            sys.exit(1)
    ```

    1 - Сервер   
    1.1 - Мы импортирует модуль socket, который используется для создания TCP-сокета 
    и установления соединения с другими узлами в сети.  
    Также импортируются модули json и sys, а также namedtuple и Any из модуля typing. 
    
    1.2 - Класс MyHTTPServer реализует простой HTTP-сервер.  
    Он содержит методы для обработки запросов GET и POST, парсинга заголовков и тела запроса, а также отправки ответов клиенту. 
    
    1.3 - Метод serve_forever запускает сервер и ожидает соединений от клиентов.  
    При получении нового соединения вызывается метод serve_client для обработки запроса. 
    
    1.4 - Метод handle_get_request обрабатывает GET-запросы.  
    Если путь запроса равен "/", то он читает файл index.html, заменяет в нем строку "GRADES" на список оценок, полученных от клиентов, отправляет его клиенту в качестве ответа.  
    Если путь запроса неизвестен, то отправляется ответ с кодом ошибки 404 Not Found. 
    
    1.5 - Метод handle_post_request обрабатывает POST-запросы.  
    Если путь запроса равен "/", то он добавляет полученную от клиента оценку в список данных сервера и отправляет пустой ответ клиенту.  
    Если путь запроса неизвестен, то отправляется ответ с кодом ошибки 404 Not Found. 
    
    1.6 - Метод send_response отправляет ответ клиенту в формате HTTP.  


=== "HTML"

    ``` py
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Журнал оценок</title>
        <script>
            function validateGradeInput(){
                let grade = document.getElementById('grade');
                if (grade.value < 1) {
                    grade.value = 1;
                } else if (grade.value > 5) {
                    grade.value = 5;
                }
            }
    
            function sendPostRequest(event) {
                event.preventDefault();
                let discipline = document.getElementById('discipline').value;
                let grade = document.getElementById('grade').value;
    
                fetch('/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ discipline: discipline, grade: grade }),
                })
                    .then(response => response.text())
                    .then(data => {
                        console.log(data);
                        location.reload();
                    })
                    .catch((error) => console.error('Error:', error));
            }
        </script>
    </head>
    <body>
    GRADES
    <form onsubmit="sendPostRequest(event)">
        <input type="text" id="discipline" name="discipline" placeholder="Дисциплина" required>
        <input type="number" id="grade" name="grade" min="1" max="5" placeholder="Оценка" onchange="validateGradeInput()" style="width: 60px;" required>
        <button type="submit">Отправить</button>
    </form>
    </body>
    </html>
    ```

    2 - HTML  
    2.1 - Форма содержит два поля - "Дисциплина" и "Оценка", а также кнопку "Отправить".
    
    2.2 - Функция validateGradeInput() вызывается при изменении значения поля "Оценка" и проверяет, что значение находится в диапазоне от 1 до 5. Если значение меньше 1, то оно устанавливается на 1, если больше 5 - на 5.  
    
    2.3 - Функция sendPostRequest(event) вызывается при отправке формы. Она получает значения полей "Дисциплина" и "Оценка", создает POST-запрос к серверу, используя fetch API, и отправляет данные в формате JSON. После получения ответа от сервера страница перезагружается.   
    
    2.4 - Строка "GRADES" в HTML-коде будет заменена на список оценок, полученных от сервера, при обработке GET-запроса в методе handle_get_request класса MyHTTPServer.

![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab1/task5.png)  
Результат на сайте
