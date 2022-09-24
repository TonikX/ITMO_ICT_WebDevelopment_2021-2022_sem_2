import Vue from 'vue'
import Router from 'vue-router'
import AboutView from '../views/AboutView'
import HomeView from '../views/HomeView'
import BookList from '../views/BookList'
import BookView from '../views/BookView'
import SignUp from '../views/SignUp'
import SignIn from '../views/SignIn'
import ReaderProfile from '../views/ReaderProfile'
import ReaderProfileEdit from '../views/ReaderProfileEdit'
import BookTakeOut from '../views/BookTakeOut'
import BookReturn from '../views/BookReturn'
import HallsList from '../views/HallsList'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/books',
      name: 'catalogue',
      component: BookList
    },
    {
      path: '/books/:id',
      name: 'book',
      component: BookView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignIn
    },
    {
      path: '/profile',
      name: 'reader_profile',
      component: ReaderProfile
    },
    {
      path: '/profile_edit',
      name: 'profile_edit',
      component: ReaderProfileEdit
    },
    {
      path: '/take_out/',
      name: 'take_out',
      component: BookTakeOut
    },
    {
      path: '/return/:id',
      name: 'return',
      component: BookReturn
    },
    {
      path: '/halls/',
      name: 'halls',
      component: HallsList
    }
  ]
})
