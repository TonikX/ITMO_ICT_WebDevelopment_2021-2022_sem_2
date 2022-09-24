<template>
<div>
    <div>
      <h1 class="purple--text text--darken-4 text-md-center">Личный кабинет</h1>
    </div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h3 class="purple--text text--darken-4 text-md-center">Информация о пользователе</h3>
      </v-card-title>

      <v-card-text>
        <div class="text-h6 indigo--text text--darken-4">
          Имя: <b>{{ this.reader.first_name }}</b> <br>
          Фамилия: <b>{{ this.reader.last_name }}</b> <br>
          Логин: {{ this.reader.username }} <br>
          Номер билета: {{ this.reader.card_number }} <br>
          Дата рождения: {{ this.reader.date_of_birth }} <br>
          Образование: {{ this.reader.education }} <br>
          Ученая степень: <span class="blue--text">{{ this.reader.degree ? 'есть' : 'нет' }} </span><br>
          Паспортные данные: {{ this.reader.passport }} <br>
          Адрес: {{ this.reader.address }} <br>
          Телефон: {{ this.reader.phone }} <br>
        </div>
      </v-card-text>
    </v-card>

  <v-card
    elevation="2"
    outlined
    class="my-2">
    <v-card-text class="text-h6 indigo--text text--darken-4">
      Вы сейчас читаете:
      <ul>
          <li v-for="book in reader.reader_book" v-bind:key="book" v-bind:book="book">
            <a @click.prevent="goBook(book.id)">{{ book.title }}</a>, {{ book.authors }}
          </li>
        </ul>
    </v-card-text>
  </v-card>

  <v-card>
    <v-card-text  style="margin-top:1cm" class="text-h6 blue--text darken-4--text">
      <router-link to="/profile_edit" class="text-decoration-none">Редактировать профиль</router-link>
    </v-card-text>
  </v-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ReaderProfile',
  data () {
    return {
      reader: Object
    }
  },
  created () {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData () {
      try {
        const response = await axios
          .get('http://127.0.0.1:8000/auth/users/me/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('auth_token')}`
            }
          })
        this.reader = response.data
        await this.loadCurrentlyReading()
      } catch (e) {
        localStorage.removeItem('auth_token')
      }
    },
    async loadCurrentlyReading () {
      this.cur_read_url = 'http://127.0.0.1:8000/library/readers/' + this.reader.id
      const response = await axios.get(this.cur_read_url)
      this.reader = response.data
      console.log(response)
    },
    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
    },
    goCatalogue () {
      this.$router.push({ name: 'catalogue' })
    },
    goHome () {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style>
</style>
