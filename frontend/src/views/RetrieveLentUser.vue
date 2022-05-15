<template>
  <section>
    <h1>Prestamo</h1>
    <hr/><br/>
    <div>
          <div>Fecha: {{ lent.fecha }}</div>
          <div>Cantidad: {{ lent.cantidad }}</div>
          <div>Moneda: {{ lent.moneda }}</div>
          <div>Pagado: {{ lent.pagado }}</div>
          <div>Fecha del pago: {{ lent.fecha_del_pago }}</div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  props: ['vehicle.id'],
  name: 'RetrieveLentUser',
  endpoint: process.env.BASE_URL,
  data() {
    return {
      lent: null,
    }
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
      getLent: function(id){
          console.log(this.user)
          axios({
            method: 'get',
            url: `/api/lents/${id}/`,
            timeout: 4000,    // 4 seconds timeout
          })
          .then(response => {
             this.lent = response.data

          })
          .catch(error => console.error('timeout exceeded', console.log(error)))
      },

    },
    mounted() {
      this.getLent(this.$route.params.id)
    },
}
</script>
