<template>
  <section>
    <h1>Expediente</h1>
    <hr/><br/>
    <div>
        <div v-for="item in expedientes.items" v-bind:key="item.id">
          <div>Fecha: {{ item.date }}</div>
          <div>Expediente: {{ item.identificador }}</div>
          <div>Cliente: {{ item.cliente }}</div>
          <div>Gestion: {{ item.gestion }}</div>
          <div>Material: {{ item.material }}</div>
          <div>Articulos: {{ articulos }}</div>
          <div>Precio: {{ item.precio }}</div>
        </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  props: ['expediente.id'],
  name: 'Expedientes',
  endpoint: process.env.BASE_URL,
  data() {
    return {
      expedientes: {
        items: [],
      },
    }
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
    title() {
      return (this.expedientes.items[0])
    },
    articulos(){
      var arts = []
      this.expedientes.items.forEach(element => {
        element.articulos.forEach(xelement => {
          arts.push(xelement.name)
        })
      })
      return arts.toString()
    },
  },
  methods: {
      getExpedientes: function(id){
          console.log(this.user)
          axios({
            method: 'get',
            url: `/api/expedientes/?search=${id}`,
            timeout: 4000,    // 4 seconds timeout
            headers: {
                  "Content-Type": "multipart/form-data",
                  "Authorization": `Token ${this.user.access_token}`
                  // 'Access-Control-Allow-Origin': '*'
              }
          })
          .then(response => {
            let expedientes = response.data.results
            expedientes.forEach(element => {
              this.expedientes.items.push(element)
            })
          })
          .catch(error => console.error('timeout exceeded', console.log(error)))
      },

    },
    mounted() {
      this.getExpedientes(this.$route.params.id)
    },

  // created() {
  //   if (this.user.user.groups.includes('driver')){
  //     this.$router.push('/login-vehicle');
  //   }
  // }

}
</script>
