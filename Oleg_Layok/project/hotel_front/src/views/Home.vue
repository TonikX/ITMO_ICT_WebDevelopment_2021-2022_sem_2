<template>
	<div>
		<login v-if="!is_auth"/>
		<admin-panel v-else/>

		<div v-if="is_auth" class="container">
			<form class="d-flex">
				<input v-model="search" class="form-control me-2" placeholder="Search Room" aria-label="Search Room">
				<button @click="reset_page()" class="btn btn-outline-success" type="button">Find</button>
			</form>
			<div class="mb-3">
				<b-button @change="notify()" class="mr-2" @click="sort_by_number()">Sort by number</b-button>
				<b-button  @change="notify()" @click="sort_by_price()">Sort by price</b-button>
			</div>
			<br>
			<div>Room Type</div>
			<label for="c1">
				<input @change="reset_page()" v-model="c1" id="c1" type="checkbox" name="choice"> 1
			</label>
			<br>
			<label for="c2">
				<input @change="reset_page()" v-model="c2" id="c2" type="checkbox" name="choice"> 2
			</label>
			<br>
			<label for="c3">
				<input @change="reset_page()" v-model="c3" id="c3" type="checkbox" name="choice"> 3
			</label>
			<br>
			<label for="c4">
				<input @change="reset_page()" v-model="c4" id="c4" type="checkbox" name="choice"> 4
			</label>
			<br>
			<div>
				<label for="price_start">
					price start
					<input @change="reset_page()" id="price_start" v-model="start_price" type="number">
				</label>
				<label for="price_end">
					price end
					<input @change="reset_page()" id="price_end" v-model="end_price" type="number">
				</label>
			</div>

			<b-table :items="items.results"></b-table>
			<b-button @click="prev()">prev</b-button>
			<b-button @click="next()">next</b-button>
			<div>{{ page }}/{{ items.count }}</div>
		</div>
	</div>
</template>

<script>
import Login from '../components/Login.vue'
import AdminPanel from '../components/Admin-panel'
import axios from 'axios'

export default {
	components: { Login, AdminPanel },
	name: 'Home',
	data () {
		return {
			is_auth: false,
			items: [],
			sort_number: true,
			sort_price: false,
			c1: false,
			c2: false,
			c3: false,
			c4: false,
			search: '',
			request: '',
			page: 1,
			next_disable: false,
			prev_disable: true,
			start_price: 0,
			end_price: 0
		}
	},
	mounted () {
		this.is_auth = Boolean(sessionStorage.getItem('auth_token') !== null)
		console.log('http://127.0.0.1:8000/rooms/?search=' + this.search + (this.sort_price ? '&ordering=price' : '&ordering=number' + this.c1 ? '&type=1' : '' + this.c2 ? '&type=2' : '' + this.c3 ? '&type=3' : '' + this.c4 ? '&type=4' : ''))
		this.request = 'http://127.0.0.1:8000/rooms/?search=' + this.search + (this.sort_price ? '&ordering=price' : '&ordering=number' + (this.c1 ? '&type=1' : '') + (this.c2 ? '&type=2' : '') + (this.c3 ? '&type=3' : '') + (this.c4 ? '&type=4' : ''))
		axios({
			method: 'get',
			url: this.request,
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.items = response.data
			console.log(this.items)
		})
	},
	methods: {
		sort_by_number: function () {
			this.sort_number = true
			this.sort_price = false
			this.notify()
		},
		sort_by_price: function () {
			this.sort_number = false
			this.sort_price = true
			this.notify()
		},
		notify: function () {
			let range = ''
			console.log(this.start_price)
			console.log(this.end_price)
			if (parseInt(this.end_price) > 0 && parseInt(this.start_price) >= parseInt(this.end_price)) {
				this.start_price = this.end_price - 1
			}
			if (parseInt(this.start_price) < parseInt(this.end_price)) {
				range = '&price_min=' + this.start_price + '&price_max=' + this.end_price
			}
			console.log(this.page)
			this.request = 'http://127.0.0.1:8000/rooms/?search=' + this.search + (this.sort_price ? '&ordering=price' : '&ordering=number' + (this.c1 ? '&type=1' : '') + (this.c2 ? '&type=2' : '') + (this.c3 ? '&type=3' : '') + (this.c4 ? '&type=4' : '') + range + '&page=' + this.page)
			axios({
				method: 'get',
				url: this.request,
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then((response) => {
				this.items = response.data
				console.log(this.items)
			})
		},
		next: function () {
			this.prev_disable = false

			if (this.items.count > this.page) {
				this.page = this.page + 1
			}
			if (this.items.count === this.page) {
				this.next_disable = true
			}
			console.log(this.page)
			this.notify()
		},
		prev: function () {
			this.next_disable = false

			if (this.page > 1) {
				this.page--
			}
			if (this.page === 1) {
				this.prev_disable = true
			}
			this.notify()
		},
		reset_page: function () {
			this.page = 1
			this.notify()
		}
	}
}
</script>

<style>

</style>
