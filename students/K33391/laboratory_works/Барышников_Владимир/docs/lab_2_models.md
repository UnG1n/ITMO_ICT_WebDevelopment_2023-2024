!!! example "Задание"
    Нам необходимо описать БД средствами Django ORM,по журналу у меня 5ый вариант, значит
интерфейс должен представлять из себя список научных конференций

Для этого перейдём в файл models.py в нашем приложении и создадим несколько классов, наследуемых от django.db.models.Model. 

=== "Профиль пользователя"

    ``` py
    class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    ```
    Описание класса -  UserProfile - это модель, которая содержит информацию о 
    пользователе, дополнительную к информации, которая уже хранится в базовой 
    модели пользователя Django (User)
    
    user - поле типа OneToOneField, тоесть каждый экзепляр будет связан с единственным User

    first_name - поле типа CharField с максимальной длиной в 30 символов

    last_name - поле типа CharField с максимальной длиной в 30 символов

    После объявления модели UserProfile, можно сохранять и извлекать данные о пользователе, такие как имя, 
    фамилию и связанного с ним пользователя, из базы данных.
    
=== "Информация о конференции"

    ``` py
    class Conference(models.Model):
    name = models.CharField(max_length=255)
    topics = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    venue_description = models.TextField()
    participation_conditions = models.TextField()

    def __str__(self):
        return self.name

    ```
    модель Conference позволяет хранить информацию о конференциях, их датах, местах проведения, а также описании и условиях участия.
    
    name - поле типа CharField с максимальной длиной в 255 символов, предназначенное для хранения имени конференции.

    topics - поле типа TextField, предназначенное для хранения информации о темах конференции.

    location - поле типа CharField с максимальной длиной в 255 символов.

    start_date и end_date - поля типа DateField, предназначенные для хранения дат начала и окончания конференции соответственно.

    description, venue_description, participation_conditions - поля типа TextField для хранения описания конференции, 
    информации о месте проведения и условиях участия соответственно.

    def str(self): return self.name - метод, который возвращает строковое представление 
    объекта модели Conference, в данном случае это просто название конференции.

=== "Регистрация"

    ``` py
    class Registration(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255, default='', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"Registration for {self.conference.name} by {self.user.username}"

    ```

    модель Registration предназначена для хранения информации о регистрациях пользователей на конференции, включая 
    связанную конференцию, пользователя, тему регистрации и статус публикации.
    
    conference - поле типа ForeignKey, которое связывает регистрацию с конференцией.

    user - поле типа ForeignKey, которое связывает регистрацию с пользователем.

     topic - поле типа CharField с максимальной длиной в 255 символов, которое может быть пустым (параметр blank=True). 
    Это предназначено для хранения темы, связанной с регистрацией.

     is_published - поле типа BooleanField со значением по умолчанию False, которое указывает, опубликована ли регистрация.

    def str(self): return f"Registration for {self.conference.name} by {self.user.username}" - метод, который 
    возвращает строковое представление объекта модели Registration, 
    включающее название конференции и имя пользователя, для которого была создана регистрация.

=== "Просмотр"

    ``` py
    class Review(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])

    def str(self):
        return f"Review by {self.user.username} on {self.conference.name}"

    ```

    Эта модель предназначена для хранения информации о пользовательских отзывах на конференции, включая связанную 
    конференцию, пользователя, дату отзыва, текст и рейтинг.

    date - поле типа DateTimeField с параметром по умолчанию timezone.now, предназначенное для хранения даты создания отзыва.

    text - поле типа TextField для хранения текста отзыва.

    rating - поле типа PositiveIntegerField для хранения рейтинга отзыва. Устанавливаются ограничения на значение 
    рейтинга с использованием валидатора MaxValueValidator(10), который не позволяет ввести значение больше 10.

     def str(self): return f"Review by {self.user.username} on {self.conference.name}" - метод, который возвращает 
    строковое представление объекта модели Review, включающее имя пользователя и название конференции, к которой 
    относится отзыв.


После создания всех моделей нужно обязательно сделать миграции:

- python manage.py makemigrations
- python manage.py migrate

А так же создать суперпользователя:

- python manage.py createsuperuser