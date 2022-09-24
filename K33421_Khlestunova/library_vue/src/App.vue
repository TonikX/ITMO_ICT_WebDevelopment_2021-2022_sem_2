<template>
  <v-app>
    <v-app-bar
      app
      color="deep-purple darken-4"
      dark
    >
        <v-toolbar-title><h1>Библиотека</h1></v-toolbar-title>
        <v-spacer></v-spacer>
          <div v-if="isAuth"><v-btn @click="logout" style="color: white; text-decoration-none" text><h3>LogOut</h3></v-btn></div>
          <router-link v-if="!isAuth" to="/signin" style="color: white" class="text-decoration-none">
            <v-btn class="mr-3" hight="40px" color="white" text>
              <h3>SignIn</h3>
            </v-btn>
          </router-link>
          <router-link v-if="!isAuth" to="/signup" style="color: white" class="text-decoration-none">
            <v-btn class="mr-3" hight="40px" color="white" text>
              <h3>SignUp</h3>
            </v-btn>
          </router-link>
    </v-app-bar>
    <v-main>
      <v-container >
        <router-view/>
      </v-container>
      <br><br>
      <div>
        <v-bottom-navigation
          absolute
          color="white"
          >
          <router-link :to="'/'" class="text-decoration-none">
            <v-btn class="mr-2" height="50px" color="deep-purple accent-4" text>
              <span>Главная</span>
              <v-icon>mdi-home</v-icon>
            </v-btn>
          </router-link>
          <router-link to="/about" class="text-decoration-none">
            <v-btn class="mr-2" height="50px" color="deep-purple accent-4" text>
              <span>О библиотеке</span>
              <v-icon>mdi-information</v-icon>
            </v-btn>
          </router-link>
          <router-link v-if="isAuth" to="/profile" class="text-decoration-none">
            <v-btn class="mr-2" height="50px" color="deep-purple accent-4" text>
              <span>Профиль</span>
              <v-icon>mdi-account</v-icon>
            </v-btn>
          </router-link>
          <router-link to="/books" class="text-decoration-none">
            <v-btn class="mr-2" height="50px" color="deep-purple accent-4" text>
              <span>Каталог</span>
              <v-icon>mdi-book-multiple</v-icon>
            </v-btn>
          </router-link>
          <router-link v-if="isAuth" to="/halls" class="text-decoration-none">
            <v-btn class="mr-2" height="50px" color="deep-purple accent-4" text>
              <span>Залы</span>
              <v-icon>mdi-bookshelf</v-icon>
            </v-btn>
          </router-link>
        </v-bottom-navigation>
      </div>
    </v-main>
  </v-app>
</template>
<script>
export default {
  data () {
    return {
      value: 1,
      active: true,
      isAuth: ''
    }
  },
  created () {
    this.isAuth = localStorage.getItem('auth_token') !== null && localStorage.getItem('auth_token') !== undefined
    if (localStorage.getItem('auth_token')) {
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('auth_token')}`
    }
    console.log(this.isAuth, localStorage.getItem('auth_token'), this.axios.defaults.headers.common.Authorization)
  },
  methods: {
    logout () {
      window.location.reload()
      console.log(localStorage.getItem('auth_token'))
      localStorage.removeItem('auth_token')
      console.log(localStorage.getItem('auth_token'))
      delete this.axios.defaults.headers.common.Authorization
    }
  }
}
</script>
