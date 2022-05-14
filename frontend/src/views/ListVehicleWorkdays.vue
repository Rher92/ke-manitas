<template>
  <section>
    <h1>Vehiculos usados por día</h1>
    <hr/><br/>
    <div>
      <ul>
        <li v-for="item in vehicles.items" v-bind:key="item.id">
          <a v-on:click="goToRetrieveVehicle(item.id)">{{ item.date }} - {{ item.vehicle.slug_name }}</a>
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  props: ['id'],
  name: 'ListVehicleWorkdays',
  endpoint: process.env.BASE_URL,
  data() {
    return {
      vehicles: {
        items: [],
      },
    }
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
      goToRetrieveVehicle: function(id){
        console.log(id)
        this.$router.push({name:'RetrieveVehicleWorkdays', params: {id: id}});
      },
      getVehicles: function(){
          console.log(this.user)
          axios({
            method: 'get',
            url: `/api/vehicles-workday/?search=${this.user.user.username}`,
            timeout: 4000,    // 4 seconds timeout
          })
          .then(response => {
            let vehicles = response.data.results
            vehicles.forEach(element => {
              this.vehicles.items.push(element)
            })
          })
          .catch(error => console.error('timeout exceeded', console.log(error)))
      },

    },
    mounted() {
      console.log(this.user.user)
      this.getVehicles()
    },

  // created() {
  //   if (this.user.user.groups.includes('driver')){
  //     this.$router.push('/login-vehicle');
  //   }
  // }

}
</script>
