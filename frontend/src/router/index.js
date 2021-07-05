import Vue from 'vue'
import Router from 'vue-router'
import Playing from "@/components/Playing";
import Start from "@/components/Start";


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Start',
      component: Start,
    },
    {
      path: '/playing',
      name: 'Playing',
      component: Playing,
    },
  ],
  mode: 'history',
})
