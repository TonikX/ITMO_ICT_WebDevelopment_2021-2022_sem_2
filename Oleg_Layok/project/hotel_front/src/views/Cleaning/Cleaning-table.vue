<template>
	<div class="container">
		<h3>Cleaning Schedule</h3>
		<hr>
		<cleaning-row
			v-for="item in items.results"
			:key="item.id"
			:id="item.id"
			:room="item.room"
			:staff="item.staff"
			:date_time="item.date_time"
		/>
		<b-button @click="prev()">prev</b-button>
		<b-button @click="next()">next</b-button>
		<div>{{ page }}/{{ items.count }}</div>
		<a href="/cleaning/create" class="btn btn-success">Add</a>
	</div>
</template>

<script>
import axios from 'axios'
import CleaningRow from '../../components/Cleaning/Cleaning-row'

export default {
	components: { CleaningRow },
	name: 'CleaningTable',
	data () {
		return {
			page: 1,
			items: []
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/cleaning/',
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
				url: 'http://127.0.0.1:8000/cleaning/?page=' + this.page,
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
