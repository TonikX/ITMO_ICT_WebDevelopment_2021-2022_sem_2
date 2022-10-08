<template>
<div>
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Workers</strong></td>
<v-spacer/><v-spacer/>
<v-btn icon color="primary" dark @click='$router.push(`/home`)' style="margin-right: 20px">
<v-icon>mdi-home</v-icon>
</v-btn>
<v-btn color="primary" dark @click='$router.push(`/workerscreate`)' style="margin-right: 20px">ADD</v-btn>
</v-row>
</v-col>
<v-col>
<v-spacer/><v-spacer/>
<v-spacer/><v-spacer/>
</v-col>
<v-card>
          <v-col
          md="3">
            <p><b>Search workers by position</b></p>
            <v-form
            @submit.prevent="apply"
          >
              <v-text-field
                label="Enter worker position"
                v-model="WorkerPosition.position"
              />
            </v-form>
             <v-col md="2">
            <p>
            <v-btn color="primary" dark @click='apply' elevation="4">Search</v-btn>
            </p>
          </v-col>
          </v-col>
          </v-card>
          <v-data-table :headers="headers" :items="elems" class="elevation-1">
          <tr v-for="elem in elems" :key="elem.id" >
          </tr>
          <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click='$router.push(`/workersedit/${ item.id }`)'
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
  name: 'WorkersList1',
  data: () => (
    {
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Passport', value: 'passport' },
        { text: 'Salary', value: 'salary' },
        { text: 'Position', value: 'position' },
        { text: 'Actions', value: 'actions', sortable: false }],
      WorkerPosition: {
        position: ''
      },
      elems: []
    }),
  async created () {
    this.WorkersList()
  },
  methods: {
    async apply () {
      try {
        const response = await this.axios
          .get(`${host}/workers_with_position_salary/` + '?position=' + this.WorkerPosition.position)
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
    async WorkersList () {
      try {
        const response = await this.axios
          .get(`${host}/workers/list/`)
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
          .delete(`${host}/workers/info/${elem}`)
        this.$router.go(0)
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
