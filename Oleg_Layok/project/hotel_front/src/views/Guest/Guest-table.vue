<template>
	<div class="container">
		<h3>Guests</h3>
		<hr>
		<guest-row
			v-for="item in items.results"
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
		<b-button @click="prev()">prev</b-button>
		<b-button @click="next()">next</b-button>
		<div>{{ page }}/{{ items.count }}</div>
		<a href="/guest/create" class="btn btn-success">Add</a>
	</div>
</template>

<script>
import axios from 'axios'
import GuestRow from '../../components/Guest/Guest-row'

export default {
	components: { GuestRow },
	name: 'GuestTable',
	data () {
		return {
			page: 1,
			items: []
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/guests/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.items = response.data
		})
	},
	methods: {
		next: function () {
			this.prev_disable = false
			console.log(this.items.count)

			if (this.items.count > this.page) {
				this.page = this.page + 1
			}
			if (this.items.count === this.page) {
				this.next_disable = true
			}
			this.new_data()
		},
		prev: function () {
			this.next_disable = false

			if (this.page > 1) {
				this.page--
			}
			if (this.page === 1) {
				this.prev_disable = true
			}
			this.new_data()
		},
		new_data: function () {
			console.log(this.page)
			axios({
				method: 'get',
				url: 'http://127.0.0.1:8000/guests/?page=' + this.page,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.items = response.data
				console.log(this.items)
			})
		}
	}
}
</script>

<style>

</style>
