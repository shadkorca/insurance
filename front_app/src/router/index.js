import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import risks from '@/components/RiskPage'
import policies from '@/components/PolicyPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/risks_detail',
      name: 'risks',
      component: risks
    },
    {
      path: '/policies',
      name: 'policies',
      component: policies
    }

  ]
})