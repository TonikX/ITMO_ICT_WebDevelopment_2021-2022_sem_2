<template>
	<div class="container">
		<b-form class="w-50 mx-auto" method='post'>
			<h2>Cleaning schedule</h2>
			<b-form-group
				label="Room"
				label-for="number"
			>
				<b-form-input
					name="number"
					type="number"
					v-model="room"
				/>
			</b-form-group>

			<b-form-group
				label="Staff"
				label-for="staff"
			>
				<b-form-select name="staff" v-model="staff" :options="cleaners"></b-form-select>

			</b-form-group>

			<b-form-group
				label="Cleaning date"
				label-for="date_time"
			>
				<b-form-datepicker
					name="date_time"
					v-model="date_time"
				/>
			</b-form-group>
			<b-button @click="save()" type="button" variant="success">Save</b-button>
		</b-form>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'CleaningForm',
	data () {
		return {
			id: '',
			room: '',
			staff: '',
			date_time: '',
			cleaners: []
		}
	},
	props: ['mode'],
	mounted () {
		this.id = this.$route.params.id
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/staff/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			response.data.results.forEach(element => {
				this.cleaners.push({ value: element.id, text: element.name })
			})
		})

		if (this.mode === 'update') {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/cleaning/' + this.id,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				this.staff = response.data.staff
				this.room = response.data.room
				this.cleaning_day = response.data.cleaning_day
			})
		}
	},
	methods: {
		save () {
			let method
			let url
			if (this.mode === 'add') {
				method = 'post'
				url = 'http://127.0.0.1:8000/cleaning/'
			} else {
				method = 'patch'
				url = 'http://127.0.0.1:8000/cleaning/' + this.id + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					room: this.room,
					staff: this.staff,
					date_time: this.date_time
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				window.location.href = '/cleanings'
			}).catch(error => {
				console.log(error.response)
			})
		}
	}
}
</script>

<style>

</style>
