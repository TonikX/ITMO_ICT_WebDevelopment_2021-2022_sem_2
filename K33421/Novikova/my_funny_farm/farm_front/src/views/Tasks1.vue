<template>
<div>
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Tasks</strong></td>
<v-spacer/><v-spacer/>
<v-btn icon color="primary" dark @click='$router.push(`/home`)' style="margin-right: 20px">
<v-icon>mdi-home</v-icon>
</v-btn>
<v-btn color="primary" dark @click='$router.push(`/taskscreate`)' style="margin-right: 20px">ADD</v-btn>
</v-row>
</v-col>
<v-col>
<v-spacer/><v-spacer/>
<v-spacer/><v-spacer/>
</v-col>
<v-card>
          <v-col
          md="3">
            <p><b>Filter tasks</b></p>
            <v-form
            @submit.prevent="apply"
          >
            <v-select
            label="Type of work"
            v-model="addForm.work_type"
            :items="work_types"
            >
            <option v-for="tp in work_types" :key="tp.id">
            {{ tp }}
            </option>
          </v-select>
          <v-text-field
            label="Position"
            v-model="addForm.position"
            >
          </v-text-field>
              <v-checkbox
            label="Is the work done?"
            v-model="addForm.work_status"
            ></v-checkbox>
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
          </tr>
          <template v-slot:item.work_status="{ item }">
          <v-simple-checkbox
          v-model="item.work_status"
          disabled
          ></v-simple-checkbox>
          </template>
          <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click='$router.push(`/tasksedit/${ item.id }`)'
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
  name: 'TaskList1',
  data: () => (
    {
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Cage', value: 'cage' },
        { text: 'Date', value: 'work_date' },
        { text: 'Type of work', value: 'work_type' },
        { text: 'Status', value: 'work_status' },
        { text: 'Details', value: 'details' },
        { text: 'Actions', value: 'actions', sortable: false }],
      workers: [],
      cages: [],
      elems: [],
      work_types: ['cl', 'fd', 'med'],
      addForm: {
        work_type: '',
        position: '',
        work_status: ''
      }
    }),
  async created () {
    this.tasksList()
    this.workersList()
    this.cagesList()
  },
  methods: {
    async apply () {
      try {
        const response = await this.axios
          .get(`${host}/work_search_date_order/?work_status=` + this.addForm.work_status + '&search=' + this.addForm.work_type + '+' + this.addForm.position)
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
    async tasksList () {
      try {
        const response = await this.axios
          .get(`${host}/work/list/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.elems = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async workersList () {
      try {
        const response = await this.axios
          .get(`${host}/workers/list/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.workers = response.data
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
          .delete(`${host}/work/info/${elem}`)
        this.$router.go(0)
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
