import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Superadmin from '../views/Superadmin.vue'

import GuestTable from '../views/Guest/Guest-table.vue'
import GuestItem from '../views/Guest/Guest-item.vue'
import GuestUpdate from '../views/Guest/Guest-update.vue'
import GuestCreate from '../views/Guest/Guest-create.vue'

import RoomTable from '../views/Room/Room-table.vue'
import RoomItem from '../views/Room/Room-item.vue'
import RoomUpdate from '../views/Room/Room-update.vue'
import RoomCreate from '../views/Room/Room-create.vue'

import CleaningTable from '../views/Cleaning/Cleaning-table.vue'
import CleaningItem from '../views/Cleaning/Cleaning-item.vue'
import CleaningUpdate from '../views/Cleaning/Cleaning-update.vue'
import CleaningCreate from '../views/Cleaning/Cleaning-create.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},

	{
		path: '/superadmin',
		name: 'Superadmin',
		component: Superadmin
	},

	{
		path: '/guests',
		name: 'GuestTable',
		component: GuestTable
	},
	{
		path: '/guests/:id',
		name: 'GuestItem',
		component: GuestItem
	},
	{
		path: '/guest/update/:id',
		name: 'GuestUpdate',
		component: GuestUpdate
	},
	{
		path: '/guest/create',
		name: 'GuestCreate',
		component: GuestCreate
	},

	{
		path: '/rooms',
		name: 'RoomTable',
		component: RoomTable
	},
	{
		path: '/rooms/:id',
		name: 'RoomItem',
		component: RoomItem
	},
	{
		path: '/room/update/:id',
		name: 'RoomUpdate',
		component: RoomUpdate
	},
	{
		path: '/room/create',
		name: 'RoomCreate',
		component: RoomCreate
	},

	{
		path: '/cleanings',
		name: 'CleaningTable',
		component: CleaningTable
	},
	{
		path: '/cleanings/:id',
		name: 'CleaningItem',
		component: CleaningItem
	},
	{
		path: '/cleaning/update/:id',
		name: 'CleaningUpdate',
		component: CleaningUpdate
	},
	{
		path: '/cleaning/create',
		name: 'CleaningCreate',
		component: CleaningCreate
	}
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router
