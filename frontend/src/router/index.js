import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DesignSystemView from '../views/DesignSystemView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/design-system',
    name: 'design-system',
    component: DesignSystemView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
