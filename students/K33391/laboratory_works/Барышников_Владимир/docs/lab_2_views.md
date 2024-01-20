!!! example "Задание"
    После форм необходимо прописать представления (views.py) - основную логику сайт

=== "Создание профиля"

    ``` py
    from django.shortcuts import render, redirect, get_object_or_404
    from django.contrib.auth import login, authenticate, get_user_model
    from django.utils import timezone
    
    from .forms import UserRegistrationForm, RegistrationForm, ReviewForm
    from .models import Conference, Registration, UserProfile, Review
    from django.contrib.auth.decorators import login_required
    
    
    def create_user_profile(user):
        try:
            return UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return UserProfile.objects.create(user=user)

    ```
    Описание класса -  UserProfile - это модель, которая содержит информацию о 
    пользователе, дополнительную к информации, которая уже хранится в базовой 
    модели пользователя Django (User)
    
    user - поле типа OneToOneField, тоесть каждый экзепляр будет связан с единственным User

    first_name - поле типа CharField с максимальной длиной в 30 символов

    last_name - поле типа CharField с максимальной длиной в 30 символов

    После объявления модели UserProfile, можно сохранять и извлекать данные о пользователе, такие как имя, 
    фамилию и связанного с ним пользователя, из базы данных.
    
=== "Регистрация"

    ``` py
    def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('confapp:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

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

=== "Изменение регистрации"

    ``` py
    def edit_registration(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)

    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('confapp:user_registrations')

    else:
        form = RegistrationForm(instance=registration)

    return render(request, 'edit_registration.html', {'form': form})


    @login_required
    def delete_registration(request, registration_id):
        registration = get_object_or_404(Registration, id=registration_id)

    if request.method == "POST":
        registration.delete()
        return redirect('confapp:user_registrations')

    return render(request, 'delete_registration.html', {'registration': registration})


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

=== "Написание отзыва"

    ``` py
    def write_review(request, conference_id):
    conference = Conference.objects.get(pk=conference_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.conference = conference
            review.user = request.user
            review.date = timezone.now()
            review.save()
            return redirect('confapp:home')

    else:
        form = ReviewForm()

    reviews = Review.objects.filter(conference=conference)

    return render(request, 'write_review.html', {'form': form, 'conference': conference, 'reviews': reviews})



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