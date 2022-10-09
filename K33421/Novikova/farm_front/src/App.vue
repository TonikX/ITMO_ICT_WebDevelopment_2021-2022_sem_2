<template>
  <v-app>
    <v-app-bar
      app
      color="dark"
      dark
    >
      <div class="d-flex align-center">
        <v-toolbar-title>Funny Farm</v-toolbar-title>
        <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
    <v-btn>
      <router-link to="/workerslist1">Workers</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/chickenslist1">Chickens</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/breedslist1">Breeds</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/cageslist1">Cages</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/taskslist1">Tasks</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/signin1">Sign In</router-link>
    </v-btn>

    <v-btn>
      <router-link to="/signup">Sign Up</router-link>
    </v-btn>
    <v-btn v-if='isAuth' icon @click="logout">
          <v-icon>mdi-export</v-icon>
        </v-btn>
        </v-toolbar-items>
      </div>
    </v-app-bar>

    <v-main class="my-5 px-5">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'App',
  data: () => ({
    isAuth: ''
  }),
  created () {
    this.isAuth = localStorage.getItem('token') !== null && localStorage.getItem('token') !== undefined
    if (localStorage.getItem('token')) {
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`
    }
    console.log(this.isAuth, localStorage.getItem('token'), this.axios.defaults.headers.common.Authorization)
  },
  methods: {
    logout () {
      localStorage.removeItem('token')
      this.$router.push({ name: 'SignIn' })
    }
  }
}
</script>
