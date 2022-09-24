<template>
  <div class="signIn">
    <h2 class="purple--text text--darken-4 text-md-center" >Авторизация</h2>
    <v-form
      @submit.prevent="signIn"
      ref="signInForm"
      class="my-2">
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Логин"
            v-model="signInForm.username"/>
          <v-text-field
            label="Пароль"
            v-model="signInForm.password"
            type="password"/>
          <v-btn type="submit" color="purple" dark>Войти</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15 text-md-center">Ещё нет аккаунта?<br>
      <router-link to="/signup" class="text-decoration-none">Зарегистрироваться</router-link></p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignIn',
  data: () => ({
    signInForm: {
      username: '',
      password: ''
    }
  }),
  methods: {
    async signIn () {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/token/login', this.signInForm)
        this.$refs.signInForm.reset()
        localStorage.setItem('auth_token', response.data.auth_token)
        console.log(response)
        await this.$router.push({ name: 'home' })
        window.location.reload()
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert('Неверный логин или пароль.')
        } else if (e.response.data.password || e.response.data.username) {
          alert('Поля "логин" и "пароль" должны быть заполнены.')
        } else {
          console.error('API error:', e.message)
        }
      }
    }
  }
}
</script>

<style>
</style>
