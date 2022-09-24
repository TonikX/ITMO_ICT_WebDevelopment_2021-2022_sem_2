<template>
  <div>
    <v-card
    levation="3"
    outlined
    class="my-2"
    >
      <v-card-title>
        <v-icon v-if="this.bookOnHold" class="mx-4" color="green">mdi-book-open-page-variant</v-icon>
        <h2>{{ this.book.title }}</h2>
        <v-spacer></v-spacer>
        <div v-if="isAuth" class="ma-4 text-end">
          <v-menu
          bottom
          offset-y
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="purple"
                dark
                icon
                v-bind="attrs"
                v-on="on"
              >
              <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
            </template>
            <v-list>
              <v-list-item v-if="!this.bookOnHold" @click="takeOutBook" link>
                <v-list-title class="purple--text text--darken-4">Взять</v-list-title>
              </v-list-item>
              <v-list-item v-if="this.bookOnHold" @click="returnBook" link>
                <v-list-title class="purple--text text--darken-4">Вернуть</v-list-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </v-card-title>
      <div class="mx-4">
        <v-img
        :src=book.cover
        width="150"
        ></v-img>
      </div>
      <v-card-text>
        <div class="text-h5 black--text">
          Авторы: <b>{{ this.book.authors }}</b> <br>
          Жанр: {{ this.book.genre }} <br>
          Год издания: {{ this.book.publication_year }} <br>
          Издательство: {{ this.book.publisher }} <br>
          Библиотечный номер: {{ this.book.book_cypher }} <br>
          <br>
          Залы:
          <ul>
            <li v-for="hall in this.book.book_hall" v-bind:key="hall" v-bind:hall="hall">
              {{ hall.title }}
            </li>
          </ul>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'BookView',
  data () {
    return {
      book: Object,
      reader: Object,
      bookOnHold: false,
      bookReaderID: '',
      isAuth: localStorage.getItem('auth_token') || false
    }
  },
  created () {
    this.loadBook()
    this.loadReaderData()
  },
  methods: {
    async loadBook () {
      this.book_url = 'http://127.0.0.1:8000/library/books/' + this.$route.params.id
      const response = await axios.get(this.book_url)
      this.book = response.data
    },
    async loadReaderData () {
      const response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('auth_token')}`
          }
        })
      this.reader = response.data
      await this.checkOnHold()
    },
    async checkOnHold () {
      this.reader_url = 'http://127.0.0.1:8000/library/readers/' + this.reader.id
      const response = await axios.get(this.reader_url)
      console.log(response.data)
      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data.reader_book)) {
        if (value.id === this.book.id) {
          this.bookOnHold = true
          this.bookReaderID = value
          break
        }
      }
    },
    takeOutBook () {
      this.$router.push({ name: 'take_out', params: { id: this.book.id } })
    },
    async returnBook () {
      const response = await axios.get('http://127.0.0.1:8000/library/reader_books/')
      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(response.data)) {
        if (value.reader.id === this.reader.id && value.book.id === this.book.id) {
          this.bookReaderID = value.id
          break
        }
      }
      await this.$router.push({ name: 'return', params: { id: this.bookReaderID } })
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
