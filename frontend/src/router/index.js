import Vue from 'vue'
import Router from 'vue-router'
import login from '@/views/login'
import register from '@/views/register'
import index from '@/views/index'
import about from '@/views/about'
import details from '@/views/details'
import search from '@/views/search'
import shopcart from '@/views/shopcart'
import commodity from '@/views/commodity'
import goods_list from '@/views/goods_list'
import custom from '@/views/custom'
import order from '@/views/order'
import add_goods from '@/views/add_goods'
import edit_goods from '@/views/edit_goods'
import discount from '@/views/discount'
import information from '@/views/information'
import slider1 from '@/views/component/slider1'
import change from '@/views/component/change'
import test from '@/views/component/test'
import $ from 'jquery'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/slider1',
      name: 'slider1',
      component: slider1
    },
    {
      path: '/change',
      name: 'change',
      component: change
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/about',
      name: 'about',
      component: about
    },
    {
      path: '/commodity',
      name: 'commodity',
      component: commodity
    },
    {
      path: '/details/:goods_num',
      name: 'details',
      component: details
    },
    {
      path: '/shopcart',
      name: 'shopcart',
      component: shopcart
    },
    {
      path: '/search/:name',
      name: 'search',
      component: search
    },
    {
      path: '/custom',
      name: 'custom',
      component: custom
    },
    {
      path: '/information',
      name: 'information',
      component: information
    },
    {
      path: '/order',
      name: 'order',
      component: order
    },
    {
      path: '/discount',
      name: 'discount',
      component: discount
    },
    {
      path: '/add_goods',
      name: 'add_goods',
      component: add_goods
    },
    {
      path: '/goods_list',
      name: 'goods_list',
      component: goods_list
    },
    {
      path: '/edit_goods/:id',
      name: 'edit_goods',
      component: edit_goods
    }
  ]
})
