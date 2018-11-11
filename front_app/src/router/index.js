import Vue from 'vue'
import Router from 'vue-router'
import risk_page from '@/components/RiskPage'
import policies from '@/components/PolicyPage'
// import risk_fields from '@/components/RiskFields'
import risk_details from '@/components/RiskDetailsPage'


Vue.use(Router)

export default new Router({
    name: 'router',
  routes: [
    {
      path: '/',
      name: 'policies',
      component: policies,
    },
    {
      path: '/risk_page',
      name: 'risk_page',
      component: risk_page,
    },
    {
      path: '/risk_page/:id',
      name: 'risk_details',
      component: risk_details,
      props: true
    },
    {
      path: '/policy_details/:id',
      name: 'policy_details',
      component: risk_details,
      props: true
    }
  ]
})