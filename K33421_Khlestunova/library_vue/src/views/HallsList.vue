<template>
  <div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
    <div class='text-center ma-4'>
        <h1>Залы</h1>
    </div>
    <v-spacer></v-spacer>
    <v-divider></v-divider>
    <v-row class="d-flex justify-center">
      <v-col cols="5" class="px-5 mx-2">
        <p>Количество экземпляров книг</p>
         <v-range-slider
            v-model="range"
            :max="max"
            :min="min"
            hide-details
            class="align-center"
            @change="rangeFilter"
          >
            <template v-slot:prepend>
              <v-text-field
                :value="range[0]"
                class="mt-0 pt-0"
                hide-details
                single-line
                type="number"
                style="width: 60px"
                @change="$set(range, 0, $event)"
              ></v-text-field>
            </template>
            <template v-slot:append>
              <v-text-field
                :value="range[1]"
                class="mt-0 pt-0"
                hide-details
                single-line
                type="number"
                style="width: 60px"
                @change="$set(range, 1, $event)"
              ></v-text-field>
            </template>
          </v-range-slider>
      </v-col>
    </v-row>
      <v-row
      elevation="2"
      class="ma-2"
      v-for="hall in halls" v-bind:key="hall.id"
      >
        <v-card-title>
          <h2>{{ hall.title }}</h2><span>(Вместимость: {{ hall.capacity }})</span>
        </v-card-title>
        <v-card-text style="font-size:1em">
          <ul>
            <div v-for="book_in_hall in book_in_halls" :key="book_in_hall">
              <li v-if="book_in_hall.hall.id === hall.id">
                <v-btn text color="black" @click="goBook(book_in_hall.book.id)">{{ book_in_hall.book.title }}</v-btn> -
                {{ book_in_hall.book.authors }}
                ({{book_in_hall.count}} шт.)
                <v-spacer></v-spacer>
              </li>
            </div>
          </ul>
        </v-card-text>
      </v-row>
    <v-divider></v-divider>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HallList',
  data () {
    return {
      books: '',
      halls: [],
      book_in_halls: [],
      allLoaded: false,
      authorized: false,
      min: 0,
      max: 500,
      range: [10, 500]
    }
  },
  created () {
    this.loadHalls()
    this.loadBookInHalls()
    if (localStorage.getItem('auth_token')) {
      this.authorized = true
    }
  },
  methods: {
    async loadHalls () {
      this.halls_url = 'http://127.0.0.1:8000/library/halls/'
      const response = await axios.get(this.halls_url)
      this.halls = response.data
    },
    async loadBookInHalls () {
      this.book_in_halls_url = 'http://127.0.0.1:8000/library/halls/books/'
      const response = await axios.get(this.book_in_halls_url)
      this.book_in_halls = response.data
    },
    async rangeFilter () {
      var params = new URLSearchParams()
      params.append('count_min', this.range[0])
      params.append('count_max', this.range[1])
      this.filterParams = {
        params: params
      }
      const response = await axios.get('http://127.0.0.1:8000/library/halls/books/', this.filterParams)
      this.book_in_halls = response.data
    },
    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
    }
  }
}
</script>
