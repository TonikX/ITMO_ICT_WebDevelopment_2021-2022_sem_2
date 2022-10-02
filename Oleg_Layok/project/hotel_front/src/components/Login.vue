<template>
	<div class="container">
		<div class="mb-3">
			<button @click="tab=1" class="btn btn-primary mr-2">Sign In</button>
			<button @click="tab=2" class="btn btn-primary">Sign Up</button>
		</div>
		<div v-if="tab===1" class="">
			<b-form class="w-50 mx-auto" method='post'>
				<h2>Sign In</h2>
				<b-form-group
					label="Login"
					label-for="username"
				>
					<b-form-input
						name="username"
						type="text"
						v-model="username"
						:rules="[v => !!v || 'Username is required']"
						required
					/>
					<p>{{login_error}}</p>
				</b-form-group>

				<b-form-group
					label="password"
					label-for="password"
				>
					<b-form-input
						name="password"
						type="password"
						v-model="password"
						:rules="[v => !!v || 'Password is required']"
						required
					/>
					<p>{{password_error}}</p>
				</b-form-group>

				<b-button @click="signIn()" type="button" variant="success">Log in</b-button>
			</b-form>
		</div>
		<div v-if="tab===2" class="">
			<b-form class="w-50 mx-auto" method='post'>
				<h2>Sign Up</h2>
				<b-form-group
					label="Login"
					label-for="username"
				>
					<b-form-input
						name="username"
						type="text"
						v-model="username"
						:rules="[v => !!v || 'Username is required']"
						required
					/>
					<p>{{login_error}}</p>
				</b-form-group>

				<b-form-group
					label="password"
					label-for="password"
				>
					<b-form-input
						name="password"
						type="password"
						v-model="password"
						:rules="[v => !!v || 'Password is required']"
						required
					/>
					<p>{{password_error}}</p>
				</b-form-group>

				<b-form-group
					label="email"
					label-for="email"
				>
					<b-form-input
						name="email"
						type="email"
						v-model="email"
						:rules="emailRules"
						required
					/>
					<p>{{email_error}}</p>
				</b-form-group>

				<b-button @click="signUp()" type="button" variant="success">Register</b-button>
			</b-form>
		</div>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Login',
	data () {
		return {
			username: '',
			password: '',
			login_error: '',
			password_error: '',
			email: '',
			email_error: '',
			tab: 1,
			emailRules: [
				v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
			]
		}
	},
	methods: {
		signIn () {
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/auth/token/login/',
				data: {
					username: this.username,
					password: this.password
				},
				responseType: 'json'
			}).then((response) => {
				sessionStorage.setItem('auth_token', response.data.auth_token)

				window.location.reload()
			}).catch((error) => {
				this.login_error = 'login_error'
				this.password_error = 'password_error'
				try {
					this.login_error = error.response.data.username[0]
				} catch (error) {
					console.log(error.response)
				}
				try {
					this.password_error = error.response.data.password[0]
				} catch (error) {
					console.log(error.response)
				}
			})
		},
		signUp () {
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/auth/users/',
				data: {
					active: true,
					username: this.username,
					password: this.password,
					email: this.email
				},
				responseType: 'json'
			}).then((response) => {
				console.log(response.data.auth_token)
				window.location.reload()
			}).catch((error) => {
				this.login_error = 'login_error'
				this.password_error = 'password_error'
				this.email_error = 'email_erroe'
				try {
					this.login_error = error.response.data.username[0]
				} catch (error) {
					console.log(error.response)
				}
				try {
					this.password_error = error.response.data.password[0]
				} catch (error) {
					console.log(error.response)
				}
				try {
					this.email_error = error.response.data.email[0]
				} catch (error) {
					console.log(error.response)
				}
			})
		}
	}

}

</script>

<style>

</style>
