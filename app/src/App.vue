<template>
  
  <div>
    <Header />
    <router-view></router-view>
  </div>
  <div>
  
  </div>
</template>

<script>
//import Table from './components/timelogs_table.vue';
import Header from './components/Header_global.vue';

export default {
  components: {
    Header
  }
}
</script>
