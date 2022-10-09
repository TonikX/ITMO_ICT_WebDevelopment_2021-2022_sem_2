<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>New breed</strong></td>
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
  name: 'BreedsCreate',
  data: () => ({
    addForm: {
      breed: '',
      avg_eggs: 0,
      avg_weight: 0,
      diet: ''
    }
  }),
  methods: {
    async postNew () {
      await this.axios
        .post(`${host}/breeds/create/`, this.addForm)
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
