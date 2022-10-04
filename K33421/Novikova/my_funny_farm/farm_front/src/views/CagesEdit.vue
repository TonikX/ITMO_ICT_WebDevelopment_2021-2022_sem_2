<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>Edit cage</strong></td>
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
            v-model="addForm.cage"
            label="Cage"
          ></v-text-field>
          <v-text-field
            v-model="addForm.row"
            label="Row"
          ></v-text-field>
          <v-text-field
            v-model="addForm.shed"
            label="Shed"
          ></v-text-field>
          <v-text-field
            v-model="addForm.square"
            label="Square"
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
  name: 'CagesEdit',
  data: () => ({
    cage_id: 0,
    cage_now: {},
    addForm: {
      cage: 0,
      row: 0,
      shed: 0,
      square: 0
    }
  }),
  created () {
    this.checkCage()
  },
  methods: {
    async checkCage () {
      try {
        this.cage_id = this.$route.params.cage_id
        await this.axios
          .get(`${host}/cage/info/${this.cage_id}`)
          .then((res) => {
            this.cage_now = res.data
            this.addForm.cage = this.cage_now.cage
            this.addForm.row = this.cage_now.row
            this.addForm.shed = this.cage_now.shed
            this.addForm.square = this.cage_now.square
            console.log(this.cage_now)
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async edit () {
      await this.axios
        .put(`${host}/cage/info/${this.cage_id}`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$router.push('/cageslist1')
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/cageslist1')
    }
  }
}
</script>
