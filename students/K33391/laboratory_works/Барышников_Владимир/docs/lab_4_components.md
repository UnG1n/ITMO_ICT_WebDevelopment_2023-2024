!!! example "Задание"
    Необходимо описать базу данных средствами Django ORM

Для этого перейдём в файл models.py в нашем приложении и создадим несколько классов, наследуемых от django.db.models.Model. 

=== "AircraftList"

    ``` vue
    <template>
      <div class="list-container ">
        <h2>Aircraft List</h2>
        <table class="aircraft-table">
          <thead>
            <tr>
              <th>Number</th>
              <th>Type</th>
              <th>Seats</th>
              <th>Speed</th>
              <th>Carrier</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="aircraft in aircrafts" :key="aircraft.id">
              <td>{{ aircraft.number }}</td>
              <td>{{ aircraft.type }}</td>
              <td>{{ aircraft.seats }}</td>
              <td>{{ aircraft.speed }}</td>
              <td>{{ aircraft.carrier }}</td>
              <button @click="deleteAircraft(aircraft.id)">Delete</button>
            </tr>
          </tbody>
        </table>
        <div claa="add-form">
            <h3>Add New Aircraft</h3>
            <form @submit.prevent="addAircraft" class="add-aircraft-form">
              <label>
                Number:
                <input v-model="newAircraft.number" type="text" required class="input-field" />
              </label>
              <label>
                Type:
                <input v-model="newAircraft.type" type="text" required class="input-field" />
              </label>
              <label>
                Seats:
                <input v-model="newAircraft.seats" type="number" required class="input-field" />
              </label>
              <label>
                Speed:
                <input v-model="newAircraft.speed" type="number" required class="input-field" />
              </label>
              <label>
                Carrier:
                <input v-model="newAircraft.carrier" type="text" required class="input-field" />
              </label>
              <button type="submit" class="add-button">Add Aircraft</button>
            </form>
            <div>
              <router-link to="/crewmembers">
                <button>Crew Members</button>
              </router-link>
              <router-link to="/flights">
                <button>Flights</button>
              </router-link>
              <router-link to="/employees">
                <button>Employees</button>
              </router-link>
              <router-link to="/profile">
                <button>Back to Profile</button>
              </router-link>
            </div>
           </div>
      </div>
    </template>
    
    <script>
    import axios from 'axios';
    export default {
      data() {
        return {
          aircrafts: [],
          newAircraft: {
            number: '',
            type: '',
            seats: 0,
            speed: 0,
            carrier: '',
          },
        };
      },
      mounted() {
        this.fetchAircrafts();
      },
      methods: {
        fetchAircrafts() {
          axios.get('http://localhost:8000/my_avia_app/api/aircrafts/')
            .then(response => {
              this.aircrafts = response.data;
            })
            .catch(error => {
              console.error(error);
            });
        },
        addAircraft() {
          axios.post('http://localhost:8000/my_avia_app/api/aircrafts/', this.newAircraft)
            .then(() => {
              this.newAircraft = {
                number: '',
                type: '',
                seats: 0,
                speed: 0,
                carrier: '',
              };
              this.fetchAircrafts();
            })
            .catch(error => {
              console.error(error);
            });
        },
         deleteAircraft(aircraftId) {
          axios.delete(`http://localhost:8000/my_avia_app/api/aircrafts/${aircraftId}/`)
            .then(() => {
              this.fetchAircrafts();
            })
            .catch(error => {
              console.error(error);
            });
        },
      },
    };
    </script>
    <style scoped>
        .list-container {
          background-color: #f0f8ff;
          display: flex;
          flex-direction: column;
          padding: 20px;
          margin: 0 auto;
        }
        h2, h3 {
          text-align: center;
          color: #4CAF50;
          margin-bottom: 20px;
          font-size: 40px;
        }
        h3 {
          margin-top: 40px;
          text-align: left;
          font-size: 30px;
        }
        .aircraft-table {
          width: 100%;
          border-collapse: collapse;
          margin-top: 20px;
          align-items: center;
        }
        .aircraft-table th,
        .aircraft-table td {
          border: 1px solid #ddd;
          padding: 8px;
          text-align: left;
        }
        .aircraft-table th {
          background-color: #4CAF50;
          color: #fff;
        }
        .add-form{
            margin-top: 40px;
            margin-left: 40px;
        }
        .add-aircraft-form {
          display: flex;
          flex-direction: column;
          align-items: flex-start;
          margin-top: 40px;
        }
        .input-field {
          width: calc(100% - 20px);
          padding: 8px;
          margin-bottom: 7px;
          border: 1px solid #4CAF50;
          border-radius: 4px;
        }
        button {
          background-color: #4CAF50;
          color: #fff;
          padding: 10px 15px;
          border: none;
          border-radius: 3px;
          cursor: pointer;
          margin-right: 10px;
          margin-top: 10px;
        }
        .button-container {
          display: flex;
          align-items: center;
          margin-top: 20px;
        }
        .add-button{
            padding-left: 70px;
            padding-right: 70px;
            }
    </style>

    ```
    
=== "CrewMembers"

    ``` vue
    <template>
      <div>
        <h2>Crew Members List</h2>
        <table class="crew-member-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Position</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="crewMember in crewMembers" :key="crewMember.id">
              <td>{{ crewMember.name }}</td>
              <td>{{ crewMember.position }}</td>
               <td>
                <button @click="deleteCrewMember(crewMember.id)">Delete</button>
              </td>
            </tr>
          </tbody>
    
        </table>
    
        <h3>Add New Crew Member</h3>
        <form @submit.prevent="addCrewMember" class="add-crew-member-form">
          <label>
            Name:
            <input v-model="newCrewMember.name" type="text" required class="input-field" />
          </label>
          <label>
            Position:
            <input v-model="newCrewMember.position" type="text" required class="input-field" />
          </label>
          <button type="submit" class="add-button">Add Crew Member</button>
        </form>
      </div>
      <div>
           <router-link to="/employees">
            <button>Employees</button>
          </router-link>
          <router-link to="/flights">
            <button>Flights</button>
          </router-link>
          <router-link to="/aircrafts">
            <button>Aircrafts</button>
          </router-link>
          <router-link to="/profile">
            <button>Back to Profile</button>
          </router-link>
        </div>
    </template>
    
    <script>
    import axios from 'axios';
    export default {
      data() {
        return {
          crewMembers: [],
          newCrewMember: {
            name: '',
            position: '',
          },
        };
      },
      mounted() {
        this.fetchCrewMembers();
      },
      methods: {
        fetchCrewMembers() {
          axios.get('http://localhost:8000/my_avia_app/api/crew-members/')
            .then(response => {
              this.crewMembers = response.data;
            })
            .catch(error => {
              console.error(error);
            });
        },
        addCrewMember() {
          axios.post('http://localhost:8000/my_avia_app/api/crew-members/', this.newCrewMember)
            .then(() => {
              this.newCrewMember = {
                name: '',
                position: '',
              };
              this.fetchCrewMembers();
            })
            .catch(error => {
              console.error(error);
            });
        },
        deleteCrewMember(crewMemberId) {
          axios.delete(`http://localhost:8000/my_avia_app/api/crew-members/${crewMemberId}/`)
            .then(() => {
              this.fetchCrewMembers();
            })
            .catch(error => {
              console.error(error);
            });
        },
      },
    };
    </script>
    <style scoped>
    .crew-member-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    .crew-member-table th,
    .crew-member-table td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    .crew-member-table th {
      background-color: #f4f4f4;
    }
    .add-crew-member-form {
      margin-top: 20px;
    }
    .input-field {
      width: 200px;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    .add-button {
      background-color: #007BFF;
      color: #fff;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .add-button:hover {
      background-color: #0056b3;
    }
    </style>

    ```
    Описание класс - Flight это класс представляющий модель полета в системе управления авиаперевозками
    
    У него есть несколько полей, таких как flight_number (номер рейса), distance (расстояние), departure_airport 
    (аэропорт отправления), destination_airport (аэропорт назначения), departure_datetime 
    (дата и время отправления), arrival_datetime (дата и время прибытия), transit_stops (транзитные остановки) и 
    sold_tickets (количество проданных билетов).

    Этот класс может быть использован для хранения информации о рейсах, а также для управления данными, связанными с 
    авиаперевозками, такими как расписание рейсов, количество проданных билетов и другие аспекты авиаперевозок.

=== "EmployeeList"

    ``` vue
    <template>
      <div>
        <h2>Employee List</h2>
        <table class="employee-table">
          <thead>
            <tr>
              <th>Username</th>
              <th>Age</th>
              <th>Education</th>
              <th>Experience</th>
              <th>Passport Data</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="employee in employees" :key="employee.id">
              <td>{{ employee.name }}</td>
              <td>{{ employee.age }}</td>
              <td>{{ employee.education }}</td>
              <td>{{ employee.experience }}</td>
              <td>{{ employee.passport_data }}</td>
              <td>
                <button @click="deleteEmployee(employee.id)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
    
        <h3>Add New Employee</h3>
        <form @submit.prevent="addEmployee" class="add-employee-form">
          <label>
            Name:
            <input v-model="newEmployee.name" type="text" required class="input-field" />
          </label>
          <label>
            Age:
            <input v-model="newEmployee.age" type="number" required class="input-field" />
          </label>
          <label>
            Education:
            <input v-model="newEmployee.education" type="text" required class="input-field" />
          </label>
          <label>
            Experience:
            <input v-model="newEmployee.experience" type="number" required class="input-field" />
          </label>
          <label>
            Passport Data:
            <input v-model="newEmployee.passport_data" type="text" required class="input-field" />
          </label>
          <button type="submit" class="add-button">Add Employee</button>
        </form>
    
        <div>
          <router-link to="/crewmembers">
            <button>Crew Members</button>
          </router-link>
          <router-link to="/flights">
            <button>Flights</button>
          </router-link>
          <router-link to="/aircrafts">
            <button>Aircrafts</button>
          </router-link>
          <router-link to="/profile">
            <button>Back to Profile</button>
          </router-link>
        </div>
      </div>
    </template>
    
    <script>
    import axios from 'axios';
    export default {
      data() {
        return {
          employees: [],
          newEmployee: {
            name: '',
            age: 0,
            education: '',
            experience: 0,
            passport_data: '',
          },
        };
      },
      mounted() {
        this.fetchEmployees();
      },
      methods: {
        fetchEmployees() {
          axios.get('http://localhost:8000/my_avia_app/api/employees/')
            .then(response => {
              this.employees = response.data;
            })
            .catch(error => {
              console.error(error);
            });
        },
        addEmployee() {
          axios.post('http://localhost:8000/my_avia_app/api/employees/', this.newEmployee)
            .then(() => {
              this.newEmployee = {
                name: '',
                age: 0,
                education: '',
                experience: 0,
                passport_data: '',
              };
              this.fetchEmployees();
            })
            .catch(error => {
              console.error(error);
            });
        },
        deleteEmployee(employeeId) {
          axios.delete(`http://localhost:8000/my_avia_app/api/employees/${employeeId}/`)
            .then(() => {
              this.fetchEmployees();
            })
            .catch(error => {
              console.error(error);
            });
        },
      },
    };
    </script>
    <style scoped>
    .employee-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    .employee-table th,
    .employee-table td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    .employee-table th {
      background-color: #f4f4f4;
    }
    .add-employee-form {
      margin-top: 20px;
    }
    .input-field {
      width: 200px;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      background-color: #007BFF;
      color: #fff;
      padding: 10px 15px;
      border: none;
      border-radius:
      }
    </style>

    ```

    Этот класс представляет модель члена экипажа в системе управления авиакомпании.
    
    У него есть несколько полей, таких как name (имя), age (возраст), education (образование), experience (опыт работы) и passport_data (паспортные данные).

=== "FlightList"

    ``` vue
    <template>
          <div class="flight-list-container">
            <h2>Flight List</h2>
            <table class="flight-table">
              <thead>
                <tr>
                  <th>Flight Number</th>
                  <th>Distance</th>
                  <th>Departure Point</th>
                  <th>Destination Point</th>
                  <th>Departure Datetime</th>
                  <th>Arrival Datetime</th>
                  <th>Sold Tickets</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="flight in flights" :key="flight.id">
                  <td>{{ flight.flight_number }}</td>
                  <td>{{ flight.distance }}</td>
                  <td>{{ flight.departure_point }}</td>
                  <td>{{ flight.destination_point }}</td>
                  <td>{{ flight.departure_datetime }}</td>
                  <td>{{ flight.arrival_datetime }}</td>
                  <td>{{ flight.sold_tickets }}</td>
                  <td>
                    <button @click="deleteFlight(flight.id)" class="delete-button">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
            <div class="add-form">
                <h3>Add New Flight</h3>
                <form @submit.prevent="addFlight" class="add-flight-form">
                  <label>
                    Flight Number:
                    <input v-model="newFlight.flight_number" type="text" required class="input-field" />
                  </label>
                  <br />
                  <label>
                    Distance:
                    <input v-model="newFlight.distance" type="number" required class="input-field" />
                  </label>
                  <br />
                  <label>
                    Departure Point:
                    <input v-model="newFlight.departure_point" type="text" required class="input-field" />
                  </label>
                  <br />
                  <label>
                    Destination Point:
                    <input v-model="newFlight.destination_point" type="text" required class="input-field" />
                  </label>
                  <br />
                  <label>
                    Departure Datetime:
                    <input v-model="newFlight.departure_datetime" type="datetime-local" required class="input-field" />
                  </label>
                  <br />
                  <label>
                    Arrival Datetime:
                    <input v-model="newFlight.arrival_datetime" type="datetime-local" required class="input-field" />
                  </label>
        
                  <br />
                  <label>
                    Sold Tickets:
                    <input v-model="newFlight.sold_tickets" type="number" required class="input-field" />
                  </label>
                  <br />
                  <button type="submit" class="add-button">Add Flight</button>
                </form>
        
                <div class = "button-container">
                  <router-link to="/crewmembers">
                    <button>Crew Members</button>
                  </router-link>
                  <router-link to="/aircrafts">
                    <button>Aircrafts</button>
                  </router-link>
                  <router-link to="/employees">
                    <button>Employees</button>
                  </router-link>
                  <router-link to="/profile">
                    <button>Back to Profile</button>
                  </router-link>
                </div>
            </div>
          </div>
        </template>
        
        <script>
        import axios from 'axios';
        export default {
          data() {
            return {
              flights: [],
              newFlight: {
                flight_number: '',
                distance: 0,
                departure_point: '',
                destination_point: '',
                departure_datetime: '',
                arrival_datetime: '',
                sold_tickets: 0,
              },
            };
          },
          mounted() {
            this.fetchFlights();
          },
          methods: {
            fetchFlights() {
              axios.get('http://localhost:8000/my_avia_app/api/flights/')
                .then(response => {
                  this.flights = response.data;
                })
                .catch(error => {
                  console.error(error);
                });
            },
            addFlight() {
              axios.post('http://localhost:8000/my_avia_app/api/flights/', this.newFlight)
                .then(() => {
                  this.newFlight = {
                    flight_number: '',
                    distance: 0,
                    departure_point: '',
                    destination_point: '',
                    departure_datetime: '',
                    arrival_datetime: '',
                    sold_tickets: 0,
                  };
                  this.fetchFlights();
                })
                .catch(error => {
                  console.error(error);
                });
            },
            deleteFlight(flightId) {
              axios.delete(`http://localhost:8000/my_avia_app/api/flights/${flightId}/`)
                .then(() => {
                  this.fetchFlights();
                })
                .catch(error => {
                  console.error(error);
                });
            },
          },
        };
        </script>
        <style scoped>
            .flight-list-container {
              background-color: #f0f8ff;
              display: flex;
              flex-direction: column;
              padding: 20px;
              margin: 0 auto;
            }
            h2, h3 {
              text-align: center;
              color: #4CAF50;
              margin-bottom: 20px;
              font-size: 40px;
            }
            h3 {
              text-align: left;
              font-size: 30px;
            }
            .flight-table {
              width: 100%;
              border-collapse: collapse;
              margin-top: 20px;
            }
            .flight-table th,
            .flight-table td {
              border: 1px solid #ddd;
              padding: 8px;
              text-align: left;
            }
            .flight-table th {
              background-color: #4CAF50;
              color: #fff;
            }
            .add-form{
                margin-top: 40px;
                margin-left: 40px;
            }
            .add-flight-form {
              display: flex;
              flex-direction: column;
              align-items: flex-start;
              margin-top: 40px;
            }
            .input-field {
              width: calc(100% - 20px);
              padding: 8px;
              margin-bottom: 7px;
              border: 1px solid #4CAF50;
              border-radius: 4px;
            }
            button {
              background-color: #4CAF50;
              color: #fff;
              padding: 10px 15px;
              border: none;
              border-radius: 3px;
              cursor: pointer;
              margin-right: 10px;
              margin-top: 10px;
            }
            .button-container {
              display: flex;
              align-items: center;
              margin-top: 20px;
            }
            .add-button{
                padding-left: 70px;
                padding-right: 70px;
                }
        </style>
    
        ```
    
        Этот класс представляет модель транзитной остановки в системе управления авиаперевозками. У него есть два поля: 
        airport (аэропорт) и datetime (дата и время).
    
        Может использоваться для отслеживания информации о транзитных остановках в рамках конкретного рейса или на пути между аэропортами. 
    
    === "HelloWorld"
    
        ``` vue
        <template>
      <div class="hello">
        <h1>{{ msg }}</h1>
        <p>
          For a guide and recipes on how to configure / customize this project,<br>
          check out the
          <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
        </p>
        <h3>Installed CLI Plugins</h3>
        <ul>
          <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
          <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
        </ul>
        <h3>Essential Links</h3>
        <ul>
          <li><a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a></li>
          <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a></li>
          <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a></li>
          <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a></li>
          <li><a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a></li>
        </ul>
        <h3>Ecosystem</h3>
        <ul>
          <li><a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a></li>
          <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a></li>
          <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a></li>
          <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a></li>
          <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a></li>
        </ul>
      </div>
    </template>
    
    <script>
    export default {
      name: 'HelloWorld',
      props: {
        msg: String
      }
    }
    </script>
    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
    <style scoped>
    h3 {
      margin: 40px 0 0;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      display: inline-block;
      margin: 0 10px;
    }
    a {
      color: #42b983;
    }
    </style>

    ```
    
    Этот класс представляет модель сотрудника в системе управления персоналом, который может быть использован, например, в 
    авиаперевозочной компании. У этого класса есть несколько полей:  name (имя), age (возраст), education (образование),
    experience (опыт работы),  passport_data (паспортные данные),  is_airport_employee (является ли сотрудник аэропортовским сотрудником),
    
    Может использоваться для хранения информации о сотрудниках, их биографических данных, образовании и опыте работы. 
    Поле is_airport_employee позволяет различать между сотрудниками аэропорта и другими работниками, что может быть полезно для управления персоналом в авиационной компании.

=== "LoginForm"

    ``` vue
    <template>
        <div class="background-container">
            <img src="@/assets/plane.jpg" alt="Sky" class="background-image">
          <div class="login-container">
            <form @submit.prevent="login" class="login-form">
              <h2>Login</h2>
              <div class="form-group">
                <label for="loginUsername">Username:</label>
                <input v-model="username" type="text" id="loginUsername" required />
              </div>
              <div class="form-group">
                <label for="loginPassword">Password:</label>
                <input v-model="password" type="password" id="loginPassword" required />
              </div>
              <button type="submit">Login</button>
              <p class="register-link">No account? <router-link to="/register">Register</router-link></p>
            </form>
          </div>
        </div>
    </template>
    
    <script>
    import axios from 'axios';
    export default {
      data() {
        return {
          username: '',
          password: '',
        };
      },
      methods: {
        login() {
          axios.post('http://localhost:8000/my_avia_app/auth/login/', {
            username: this.username,
            password: this.password,
          })
          .then(response => {
            console.log('Server Response:', response.data);
            localStorage.setItem('token', response.data.token);
              const userId = response.data.id;
            console.log('User ID:', userId);
            console.log(response.data);
            this.$router.push({ path: '/auth/profile/:id' });
          })
          .catch(error => {
            console.error(error);
          });
        }
      }
    };
    </script>
    <style scoped>
    .background-container {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }
    .background-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
    }
    .login-container {
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #fff; /* Белый фон */
    }
    .login-form {
      max-width: 300px;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h2 {
      text-align: center;
      color: #4CAF50; /* Светло-зеленый цвет */
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 3px;
    }
    button {
      background-color: #4CAF50; /* Светло-зеленый цвет */
      color: #fff;
      padding: 10px 15px;
      border: none;
      border-radius: 3px;
      cursor: pointer;
      width: 100%;
    }
    button:hover {
      background-color: #45a049; /* Темно-зеленый цвет при наведении */
    }
    .register-link {
      text-align: center;
      margin-top: 10px;
    }
    .register-link a {
      color: #4CAF50;
      text-decoration: none;
    }
    </style>

    ```

    Этот класс представляет модель транзитной остановки в системе управления авиаперевозками. У него есть два поля: 
    airport (аэропорт) и datetime (дата и время).

    Может использоваться для отслеживания информации о транзитных остановках в рамках конкретного рейса или на пути между аэропортами. 

=== "ProfileForm"

    ``` vue
    <template>
     <div class="background-container">
         <img src="@/assets/road.jpg" alt="Sky" class="background-image">
      <div class="main-container">
        <form @submit.prevent="updateProfile" class="profile-form">
          <label>
            Username:
            <input v-model="username" type="text" required />
          </label>
          <br />
          <label>
            Email:
            <input v-model="email" type="email" required />
          </label>
          <br />
          <label>
            New Password:
            <input v-model="newPassword" type="password" required />
          </label>
          <br />
          <button type="submit">Update Profile</button>
        </form>
        <div class="buttons-container">
          <router-link to="/aircrafts">
            <button>Aircrafts</button>
          </router-link>
          <router-link to="/crewmembers">
            <button>Crew Members</button>
          </router-link>
          <router-link to="/flights">
            <button>Flights</button>
          </router-link>
          <router-link to="/employees">
            <button>Employees</button>
          </router-link>
        </div>
      </div>
     </div>
    </template>
    
    <script>
    import axios from 'axios';
    export default {
      data() {
        return {
          username: '',
          email: '',
          newPassword: '',
          token: '',
          currentUser: {
            username: '',
            email: ''
          }
        };
      },
      created() {
        const token = localStorage.getItem('token');
        if (token) {
          this.fetchUserProfile(token);
        } else {
          console.error('Token not found');
        }
      },
      methods: {
        fetchUserProfile(token) {
          const userId = this.$route.params.id;
          axios.get(`http://localhost:8000/my_avia_app/auth/profile/${userId}/`, {
            headers: {
              Authorization: `Token ${token}`,
            },
          })
          .then(response => {
            console.log(response.data);
            this.currentUser = response.data;
          })
          .catch(error => {
            console.error(error.response.data);
          });
        }
      }
    };
    </script>
    <style scoped>
    .background-container {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }
    .background-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
    }
    .main-container {
      margin-top: 100px;
    }
    .profile-form {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      background-color: #fff;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
      color: #4CAF50;
    }
    input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 3px;
      margin-top: 10px;
    }
    button {
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 15px;
      border: none;
      border-radius: 3px;
      cursor: pointer;
      margin-top: 5px;
    }
    button:hover {
      background-color: #45a049;
    }
    .buttons-container {
      display: flex;
      justify-content: center;
      margin-top: 20px;
    }
    .buttons-container button {
      margin: 0 10px;
    }
    </style>

    ```

    Этот класс представляет модель транзитной остановки в системе управления авиаперевозками. У него есть два поля: 
    airport (аэропорт) и datetime (дата и время).

    Может использоваться для отслеживания информации о транзитных остановках в рамках конкретного рейса или на пути между аэропортами. 

=== "RegisterForm"

    ``` vue
        <template>
        <div class="background-container">
          <img src="@/assets/sky.jpg" alt="Sky" class="background-image">
          <div class="register-container">
            <form @submit.prevent="register" class="register-form">
    
              <h2>Register</h2>
              <div class="form-group">
                <label for="registerUsername">Username:</label>
                <input v-model="username" type="text" id="registerUsername" required />
              </div>
              <div class="form-group">
                <label for="registerEmail">Email:</label>
                <input v-model="email" type="email" id="registerEmail" required />
              </div>
              <div class="form-group">
                <label for="registerPassword">Password:</label>
                <input v-model="password" type="password" id="registerPassword" required />
              </div>
              <div class="form-group">
                <label for="registerRePassword">Repeat Password:</label>
                <input v-model="rePassword" type="password" id="registerRePassword" required />
              </div>
              <button type="submit">Register</button>
              <p class="login-link">Already have an account? <router-link to="/login">Login</router-link></p>
            </form>
          </div>
        </div>
    </template>
    
    <script>
    import axios from 'axios';
    export default {
      data() {
        return {
          username: '',
          email: '',
          password: '',
          rePassword: ''
        };
      },
      methods: {
        register() {
          if (this.password !== this.rePassword) {
            console.error('Passwords do not match');
            return;
          }
          axios.post('http://localhost:8000/my_avia_app/auth/register/', {
            username: this.username,
            email: this.email,
            password: this.password,
            re_password: this.rePassword
          })
          .then(response => {
            console.log(response.data);
            this.$router.push({  path: '/profile'  });
          })
          .catch(error => {
            console.error(error);
          });
        }
      }
    };
    </script>
    <style scoped>
    .background-container {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }
    .background-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
    }
    .register-container {
      display: flex;
      justify-content: center;
      align-items: center;
      background: #fff;
    }
    .register-form {
      max-width: 300px;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h2 {
      text-align: center;
      color: #4CAF50;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 3px;
    }
    button {
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 15px;
      border: none;
      border-radius: 3px;
      cursor: pointer;
      width: 100%;
    }
    button:hover {
      background-color: #45a049;
    }
    .login-link {
      text-align: center;
      margin-top: 10px;
    }
    .login-link a {
      color: #4CAF50;
      text-decoration: none;
    }
    </style>

    ```

    Этот класс представляет модель транзитной остановки в системе управления авиаперевозками. У него есть два поля: 
    airport (аэропорт) и datetime (дата и время).

    Может использоваться для отслеживания информации о транзитных остановках в рамках конкретного рейса или на пути между аэропортами. 
