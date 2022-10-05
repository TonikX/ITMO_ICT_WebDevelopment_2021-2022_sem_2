<template>
	<div class="container">
		<b-form class="w-50 mx-auto" method='post'>
			<b-form-group
				label="Passport"
				label-for="passport_number"
			>
				<b-form-input
					name="passport_number"
					type="text"
					v-model="passport_number"
				/>
				<p>{{passport_number_error}}</p>
			</b-form-group>

			<b-form-group
				label="Guest Name"
				label-for="name"
			>
				<b-form-input
					name="name"
					type="text"
					v-model="name"
				/>
				<p>{{name_error}}</p>
			</b-form-group>

			<b-form-group
				label="Guest Surname"
				label-for="surname"
			>
				<b-form-input
					name="surname"
					type="text"
					v-model="surname"
				/>
				<p>{{surname_error}}</p>
			</b-form-group>

			<b-form-group
				label="Guest Middlename"
				label-for="middlename"
			>
				<b-form-input
					name="middlename"
					type="text"
					v-model="middlename"
				/>
				<p>{{middlename_error}}</p>
			</b-form-group>

			<b-form-group
				label="Location"
				label-for="from_location"
			>
				<b-form-input
					name="from_location"
					type="text"
					v-model="from_location"
				/>
				<p>{{from_location_error}}</p>
			</b-form-group>

			<b-form-group
				label="Check in"
				label-for="check_in_date"
			>
				<b-form-datepicker
					name="check_in_date"
					v-model="check_in_date"
				/>
			</b-form-group>

			<b-form-group
				label="Check out"
				label-for="check_out_date"
			>
				<b-form-datepicker
					name="check_out_date"
					v-model="check_out_date"
				/>
			</b-form-group>

			<b-form-group
				label="Prev Check out"
				label-for="prev_check_out_date"
			>
				<b-form-datepicker
					name="prev_check_out_date"
					v-model="prev_check_out_date"
				/>
			</b-form-group>

			<b-form-group
				label="Room"
				label-for="room"
			>
				<b-form-input
					name="room"
					type="number"
					v-model="room"
					/>
			</b-form-group>

			<b-button @click="save()" type="button" variant="success">Save</b-button>
		</b-form>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'GuestForm',
	data () {
		return {
			id: '',
			passport_number: '',
			passport_number_error: '',
			name: '',
			name_error: '',
			surname: '',
			surname_error: '',
			middlename: '',
			middlename_error: '',
			from_location: '',
			from_location_error: '',
			check_in_date: '',
			check_out_date: '',
			prev_check_out_date: '',
			room: ''
		}
	},
	props: ['mode'],
	mounted () {
		this.id = this.$route.params.id
		console.log(this.id)
		if (this.mode === 'update') {
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/guests/' + this.id,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				this.passport_number = response.data.passport_number
				this.name = response.data.name
				this.surname = response.data.surname
				this.middlename = response.data.middlename
				this.from_location = response.data.from_location
				this.check_in_date = response.data.check_in_date
				this.check_out_date = response.data.check_out_date
				this.prev_check_out_date = response.data.prev_check_out_date
				this.room = response.data.room
			})
		}
	},
	methods: {
		save () {
			let method
			let url
			this.id = this.$route.params.id
			if (this.mode === 'add') {
				method = 'post'
				url = 'http://127.0.0.1:8000/guests/'
			} else {
				method = 'patch'
				url = 'http://127.0.0.1:8000/guests/' + this.id + '/'
			}

			axios({
				method: method,
				url: url,
				responseType: 'json',
				data: {
					passport_number: this.passport_number,
					name: this.name,
					surname: this.surname,
					middlename: this.middlename,
					from_location: this.from_location,
					check_in_date: this.check_in_date,
					check_out_date: this.check_out_date,
					prev_check_out_date: this.prev_check_out_date,
					room: this.room
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response)
				window.location.href = '/guests'
			}).catch(error => {
				console.log(error.response)
			})
		}
	}
}
</script>

<style>

</style>
