!!! example "Задание"
    Для того, чтобы написать представления к нашей БД, нам нужно создать некоторые формы

Для этого создадим файл forms.py в нашем приложении.

=== "Регистрация пользователя"

    ``` py
    class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    ```
    В Django уже существует встроенная форма для регистрации новых пользователей - UserCreationForm. Но она состоит 
    только из 3 полей: никнейм, пароль и подтверждение пароля. Создадим новый класс, наследуя эту форму.
    
    Описание класса -  UserRegistrationForm наследует все функциональные возможности UserCreationForm, но также определяет 
    свой собственный набор полей для использования в процессе регистрации новых пользователей.

    
=== "Форма просмотра"

    ``` py
    class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']

    def init(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

    ```

    ModelForm - это стандартный способ создания форм на основе моделей в Django, который автоматически создает формы для моделей и их полей.

    ReviewForm - это форма, используемая для создания и обновления отзывов пользователей.

    def init(self, *args, **kwargs): - это метод-конструктор, который может быть использован для настройки формы. 
    В данном случае он вызывает конструктор родительского класса с передачей ему всех аргументов, которые могут быть переданы этому классу

=== "Форма регистрации"

    ``` py
    class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['topic']

    def init(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RegistrationForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'] = forms.ModelChoiceField(
                queryset=user,
                initial=user,
                widget=forms.HiddenInput()
            )

    ```
    ModelForm - это стандартный способ создания форм на основе моделей в Django, который автоматически создает формы для моделей и их полей.

    RegistrationForm - это форма, используемая для создания и обновления информации о регистрации на конференцию.
    
    def init(self, *args, **kwargs): - метод-конструктор, который может быть использован для настройки формы. 
    Здесь происходит дополнительная настройка формы, чтобы добавить поле пользователя.

    user = kwargs.pop('user', None) - извлекает аргумент 'user' из словаря kwargs. 
    Если пользователь не передан, по умолчанию значение будет None.
    
    super(RegistrationForm, self).__init__(*args, **kwargs) - вызывает конструктор родительского класса с передачей 
    ему всех аргументов, которые могут быть переданы этому классу.
    
    self.fields['user'] = forms.ModelChoiceField(queryset=user, initial=user, widget=forms.HiddenInput()) - 
    добавляет поле пользователя в форму с помощью виджета HiddenInput, чтобы оно не отображалось на странице, но передавалось вместе с формой.

