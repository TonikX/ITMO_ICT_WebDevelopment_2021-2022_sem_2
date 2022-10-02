<template>
	<div class="container">
		<h3>Guest Name: {{item.name}}</h3>
		<h3>Guest Surname: {{item.surname}}</h3>
		<h3>Guest Middlename: {{item.middlename}}</h3>
		<p>Passport: {{item.passport_number}}</p>
		<p>Location: {{item.from_location}}</p>
		<p>Check in: {{item.check_in_date}}</p>
		<p>Check out: {{item.check_out_date}}</p>
		<p>Prev Check out: {{item.prev_check_out_date}}</p>
		<p>Room: {{item.room}}</p>
		<a :href="'/guest/update/' + this.$route.params.id" class="btn btn-success">Edit</a>
		<button @click="delete_item()" class="btn btn-danger">Delete</button>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'GuestItem',
	data () {
		return {
			item: []
		}
	},
	props: ['id'],
	created () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/guests/' + this.$route.params.id,
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.item = response.data
			console.log(response)
		})
	},
	methods: {
		delete_item () {
			if (confirm('Удалить?')) {
				axios({
					method: 'delete',
					url: 'http://127.0.0.1:8000/guests/' + this.$route.params.id,
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					console.log(response)
					window.location.href = '/guests'
				})
			}
		}
	}
}
</script>

<style>

</style>
