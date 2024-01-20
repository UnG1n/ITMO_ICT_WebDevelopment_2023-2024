!!! example "Задание"
    Реализовать админ-панель нашего приложения в папке admin.py

Далее необходимо зарегистрировать все модели. 
Чтобы дополнительно их настроить, создадим новые классы, наследуемые от admin.ModelAdmin и повесим на них декоратор @admin.register(НазваниеМодели).

=== "Регистрация_Админа"

    ``` py
    class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'conference', 'is_published')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['user', 'conference']
    ```
    Определяется пользовательский класс администратора RegistrationAdmin для модели Registration, который наследуется 
    от admin.ModelAdmin. 
    Атрибут list_display определяет, какие поля должны отображаться в списке моделей в интерфейсе
    администратора. Метод get_readonly_fields переопределяется для установки определенных полей только для чтения в зависимости от статуса вошедшего в систему пользователя. 
    Если пользователь является суперпользователем, все поля доступны для редактирования; в противном случае поля "user" и "conference" становятся только для чтения.
      
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/conf_info.png)  



    
=== "Конференция"

    ``` py
        @admin.register(Conference)
    class ConferenceAdmin(admin.ModelAdmin):
        list_display = ('name', 'start_date', 'end_date')
    
    
    def delete_selected_reviews(modeladmin, request, queryset):
        queryset.delete()
    ```
    Декоратор @admin.register(Conference) используется для регистрации модели Conference с пользовательским классом 
    ConferenceAdmin. 
    Атрибут list_display ConferenceAdmin определяет поля, которые будут отображаться в списке моделей в интерфейсе администратора.

    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab1/conf_main.png)  



=== "Удаление_обзоров"

    ``` py
            delete_selected_reviews.short_description = "Удалить выбранные отзывы"@admin.register(Review)
    class ReviewAdmin(admin.ModelAdmin):
        list_display = ('conference', 'user', 'text', 'rating')
        list_filter = ('conference', 'user')
        search_fields = ('conference__name', 'user__username', 'text')
        actions = [delete_selected_reviews]
    ```
     Функция delete_selected_reviews определяется для обработки удаления выбранных обзоров. Эта функция удаляет обзоры из queryset.
    Устанавливается атрибут short_description для функции delete_selected_reviews для предоставления понятного описания действия.
    Модель Review регистрируется с классом ReviewAdmin с помощью @admin.register(Review). 
    Класс ReviewAdmin определяет отображаемые поля, фильтры, поля для поиска и действия для модели. 
    Он использует функцию delete_selected_reviews в качестве действия для удаления выбранных обзоров.

    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/review_edit.png)

    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab2/review_main.png)
