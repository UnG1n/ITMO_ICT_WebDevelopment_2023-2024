!!! example "Задание"
    Сделать вывод страниц для пользователя

После написания всех компонентов для страниц приложения, необходимо выводить их пользователям и для того
чтобы код понимал в какой момент это делать воспользуемся роутером - 

=== "index.js"

    ``` js
    import { createRouter, createWebHistory } from 'vue-router';
    import LoginForm from '../components/LoginForm.vue';
    import RegisterForm from '../components/RegisterForm.vue';
    import ProfileForm from '../components/ProfileForm.vue';
    import CrewMemberForm from '../components/CrewMemberList.vue';
    import EmployeeForm from '../components/EmployeeList.vue';
    import AircraftForm from '../components/AircraftList.vue';
    import FlightForm from '../components/FlightList.vue';
    const routes = [
      { path: '/login', component: LoginForm },
      { path: '/register', component: RegisterForm },
      { path: '/auth/profile/:id', name: 'user-profile', component: ProfileForm, props: true },
      { path: '/', redirect: '/login' },
      { path: '/aircrafts', component: AircraftForm },
      { path: '/crewmembers', component: CrewMemberForm },
      { path: '/flights', component:  FlightForm },
      { path: '/employees', component: EmployeeForm },
      {
            path: '/profile',
            name: 'ProfileForm',
            component: ProfileForm,
            meta: { requiresAuth: true },
          },
        ];
    
        const router = createRouter({
          history: createWebHistory(),
          routes,
        });
    
    
        router.beforeEach((to, from, next) => {
            const isAuthenticated = !!localStorage.getItem('token');
    
    
          if (to.meta.requiresAuth && !isAuthenticated) {
    
            next('/login');
          } else {
    
            next();
          }
        });
    
    
    export default router;



    ```
    createRouter() создает новый экземпляр маршрутизатора с использованием createWebHistory(), который использует HTML5 
    History API для управления историей браузера.

    routes - это массив объектов маршрутов, где каждый объект представляет собой маршрут в приложении. Каждый маршрут 
    содержит path - путь к компоненту, который будет отображаться, и component - сам компонент.

    Некоторые маршруты также содержат name, который может использоваться для ссылок на этот маршрут в приложении, 
    и props, которые передаются в компонент через URL.

    router.beforeEach() - это функция-обработчик, которая выполняется перед каждой навигацией в приложении. 
    Она проверяет, аутентифицирован ли пользователь, и перенаправляет его на страницу входа, если он не аутентифицирован.

    Экспорт router позволяет использовать этот экземпляр маршрутизатора в других частях приложения.

