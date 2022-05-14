<template>
  <section>
    <h1>Vehiculos usado por día</h1>
    <hr/><br/>
    <div>
        <div v-for="item in vehicles.items" v-bind:key="item.id">
          <div>{{ item.vehicle.slug_name }}</div>
          <div>Fecha: {{ item.date }}</div>
          <div>Kilometraje de inicio: {{ item.km_init }}</div>
          <div>Kilometraje del final: {{ item.km_finish }}</div>
        </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  props: ['vehicle.id'],
  name: 'RetrieveVehicleWorkdays',
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
    title() {
      return (this.vehicles.items[0])
    }
  },
  methods: {
      getVehicles: function(id){
          console.log(this.user)
          axios({
            method: 'get',
            url: `/api/vehicles-workday/?search=${id}`,
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
      this.getVehicles(this.$route.params.id)
    },

  // created() {
  //   if (this.user.user.groups.includes('driver')){
  //     this.$router.push('/login-vehicle');
  //   }
  // }

}
</script>
