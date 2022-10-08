<template>
  <div class="signin1">
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Enter username"
            v-model="signInForm.username"
          />
          <v-text-field
            label="Enter password"
            v-model="signInForm.password"
            type="password"
          />
          <v-btn color="primary" dark @click="goLogin">Log in</v-btn>

          <p class="mt-5">No account? <v-btn @click="goRegister" color="primary" dark>Register</v-btn></p>
        </v-col>
      </v-row>
  </div>
</template>

<script>
const host = 'http://127.0.0.1:8000'
export default {
  name: 'SignIn',
  data: () => ({
    signInForm: {
      username: '',
      password: ''
    }
  }),
  methods: {
    async goRegister () {
      this.$router.push('/signup')
    },
    async goLogin () {
      const token = await this.axios
        .post(`${host}/auth/token/login/`, this.signInForm)
        .then((res) => {
          console.log(res.data.auth_token)
          return res.data.auth_token
        })
        .catch((error) => {
          console.log(error)
        })
      localStorage.setItem('token', token)
      this.axios.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`
      this.$router.push('/home')
    }
  }
}
</script>
