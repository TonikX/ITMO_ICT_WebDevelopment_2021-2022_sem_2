<template>
	<div>
		<div class="container">
			<h2 class="text-center">Hotel Administrator</h2>
		</div>
		<div class="container">
			<form class="d-flex">
				<input v-model="query_name" class="form-control me-2" placeholder="Search Clients" aria-label="Search Clients">
				<button @click="search()" class="btn btn-outline-success" type="button">Find</button>
			</form>
			<br>
			<guest-row
			v-for="item in items"
			:key="item.id"
			:id="item.id"
			:passport_number="item.passport_number"
			:name="item.name"
			:surname="item.surname"
			:middlename="item.middlename"
			:from_location="item.from_location"
			:check_in_date="item.check_in_date"
			:check_out_date="item.check_out_date"
			:prev_check_out_date="item.prev_check_out_date"
			:room="item.room"
			/>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import GuestRow from './Guest/Guest-row.vue'

export default {
	components: { GuestRow },
	name: 'AdminPanel',
	data () {
		return {
			query_name: '',
			items: []
		}
	},
	methods: {
		search () {
			axios({
				method: 'get',
				url: 'http://localhost:8000/guests?search=' + this.query_name,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.items = response.data.results
			})
		}
	}
}

</script>
