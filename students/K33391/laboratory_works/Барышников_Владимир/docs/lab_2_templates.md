!!! example "Задание"
    Реализуем шаблны html страниц нашего приложения

Django имеет встроенную систему для работы с шаблонами - Django template language (DTL). 
С помощью этой системы можно использовать в HTML файлах различные переменные и теги, например, циклы.

=== "Регистрация пользователей"

    ``` html
        <!DOCTYPE html>
    <html>
    <head>
        <title>Регистрация</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
    
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
                max-width: 400px;
                width: 100%;
            }
    
            h2 {
                text-align: center;
            }
    
            form {
                display: flex;
                flex-direction: column;
            }
    
            label {
                margin-top: 10px;
                font-weight: bold;
            }
    
            input[type="text"],
            input[type="password"] {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 3px;
                margin-top: 5px;
            }
    
            button {
                background-color: #007BFF;
                color: #fff;
                border: none;
                border-radius: 3px;
                padding: 10px;
                margin-top: 10px;
                cursor: pointer;
            }
    
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Регистрация</h2>
            <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit">Зарегистрироваться</button>
            </form>
        </div>
    </body>
    </html>

    ```
    В заголовке страницы отображается название конференции, которое передается через переменную {{ conference.name }}.

    В стилях определяется внешний вид страницы: шрифт, цвет фона, отступы и стилизация таблицы.

    В теле страницы отображаются участники конференции в виде таблицы. Используется цикл for, чтобы пройти через всех участников (переменная participants) и отобразить информацию о каждом из них в отдельной строке таблицы.

    Для каждого участника отображаются его имя, фамилия, электронная почта, тема и статус рекомендации к публикации. Информация о каждом участнике передается через соответствующие переменные, такие как {{ participant.user.first_name }} и т.д.

    Если список участников пустой, то выводится соответствующее сообщение.


        ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/register.png)  
    
=== "Просмотр_конференций"

    ``` html
        <!DOCTYPE html>
    <html>
    <head>
        <title>Главная страница</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
    
            h1 {
                background-color: #007BFF;
                color: #fff;
                padding: 20px;
                text-align: center;
            }
    
            ul {
                list-style: none;
                margin: 0;
                padding: 0;
            }
    
            li {
                background-color: #fff;
                border: 1px solid #ddd;
                margin: 10px;
                padding: 10px;
                border-radius: 5px;
            }
    
            a {
                text-decoration: none;
                color: #007BFF;
                font-weight: bold;
                margin-left: 10px;
            }
    
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Список конференций</h1>
    
        <!-- Ссылка на страницу "Мои регистрации" -->
        <a href="{% url 'confapp:user_registrations' %}">Мои регистрации</a><br>
    
        <ul>
            {% for conference in conferences %}
                <li>
                    <h2><a href="{% url 'confapp:conference_detail' conference.id %}">{{ conference.name }}</a></h2>
                    <p>Тематики: {{ conference.topics }}</p>
                    <p>Место проведения: {{ conference.location }}</p>
                    <p>Период проведения: {{ conference.start_date }} - {{ conference.end_date }}</p>
                    <p>Описание конференции: {{ conference.description }}</p>
                    <a href="{% url 'confapp:register_for_conference' conference.id %}">Регистрация для выступления</a><br>
                    <a href="{% url 'confapp:conference_participants' conference.id %}">Просмотр участников</a><br>
                    <a href="{% url 'confapp:write_review' conference.id %}">Написать отзыв</a>
                </li>
            {% endfor %}
        </ul>
    </body>
    </html>

    ```

    В заголовке страницы отображается название "Главная страница".
    
    В стилях задается внешний вид страницы: шрифт, цвет фона, отступы и стилизация элементов списка.

    В теле страницы выводится заголовок первого уровня с названием "Список конференций", а затем ссылка на страницу "Мои регистрации".

    Затем используется цикл для вывода информации о каждой конференции из списка conferences. Для каждой конференции выводится название, тематика, место проведения, период проведения, описание, а также ссылки для регистрации, просмотра участников и написания отзыва.

    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/conf_view.png)  

=== "Регистрация_авторов"

    ``` html
        <!DOCTYPE html>
    <html>
    <head>
        <title>Регистрация на конференцию</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
    
            h2 {
                background-color: #007BFF;
                color: #fff;
                padding: 20px;
                text-align: center;
            }
    
            form {
                margin: 20px;
                padding: 20px;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
    
            form button {
                background-color: #007BFF;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
    
        </style>
    </head>
    <body>
        <h2>Регистрация на конференцию "{{ conference.name }}"</h2>
        <form method="post">
            {% csrf_token %}
            <p><strong>Конференция:</strong> {{ conference.name }}</p>
            <p>Дата начала конференции: {{ conference.start_date }}</p>
            <p>Дата окончания конференции: {{ conference.end_date }}</p>
            {{ form.as_p }}
            <button type="submit">Зарегистрироваться</button>
        </form>
    </body>
    </html>

    ```

    В заголовке страницы отображается название "Регистрация на конференцию".
    
    В стилях задается внешний вид страницы: шрифт, цвет фона, отступы и стилизация формы.
    
    В теле страницы выводится заголовок второго уровня с названием конференции, на которую пользователь регистрируется.
    
    Затем отображается форма для регистрации. В форме отображается информация о конференции (название, дата начала и окончания)
    и используется CSRF-токен для защиты от подделки межсайтовых запросов. 
    Также отображаются поля формы для ввода данных и кнопка "Зарегистрироваться".
    
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/author_registration.png) 

