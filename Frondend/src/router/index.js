import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '../views/HomeView.vue'
import DetailPage from '../views/DetailPage.vue'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',  // 主页面路径
      name: 'Homeview',
      component: HomeView
    },
    {
      path: '/detail/:id',  // 分页面路径 (使用动态参数 id)
      name: 'DetailPage',
      component: DetailPage
    }
  ]
})