<template>
<div>
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Chickens</strong></td>
<v-spacer/><v-spacer/>
<v-btn icon color="primary" dark @click='$router.push(`/home`)' style="margin-right: 20px">
<v-icon>mdi-home</v-icon>
</v-btn>
<v-btn color="primary" dark @click='$router.push(`/chickenscreate`)' style="margin-right: 20px">ADD</v-btn>
</v-row>
</v-col>
<v-col>
<v-spacer/><v-spacer/>
<v-spacer/><v-spacer/>
</v-col>
<v-card>
          <v-col
          md="3">
            <p><b>Filter chickens by eggs</b></p>
            <v-form
            @submit.prevent="apply"
          >
              <v-text-field
                label="Enter min eggs"
                v-model="ChickenEggs.min_eggs"
              />
              <v-text-field
                label="Enter max eggs"
                v-model="ChickenEggs.max_eggs"
              />
            </v-form>
             <v-col md="2">
            <p>
            <v-btn color="primary" dark @click='apply' elevation="4">Filter</v-btn>
            </p>
          </v-col>
          </v-col>
          </v-card>
          <v-data-table :headers="headers" :items="elems" class="elevation-1">
          <tr v-for="elem in elems" :key="elem.id" >
              <td>{{ elem.breed }}</td>
              <td>{{ elem.weight }}</td>
              <td>{{ elem.age }}</td>
              <td>{{ elem.egg_amount }}</td>
              <td>{{ elem.cage }}</td>
              <td>{{ elem.prev_eggs }}</td>
              //<td><v-icon small class="mr-2" @click='$router.push(`/chickensedit/${ elem.id }`)'>mdi-pencil</v-icon></td>
              //<td><v-icon small class="mr-2" @click="deleteElem(elem.id)">mdi-delete</v-icon></td>
          </tr>
          <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click='$router.push(`/chickensedit/${ item.id }`)'
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteElem(item.id)"
      >
        mdi-delete
      </v-icon>
    </template>
          </v-data-table>
</div>
</template>

<script>
import axios from 'axios'
const host = 'http://127.0.0.1:8000'
export default {
  name: 'ChickenList1',
  data: () => (
    {
      headers: [
        { text: 'Breed', value: 'breed' },
        { text: 'Cage', value: 'cage' },
        { text: 'Weight', value: 'weight' },
        { text: 'Age', value: 'age' },
        { text: 'Eggs', value: 'egg_amount' },
        { text: 'Previous amount of eggs', value: 'prev_eggs' },
        { text: 'Actions', value: 'actions', sortable: false }],
      ChickenEggs: {
        min_eggs: '',
        max_eggs: ''
      },
      breeds: [],
      cages: [],
      elems: []
    }),
  async created () {
    this.chickensList()
    this.breedsList()
    this.cagesList()
  },
  methods: {
    async apply () {
      try {
        const response = await this.axios
          .get(`${host}/chicken_eggs_range/?egg_amount_max=` + this.ChickenEggs.max_eggs + '&egg_amount_min=' + this.ChickenEggs.min_eggs)
        console.log(response)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.elems = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async chickensList () {
      try {
        const response = await this.axios
          .get(`${host}/chickens/list/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.elems = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async breedsList () {
      try {
        const response = await this.axios
          .get(`${host}/breeds/list/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.breeds = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async cagesList () {
      try {
        const response = await this.axios
          .get(`${host}/cage/list/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.cages = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async deleteElem (elem) {
      try {
        const response = await this.axios
          .delete(`${host}/chickens/info/${elem}`)
        this.$router.go(0)
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
