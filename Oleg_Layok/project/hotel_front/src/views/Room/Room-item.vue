<template>
	<div class="container">
		<h1>Room Number: {{item.number}}</h1>\
		<p>Room Type: {{item.type}}</p>
		<p>Price: {{item.price}}</p>
		<p>Floor: {{item.floor}}</p>
		<p>Staff: {{item.cleaners}}</p>

		<a :href="'/room/update/' + this.$route.params.id" class="btn btn-success">Edit</a>
		<button @click="delete_item()" class="btn btn-danger">Delete</button>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'RoomItem',
	data () {
		return {
			item: []
		}
	},
	props: ['id'],
	created () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/rooms/' + this.$route.params.id,
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.item = response.data
		})
	},
	methods: {
		delete_item () {
			if (confirm('Удалить?')) {
				axios({
					method: 'delete',
					url: 'http://127.0.0.1:8000/rooms/' + this.$route.params.id,
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					console.log(response)
					window.location.href = '/rooms'
				})
			}
		}
	}
}
</script>

<style>

</style>