=== "Отзывы"

    ``` html
        <!DOCTYPE html>
    <html>
    <head>
        <title>Написать отзыв</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
    
            h2 {
                background-color: #007BFF;
                color: #fff;
                padding: 20px;
                text-align: center;
            }
    
            form {
                margin: 20px;
                padding: 20px;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
    
            form button {
                background-color: #007BFF;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
    
            h2 + ul {
                margin: 20px;
                padding: 20px;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
    
            ul {
                list-style: none;
                padding: 0;
            }
    
            ul li {
                margin: 10px 0;
                padding: 0;
            }
    
            ul li:first-child {
                font-weight: bold;
            }
    
            ul li a {
                color: #007BFF;
                text-decoration: none;
            }
    
            ul li a:hover {
                text-decoration: underline;
            }
            .review {
                margin: 10px 0;
            }
    
            .review-frame {
                border: 1px solid #ddd;
                padding: 10px;
                border-radius: 5px;
            }
    
        </style>
    </head>
    <body>
        <h2>Написать отзыв о конференции "{{ conference.name }}"</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Отправить отзыв</button>
        </form>
    
        <h2>Отзывы о конференции: "{{ conference.name }}"</h2>
        <ul>
            {% for review in reviews %}
                <li class="review">
                    <div class="review-frame">
                        <strong>Комментатор:</strong> {{ review.user.username }}<br>
                        <strong>Дата конференции:</strong> {{ review.conference.start_date }} - {{ review.conference.end_date }}<br>
                        <strong>Текст комментария:</strong> {{ review.text }}<br>
                        <strong>Рейтинг:</strong> {{ review.rating }}<br>
    
                    </div>
                </li>
            {% empty %}
                <li>Пока нет отзывов</li>
            {% endfor %}
        </ul>
     </body>
    </html>

    ```
    Внутри <head> задаются стили страницы, включая шрифт, цвет фона, оформление заголовков и формы, а также стили для списка отзывов.
    
    Заголовок второго уровня (<h2>) отображает название конференции, для которой пользователь может написать отзыв.
    
    Далее следует форма (<form>) для отправки отзыва. В форме присутствует CSRF-токен для защиты от подделки запросов, 
    поле для ввода данных отзыва и кнопка "Отправить отзыв".
    
    После формы отображается заголовок второго уровня, сообщающий о наличии отзывов о конференции.
    
    Затем представлен список отзывов в виде элементов списка (<ul>), где для каждого отзыва показывается комментатор, 
    дата конференции, текст комментария и рейтинг. Если отзывов нет, выводится соответствующее сообщение.
       
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/review_add.png) 

    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/review_edit.png)  

=== "Результаты"

    ``` html
        <!DOCTYPE html>
    <html>
    <head>
        <title>Редактирование регистрации</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
    
            h2 {
                background-color: #007BFF;
                color: #fff;
                padding: 20px;
                text-align: center;
            }
    
            form {
                width: 50%;
                margin: 0 auto;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
    
            button[type="submit"] {
                background-color: #007BFF;
                color: #fff;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
                display: block;
                margin: 0 auto;
            }
    
            button[type="submit"]:hover {
                background-color: #0056b3;
            }
    
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
    
            input[type="text"], input[type="password"], select {
                width: 100%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin: 5px 0;
            }
        </style>
    </head>
    <body>
        <h2>Редактирование регистрации</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Сохранить изменения</button>
        </form>
    </body>
    </html>

    ```
    
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/recommendation_admin.png)  

=== "Участники"

    ``` html
        <!DOCTYPE html>
    <html>
    <head>
        <title>Участники конференции "{{ conference.name }}"</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
    
            h2 {
                background-color: #007BFF;
                color: #fff;
                padding: 20px;
                text-align: center;
            }
    
            table {
                border-collapse: collapse;
                width: 80%;
                margin: 20px auto;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
    
            th, td {
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }
    
            th {
                background-color: #007BFF;
                color: #fff;
            }
    
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
    
            tr:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <h2>Участники конференции "{{ conference.name }}"</h2>
        <table>
            <thead>
                <tr>
                    <th>Имя</th>
                    <th>Фамилия</th>
                    <th>Электронная почта</th>
                    <th>Тема</th>
                    <th>Рекомендован к публикации</th>
    
                </tr>
            </thead>
            <tbody>
                {% for participant in participants %}
                    <tr>
                        <td>{{ participant.user.first_name }}</td>
                        <td>{{ participant.user.last_name }}</td>
                        <td>{{ participant.user.email }}</td>
                        <td>{{ participant.topic }}</td>
                        <td>{% if participant.is_published %}Да{% else %}Нет{% endif %}</td>
    
    
                    </tr>
                {% empty %}
                    <tr>
                        <td colspan="4">Пока нет участников</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>

    ```
   
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/recommendation.png)  