<template>
    <table class="table">
      <thead class="thead-dark">
        <tr>
          <th>Team</th>
          <th>Username</th>
          <th>Job Number</th>
          <th>Booking Codes</th>
          <th>Booking Date</th>
          <th>Time Tracked</th>
          <th>Task Estimate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.team }}</td>
          <td>{{ item.username }}</td>
          <td>{{ item.job_number }}</td>
          <td>{{ item.booking_codes }}</td>
          <td>{{ item.booking_date }}</td>
          <td>{{ item.time_tracked }}</td>
          <td>{{ item.task_estimate }}</td>
        </tr>
      </tbody>
    </table>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        items: []
      }
    },
    created() {
      axios.get('http://localhost:8000/timelogs/api/')
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
  </script>
  