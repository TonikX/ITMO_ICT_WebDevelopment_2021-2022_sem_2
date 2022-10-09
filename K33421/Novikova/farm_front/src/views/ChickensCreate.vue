<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>New chicken</strong></td>
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
      @submit.prevent="postNew"
      ref="addForm"
      class="my-2"
    >
    <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Breed"
            v-model="addForm.breed"
            @click="breedsList"
            :items="breeds"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="b in breeds" :key="b.id">
              {{ b.label }}
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
            v-model="addForm.weight"
            label="Weight"
            type="number"
          ></v-text-field>
          <v-text-field
            v-model="addForm.age"
            label="Age"
            type="number"
          ></v-text-field>
          <v-text-field
            v-model="addForm.egg_amount"
            label="Eggs"
            type="number"
          ></v-text-field>
          <v-text-field
            v-model="addForm.prev_eggs"
            label="Previous amount of eggs"
            type="number"
          ></v-text-field>
          <v-row>
          <v-btn color="primary" dark @click="postNew">ADD</v-btn>
          <spacer style="margin-right: 20px"/>
          <v-btn color="primary" dark @click='$router.go(-1)' elevation="4" style="margin-right: 20px">Cancel</v-btn>
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
  name: 'ChickensCreate',
  data: () => ({
    breeds: [],
    cages: [],
    addForm: {
      breed: '',
      cage: '',
      weight: 0,
      age: 0,
      egg_amount: 0,
      prev_eggs: 0
    }
  }),
  methods: {
    async breedsList () {
      try {
        const response = await this.axios
          .get(`${host}/breeds/list/`)
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        const data = response.data
        for (let i = 0; i < response.data.length; i++) {
          const label = `${data[i].breed}`
          const id = data[i].id
          this.breeds.push({ label: label, code: id })
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
    async postNew () {
      await this.axios
        .post(`${host}/chickens/create/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$router.push('/chickenslist1')
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/chickenslist1')
    }
  }
}
</script>
