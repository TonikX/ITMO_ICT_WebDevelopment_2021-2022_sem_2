<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
      <v-card-title>
        <h2>{{ this.book.title }}</h2>
      </v-card-title>

      <v-card-text>
        <div class="text--primary">
          Авторы: <b>{{ this.book.authors }}</b> <br>
          Жанр: {{ this.book.genre }} <br>
          Год издания: {{ this.book.publication_year }} <br>
          Издательство: {{ this.book.publisher }} <br>
          Библиотечный номер: {{ this.book.book_cypher }} <br>
        </div>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-text>
        <div class="text--primary">
          Дата выдачи: {{ this.issue_date }} <br>
          Срок возврата: {{ this.due_date }}
        </div>
      </v-card-text>
    </v-card>

    <v-btn style="margin-top:0.5cm" color="primary" light @click="returnBook">Вернуть</v-btn>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'BookReturn',
  data: () => ({
    book: Object,
    reader: Object,
    issue_date: '',
    due_date: ''
  }),
  created () {
    this.loadReaderBookData()
  },
  methods: {
    async loadReaderBookData () {
      this.book_url = 'http://127.0.0.1:8000/library/reader_books/' + this.$route.params.id
      const response = await axios.get(this.book_url)
      this.book = response.data.book
      this.reader = response.data.reader
      this.issue_date = response.data.issue_date
      this.due_date = response.data.due_date
    },
    async returnBook () {
      this.return_url = 'http://127.0.0.1:8000/library/return/' + this.$route.params.id
      await axios.delete(this.return_url)
      alert('Вы вернули книгу в библиотеку')
      await this.$router.push({ name: 'catalogue' })
    }
  }
}
</script>
<style>
</style>
