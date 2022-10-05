<template>
	<div class="container">
		<h1>Room: {{item.room}}</h1>
		<p>Staff: {{staff}}</p>
		<p>Cleaning date: {{item.date_time}}</p>

		<a :href="'/cleaning/update/' + this.$route.params.id" class="btn btn-success">Edit</a>
		<button @click="delete_item()" class="btn btn-danger">Delete</button>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'cleaningsItem',
	data () {
		return {
			item: [],
			staff: ''
		}
	},
	props: ['id'],
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/cleaning/' + this.$route.params.id,
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.item = response.data
			console.log(this.item.staff)

			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/staff/' + this.item.staff + '/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				this.staff = response.data.name
			})
		})
	},
	methods: {
		delete_item () {
			if (confirm('Delete?')) {
				axios({
					method: 'delete',
					url: 'http://127.0.0.1:8000/cleaning/' + this.$route.params.id,
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					console.log(response)
					window.location.href = '/cleanings'
				})
			}
		}
	}
}
</script>

<style>

</style>
