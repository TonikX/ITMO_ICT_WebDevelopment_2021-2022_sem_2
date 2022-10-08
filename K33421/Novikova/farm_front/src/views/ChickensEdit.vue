<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Edit chicken</strong></td>
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
            label="Breed"
            v-model="addForm.breed"
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
  name: 'ChickensEdit',
  data: () => ({
    chick_id: 0,
    chick_now: {},
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
  created () {
    this.breedsList()
    this.cagesList()
    this.checkChicken()
  },
  methods: {
    async checkChicken () {
      try {
        this.chick_id = this.$route.params.chicken_id
        await this.axios
          .get(`${host}/chickens/info/${this.chick_id}`)
          .then((res) => {
            this.chick_now = res.data
            this.addForm.breed = this.chick_now.breed
            this.addForm.cage = this.chick_now.cage
            this.addForm.weight = this.chick_now.weight
            this.addForm.age = this.chick_now.age
            this.addForm.egg_amount = this.chick_now.egg_amount
            this.addForm.prev_eggs = this.chick_now.prev_eggs
            console.log(this.chick_now)
          })
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
    async edit () {
      await this.axios
        .put(`${host}/chickens/info/${this.chick_id}`, this.addForm)
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
