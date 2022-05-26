<template>
  <section>
    <h1>Prestamo</h1>
    <hr/><br/>
    <div>
          <div>Fecha: {{ expense.date }}</div>
          <div>Vehiculo: {{ expense.vehicle }}</div>
          <div>tipo: {{ expense.type }}</div>
          <div>Valor: {{ expense.value }}</div>
          <div>Moneda:  {{ expense.moneda }}</div>
          <div>Descripcion: {{ expense.description }}</div>
          <div>pagado: {{ expense.pagado }}</div>
          <div>fecha del pago: {{ expense.fecha_del_pago }}</div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  props: ['vehicle.id'],
  name: 'RetrieveExpenseUser',
  endpoint: process.env.BASE_URL,
  data() {
    return {
      expense: null,
    }
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
      getExpense: function(id){
          console.log(this.user)
          axios({
            method: 'get',
            url: `/api/expenses/${id}/`,
            timeout: 4000,    // 4 seconds timeout
            headers: {
                  "Content-Type": "multipart/form-data",
                  "Authorization": `Token ${this.user.access_token}`
                  // 'Access-Control-Allow-Origin': '*'
              }
          })
          .then(response => {
             this.expense = response.data

          })
          .catch(error => console.error('timeout exceeded', console.log(error)))
      },

    },
    mounted() {
      this.getExpense(this.$route.params.id)
    },
}
</script>
