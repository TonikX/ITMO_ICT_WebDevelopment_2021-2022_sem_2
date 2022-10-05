<template>
	<div class="container">
		<b-form class="w-50 mx-auto" method='post'>
			<h2>Room</h2>
			<b-form-group
				label="Room Number"
				label-for="number"
			>
				<b-form-input
					name="number"
					type="number"
					v-model="number"
				/>
				<p>{{number_error}}</p>
			</b-form-group>

			<b-form-group
				label="Room Type"
				label-for="type"
			>
				<b-form-select name='type' v-model="type" :options="options"></b-form-select>
			</b-form-group>

			<b-form-group
				label="Price"
				label-for="price"
			>
				<b-form-input
					name="price"
					type="number"
					v-model="price"
				/>
				<p>{{price_error}}</p>
			</b-form-group>

			<b-form-group
				label="Floor Number"
				label-for="floor"
			>
				<b-form-input
					name="floor"
					type="number"
					v-model="floor"
				/>
				<p>{{floor_error}}</p>
			</b-form-group>

			<b-button @click="save()" type="button" variant="success">Save</b-button>
		</b-form>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'RoomForm',
	data () {
		return {
			id: '',
			number: '',
			number_error: '',
			type: '',
			options: ['1', '2', '3', '4'],
			price: '',
			price_error: '',
			floor: '',
			floor_error: ''
		}
	},
	props: ['mode'],
	mounted () {
		this.id = this.$route.params.id
		if (this.mode === 'update') {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/rooms/' + this.id,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				this.number = response.data.number
				this.type = response.data.type
				this.price = response.data.price
				this.floor = response.data.floor
				this.cleaners = response.data.cleaners
			})
		}
	},
	methods: {
		save () {
			let method
			let url
			if (this.mode === 'add') {
				method = 'post'
				url = 'http://127.0.0.1:8000/rooms/'
			} else {
				method = 'patch'
				url = 'http://127.0.0.1:8000/rooms/' + this.number + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					number: this.number,
					type: this.type,
					price: this.price,
					floor: this.floor,
					cleaners: this.cleaners
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				window.location.href = '/rooms'
			}).catch(error => {
				console.log(error.response)
			})
		}
	}
}
</script>

<style>

</style>
