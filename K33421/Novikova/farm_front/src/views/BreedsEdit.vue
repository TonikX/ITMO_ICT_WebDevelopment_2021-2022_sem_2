<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Edit breed</strong></td>
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
            v-model="addForm.breed"
            label="Breed"
          ></v-text-field>
          <v-text-field
            v-model="addForm.avg_eggs"
            label="Average eggs"
          ></v-text-field>
          <v-text-field
            v-model="addForm.avg_weight"
            label="Average weight"
          ></v-text-field>
          <v-text-field
            v-model="addForm.diet"
            label="Diet"
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
  name: 'BreedsEdit',
  data: () => ({
    breed_id: 0,
    breed_now: {},
    addForm: {
      breed: '',
      avg_eggs: 0,
      avg_weight: 0,
      diet: ''
    }
  }),
  created () {
    this.checkBreed()
  },
  methods: {
    async checkBreed () {
      try {
        this.breed_id = this.$route.params.breed_id
        await this.axios
          .get(`${host}/breeds/info/${this.breed_id}`)
          .then((res) => {
            this.breed_now = res.data
            this.addForm.breed = this.breed_now.breed
            this.addForm.avg_eggs = this.breed_now.avg_eggs
            this.addForm.avg_weight = this.breed_now.avg_weight
            this.addForm.diet = this.breed_now.diet
            console.log(this.breed_now)
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async edit () {
      await this.axios
        .put(`${host}/breeds/info/${this.breed_id}`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$router.push('/breedslist1')
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/breedslist1')
    }
  }
}
</script>
