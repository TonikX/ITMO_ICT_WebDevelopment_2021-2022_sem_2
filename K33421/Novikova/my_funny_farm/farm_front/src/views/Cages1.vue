<template>
<div>
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Cages</strong></td>
<v-spacer/><v-spacer/>
<v-btn icon color="primary" dark @click='$router.push(`/home`)' style="margin-right: 20px">
<v-icon>mdi-home</v-icon>
</v-btn>
<v-btn color="primary" dark @click='$router.push(`/cagescreate`)' style="margin-right: 20px">ADD</v-btn>
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
        @click='$router.push(`/cagesedit/${ item.id }`)'
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
  name: 'CageList1',
  data: () => (
    {
      headers: [
        { text: 'Cage', value: 'cage' },
        { text: 'Row', value: 'row' },
        { text: 'Shed', value: 'shed' },
        { text: 'Square', value: 'square' },
        { text: 'Actions', value: 'actions', sortable: false }],
      elems: []
    }),
  async created () {
    this.cagesList()
  },
  methods: {
    async cagesList () {
      try {
        const response = await this.axios
          .get(`${host}/cage/list/`)
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
          .delete(`${host}/cage/info/${elem}`)
        this.$router.go(0)
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
