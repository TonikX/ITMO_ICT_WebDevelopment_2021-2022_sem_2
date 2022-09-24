<template>
  <div>
    <v-card
      tile
      outlined
      class="my-2"
    >
    <v-card outlined tile color="purple darken-4">
      <h1 outlined class="white--text ma-4 text-center">Каталог библиотеки</h1>
    </v-card>
      <v-container fluid>
        <v-row class="mx-2">
          <v-col cols="5">
            <v-text-field
            v-model="search"
            outlined
            color="deep-purple"
            placeholder="Начните вводить название книги"
            prepend-inner-icon="mdi-magnify"
            label="Искать"
            @input="allFilter"
            ></v-text-field>
          </v-col>
          <v-col cols="5">
            <v-row>
              <v-col>
                <v-checkbox
                v-model="genreSelected"
                label="Роман"
                value="Роман"
                @click="allFilter"
                ></v-checkbox>
              </v-col>
              <v-col>
                <v-checkbox
                  v-model="genreSelected"
                  label="Фантастика"
                  value="Фантастика"
                  @click="allFilter"
                ></v-checkbox>
              </v-col>
              <v-col>
                <v-checkbox
                  v-model="genreSelected"
                  label="Драма"
                  value="Драма"
                  @click="allFilter"
                ></v-checkbox>
              </v-col>
              <v-col>
                <v-checkbox
                  v-model="genreSelected"
                  label="Поэма"
                  value="Поэма"
                  @click="allFilter"
                ></v-checkbox>
              </v-col>
            </v-row>
          </v-col>
          <v-col>
            <v-btn-toggle
              v-model="sortDesc"
              mandatory
            >
              <v-btn
                large
                depressed
                color="blue"
                :value="false"
                @click="allFilter"
              >
                <v-icon>mdi-arrow-up</v-icon>
              </v-btn>
              <v-btn
                large
                depressed
                color="blue"
                :value="true"
                @click="allFilter"
              >
                <v-icon>mdi-arrow-down</v-icon>
              </v-btn>
            </v-btn-toggle>
          </v-col>
        </v-row>
        <v-row>
          <v-col
          v-for="book in books"
          v-bind:key="book.title"
          cols="6"
          class="d-flex align-center">
            <div align="center">
              <v-img
              :src=book.cover
              @click="goBook(book.id)"
              width="150"
              ></v-img>
            </div>
            <div class="text-center ma-3">
              <v-btn outlined color="blue" @click="goBook(book.id)">
                {{ book.title }}
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-container>
      <v-row class="d-flex align-center">
        <v-col>
          <v-btn v-if="showNextButton" class="blue lighten-2 mx-4" @click="loadNext">Next</v-btn>
          <v-btn v-if="showPrevButton" class="pink lighten-2" @click="loadPrev">Previous</v-btn>
        </v-col>
        <v-col>
          <div class="mx-4 text-end">
            Страница {{ this.current_page }} из {{ pages }}
          </div>
        </v-col>
        <v-col>
          <v-text-field
          label="Количество книг/стр"
          v-model="itemsPerPage">
          </v-text-field>
        </v-col>
        <v-col>
          <v-btn @click="updateItemsPerPage">Update</v-btn>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'BookList',
  data: () => ({
    books: [],
    errors: [],
    current_page: 1,
    showNextButton: false,
    showPrevButton: false,
    itemsPerPage: 2,
    pages: 0,
    search: '',
    sortDesc: false,
    sliderMin: 1800,
    sliderMax: 2022,
    range: [1800, 2022],
    genreSelected: []
  }),
  created () {
    this.allFilter()
  },
  computed: {
    ordering () {
      var res = 'publication_year'
      if (this.sortDesc) res = '-' + res
      return res
    }
  },
  methods: {
    loadNext () {
      if (this.current_page + 1 <= this.pages) {
        this.current_page += 1
        this.allFilter()
      }
    },
    loadPrev () {
      if (this.current_page - 1 >= 1) {
        this.current_page -= 1
        this.allFilter()
      }
    },
    async allFilter () {
      var params = new URLSearchParams()
      params.append('page', this.current_page)
      params.append('page_size', this.itemsPerPage)
      params.append('search', this.search)
      this.genreSelected.forEach(element => {
        params.append('genre', element)
      })
      params.append('ordering', this.ordering)
      this.filter_params = {
        params: params
      }
      const response = await axios.get('http://127.0.0.1:8000/library/books/', this.filter_params)
      this.books = response.data.results
      this.showNextButton = false
      this.showPrevButton = false
      this.pages = response.data.pages
      if (response.data.next) {
        this.showNextButton = true
      }
      if (response.data.previous) {
        this.showPrevButton = true
      }
    },
    updateItemsPerPage () {
      this.allFilter()
    },
    goBook (bookID) {
      this.$router.push({ name: 'book', params: { id: bookID } })
    },
    goHome () {
      this.$router.push({ name: 'home' })
    }
  }
}

</script>

<style>
</style>
