!!! example "Задание"
    Создать макет нашего приложения

Для этого перейдём в файл models.py в нашем приложении и создадим несколько классов, наследуемых от django.db.models.Model. 

=== "main.js"

    ``` js
    import { createApp } from 'vue';
    import App from './App.vue';
    import router from './router';
    import { createVuetify } from 'vuetify';
    import 'vuetify/dist/vuetify.min.css';
    
    const app = createApp(App);
    
    const vuetify = createVuetify();
    
    app.use(router);
    app.use(vuetify);
    app.mount('#app');


    ```
    С помощью данного кода мы создаем настраиваем и запускаем, приложение Vue с использованием Vuetify и Router
    
    createApp(App) создает новый экземпляр приложения Vue, где App - это корневой компонент приложения.

    createVuetify() создает новый экземпляр Vuetify, который будет использоваться в приложении.

    app.use(router) устанавливает Vue Router в качестве плагина для приложения.

    app.use(vuetify) устанавливает Vuetify в качестве плагина для приложения.

    app.mount('#app') монтирует приложение в HTML-элемент с id "app". 

