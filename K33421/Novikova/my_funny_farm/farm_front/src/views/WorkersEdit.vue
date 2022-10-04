<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Edit worker</strong></td>
<v-spacer/><v-spacer/>
<v-btn icon color="primary" dark @click='$router.push(`/home`)' style="margin-right: 20px">
<v-icon>mdi-home</v-icon>
</v-btn>
<v-btn color="primary" dark @click='$router.go(-1)' elevation="4" style="margin-right: 20px">Back</v-btn>&nbsp;&nbsp;
</v-row>
</v-col>
<v-col>
<v-spacer/><v-spacer/>
<v-spacer/><v-spacer/>
</v-col>
<v-form
      @submit.prevent="edit"
      ref="addForm"
      class="my-2"
    >
    <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            v-model="addForm.name"
            label="Name"
          ></v-text-field>
          <v-text-field
            v-model="addForm.passport"
            label="Passport"
          ></v-text-field>
          <v-text-field
            v-model="addForm.salary"
            label="Salary"
            type="number"
          ></v-text-field>
          <v-text-field
            v-model="addForm.position"
            label="Position"
          ></v-text-field>
          <v-row>
          <v-btn color="primary" dark @click="edit">Edit</v-btn>
          <spacer style="margin-right: 20px"></spacer>
          <v-btn color="primary" dark @click='$router.go(-1)' elevation="4">Cancel</v-btn>
          </v-row>
        </v-col>
    </v-row>
</v-form>
</div>
</template>

<script>
import axios from 'axios'
const host = 'http://127.0.0.1:8000'
export default {
  name: 'WorkersEdit',
  data: () => ({
    worker_id: 0,
    worker_now: {},
    addForm: {
      name: '',
      passport: '',
      salary: 0,
      position: ''
    }
  }),
  created () {
    this.checkWorker()
  },
  methods: {
    async checkWorker () {
      try {
        this.worker_id = this.$route.params.worker_id
        await this.axios
          .get(`${host}/workers/info/${this.worker_id}`)
          .then((res) => {
            this.worker_now = res.data
            this.addForm.name = this.worker_now.name
            this.addForm.passport = this.worker_now.passport
            this.addForm.salary = this.worker_now.salary
            this.addForm.position = this.worker_now.position
            console.log(this.worker_now)
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async edit () {
      await this.axios
        .put(`${host}/workers/info/${this.worker_id}`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$router.push('/workerslist1')
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/workerslist1')
    }
  }
}
</script>
