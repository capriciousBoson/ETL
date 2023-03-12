<template>
  <div class="container" style="width:40% ;">
    <h3 style="padding-left: 157px">Team vs Time tracked</h3>
  <VuePlotly :data="datapie" :layout="layout" :display-mode-bar="false"></VuePlotly>
  </div>
</template>

<script>


import { VuePlotly } from 'vue3-plotly'
import axios from 'axios';

export default {
  components: {
    VuePlotly
  },

  data() {
    return {
      datapie: [{
        values: undefined,
        labels: undefined,
        type: "pie"
      }],
      layout: {
        font: {
        size: 17 // modify the font size here
        },
        legend: {
        orientation: 'h',
        y: -0.1 // adjust the y position to move the legends below the chart
            }
      },
      data: [],
      teams: [],
      mergedTeams: [],
    }
  },
  mounted() {
      axios
        .get('http://localhost:8000/timelogs/api/')
        .then((response) => {
          this.data = response.data;
          this.extractTeams();
          this.mergeTeams();
          this.pie();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
      extractTeams() {
        this.teams = this.data.map(({ team, time_tracked }) => ({
          team: team,
          time_tracked: time_tracked,
        }));
      },
      mergeTeams() {
        const teams = this.teams.reduce((accumulator, current) => {
          const existingTeam = accumulator.find(
            (team) => team.team === current.team
          );
          if (existingTeam) {
            existingTeam.time_tracked += current.time_tracked;
          } else {
            accumulator.push({
              team: current.team,
              time_tracked: current.time_tracked,
            });
          }
          return accumulator;
        }, []);
        this.mergedTeams = teams;
      },
      pie() {
        this.datapie[0].values = this.mergedTeams.map(team => team.time_tracked);
        this.datapie[0].labels = this.mergedTeams.map(team => team.team);
      }

    },
}
</script>