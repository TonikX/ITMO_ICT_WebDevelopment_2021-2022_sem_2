<template>
	<div class="container">
		<h3>Rooms</h3>
		<hr>
		<room-row
			v-for="item in items.results"
			:key="item.id"
			:id="item.id"
			:number="item.number"
			:type="item.type"
			:price="item.price"
			:floor="item.floor"
			:cleaners="item.cleaners"
		/>
		<b-button @click="prev()">prev</b-button>
		<b-button @click="next()">next</b-button>
		<div>{{ page }}/{{ items.count }}</div>
		<a href="/room/create" class="btn btn-success">Add</a>
	</div>
</template>

<script>
import axios from 'axios'
import RoomRow from '../../components/Room/Room-row'

export default {
	components: { RoomRow },
	name: 'RoomTable',
	data () {
		return {
			page: 1,
			items: []
		}
	},
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/rooms/',
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
				url: 'http://127.0.0.1:8000/rooms/?page=' + this.page,
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
