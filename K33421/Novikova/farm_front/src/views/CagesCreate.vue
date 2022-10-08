<template>
<div class="add">
<v-col>
<v-spacer/><v-spacer/>
<v-row>
<td><strong>New cage</strong></td>
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
  name: 'CagesCreate',
  data: () => ({
    addForm: {
      cage: 0,
      row: 0,
      shed: 0,
      square: 0
    }
  }),
  methods: {
    async postNew () {
      await this.axios
        .post(`${host}/cage/create/`, this.addForm)
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
