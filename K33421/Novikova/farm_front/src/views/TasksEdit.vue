<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Edit task</strong></td>
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
          <v-select
            label="Worker name"
            v-model="addForm.name"
            @click="workersList"
            :items="workers"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="w in workers" :key="w.id">
              {{ w.label }}
            </option>
          </v-select>
          <v-select
            label="Cage"
            v-model="addForm.cage"
            @click="cagesList"
            :items="cages"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="c in cages" :key="c.id">
              {{ c.label }}
            </option>
          </v-select>
          <v-text-field
            label="Date of work"
            v-model="addForm.work_date"
            type="date"
            ></v-text-field>
          <v-select
            label="Type of work"
            v-model="addForm.work_type"
            :items="work_types"
            >
            <option v-for="tp in work_types" :key="tp.id">
            {{ tp }}
            </option>
          </v-select>
          <v-checkbox
            label="Is the work done?"
            v-model="addForm.work_status"
            ></v-checkbox>
          <v-text-field
            label="More details"
            v-model="addForm.details"
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
  name: 'TasksEdit',
  data: () => ({
    task_id: 0,
    task_now: {},
    workers: [],
    cages: [],
    work_types: ['cl', 'fd', 'med'],
    addForm: {
      name: '',
      cage: '',
      work_date: '',
      work_type: '',
      work_status: false,
      details: ''
    }
  }),
  created () {
    this.workersList()
    this.cagesList()
    this.checkTask()
  },
  methods: {
    async checkTask () {
      try {
        this.task_id = this.$route.params.task_id
        await this.axios
          .get(`${host}/work/info/${this.task_id}`)
          .then((res) => {
            this.task_now = res.data
            this.addForm.name = this.task_now.name
            this.addForm.cage = this.task_now.cage
            this.addForm.work_date = this.task_now.work_date
            this.addForm.work_type = this.task_now.work_type
            this.addForm.work_status = this.task_now.work_status
            this.addForm.details = this.task_now.details
            console.log(this.task_now)
          })
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
        const data = response.data
        for (let i = 0; i < response.data.length; i++) {
          const label = `${data[i].name}`
          const id = data[i].id
          this.workers.push({ label: label, code: id })
        }
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
        const data = response.data
        for (let i = 0; i < response.data.length; i++) {
          const label = `${data[i].shed} ${data[i].row} ${data[i].cage}`
          const id = data[i].id
          this.cages.push({ label: label, code: id })
        }
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async edit () {
      await this.axios
        .put(`${host}/work/info/${this.task_id}`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$router.push('/taskslist1')
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/taskslist1')
    }
  }
}
</script>
