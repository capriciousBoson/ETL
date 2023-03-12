<template>
  <div>
    <router-link to="/reports">show reports</router-link>
  </div>
    <div>
      <Table />
    </div>
  </template>
  
  <script>
  import Table from './timelogs_table.vue';
  export default {
    name: 'Timelogs_page',
    components: {
      Table
    }
  };
  </script>