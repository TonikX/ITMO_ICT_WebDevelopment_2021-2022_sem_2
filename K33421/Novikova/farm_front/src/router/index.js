import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUp from '../views/SignUp.vue'
import SignIn from '../views/SignIn.vue'
import ChickensList from '../views/Chickens.vue'
import BreedsList from '../views/Breeds.vue'
import CagesList from '../views/Cages.vue'
import TasksList from '../views/Tasks.vue'
import WorkersList from '../views/Workers.vue'
import SignIn1 from '../views/SignIn1.vue'
import ChickensList1 from '../views/Chickens1.vue'
import ChickensCreate from '../views/ChickensCreate.vue'
import ChickensEdit from '../views/ChickensEdit.vue'
import BreedsList1 from '../views/Breeds1.vue'
import BreedsCreate from '../views/BreedsCreate.vue'
import BreedsEdit from '../views/BreedsEdit.vue'
import WorkersList1 from '../views/Workers1.vue'
import WorkersCreate from '../views/WorkersCreate.vue'
import WorkersEdit from '../views/WorkersEdit.vue'
import CagesList1 from '../views/Cages1.vue'
import CagesCreate from '../views/CagesCreate.vue'
import CagesEdit from '../views/CagesEdit.vue'
import TasksList1 from '../views/Tasks1.vue'
import TasksCreate from '../views/TasksCreate.vue'
import TasksEdit from '../views/TasksEdit.vue'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/signin1',
    name: 'signin1',
    component: SignIn1
  },
  {
    path: '/chickenslist1',
    name: 'ChickensList1',
    component: ChickensList1
  },
  {
    path: '/chickenscreate',
    name: 'ChickensCreate',
    component: ChickensCreate
  },
  {
    path: '/chickensedit/:chicken_id',
    name: 'ChickensEdit',
    component: ChickensEdit
  },
  {
    path: '/breedslist1',
    name: 'BreedsList1',
    component: BreedsList1
  },
  {
    path: '/breedscreate',
    name: 'BreedsCreate',
    component: BreedsCreate
  },
  {
    path: '/breedsedit/:breed_id',
    name: 'BreedsEdit',
    component: BreedsEdit
  },
  {
    path: '/workerslist1',
    name: 'WorkersList1',
    component: WorkersList1
  },
  {
    path: '/workerscreate',
    name: 'WorkersCreate',
    component: WorkersCreate
  },
  {
    path: '/workersedit/:worker_id',
    name: 'WorkersEdit',
    component: WorkersEdit
  },
  {
    path: '/cageslist1',
    name: 'CagesList1',
    component: CagesList1
  },
  {
    path: '/cagescreate',
    name: 'CagesCreate',
    component: CagesCreate
  },
  {
    path: '/cagesedit/:cage_id',
    name: 'CagesEdit',
    component: CagesEdit
  },
  {
    path: '/taskslist1',
    name: 'TasksList1',
    component: TasksList1
  },
  {
    path: '/taskscreate',
    name: 'TasksCreate',
    component: TasksCreate
  },
  {
    path: '/tasksedit/:task_id',
    name: 'TasksEdit',
    component: TasksEdit
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
