<template>
<div>
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Breeds</strong></td>
<v-spacer/><v-spacer/>
<v-btn icon color="primary" dark @click='$router.push(`/home`)' style="margin-right: 20px">
<v-icon>mdi-home</v-icon>
</v-btn>
<v-btn color="primary" dark @click='$router.push(`/breedscreate`)' style="margin-right: 20px">ADD</v-btn>
</v-row>
</v-col>
<v-col>
<v-spacer/><v-spacer/>
<v-spacer/><v-spacer/>
</v-col>
          <v-data-table :headers="headers" :items="elems" class="elevation-1">
          <tr v-for="elem in elems" :key="elem.id" >
          </tr>
          <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click='$router.push(`/breedsedit/${ item.id }`)'
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
  name: 'BreedList1',
  data: () => (
    {
      headers: [
        { text: 'Breed', value: 'breed' },
        { text: 'Average eggs', value: 'avg_eggs' },
        { text: 'Average weight', value: 'avg_weight' },
        { text: 'Diet', value: 'diet' },
        { text: 'Actions', value: 'actions', sortable: false }],
      elems: []
    }),
  async created () {
    this.breedsList()
  },
  methods: {
    async breedsList () {
      try {
        const response = await this.axios
          .get(`${host}/breeds/list/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.elems = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async deleteElem (elem) {
      try {
        const response = await this.axios
          .delete(`${host}/breeds/info/${elem}`)
        this.$router.go(0)
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
