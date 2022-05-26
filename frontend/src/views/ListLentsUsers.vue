<template>
  <section>
    <h1>Prestamos</h1>
    <hr/><br/>
  <div class="overflow-auto">
    <b-table
      id="my-table"
      :items="items"
      :per-page="perPage"
      :fields="fields"
      @row-selected="onRowSelected"
      ref="selectableTable"
      selectable
      small
    >
    </b-table>
    <b-pagination
      v-model="currentPage"
      :per-page="perPage"
      :current-page="currentPage"
      :total-rows="total"
      @input= "updatePage(currentPage)"
      aria-controls="my-table"
    ></b-pagination>
  </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  props: ['id'],
  name: 'ListLentsUsers',
  endpoint: process.env.BASE_URL,
  data() {
    return {
      vehicles: {
        items: [],
      },
        total: '',
        next_page: '',
        previous_page: '',
        perPage: 10,
        currentPage: 1,
        fields:['fecha', 'cantidad', 'moneda', 'pagado', 'fecha_del_pago'],
        items: []
    }
  },
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
    goToRetrieveLents: function(id){
      this.$router.push({name:'RetrieveLentUser', params: {id: id}});
    },
    getItems: function(page=null){
      var url = `/api/lents/?search=${this.user.user.username}`
      if(page){
        url = `/api/lents/?page=${page}&search=${this.user.user.username}`
      }
        axios({
          method: 'get',
          url: url,
          timeout: 4000,    // 4 seconds timeout
          headers: {
                  "Content-Type": "multipart/form-data",
                  "Authorization": `Token ${this.user.access_token}`
                  // 'Access-Control-Allow-Origin': '*'
              }
        })
        .then(response => {
          this.next_page = response.data.next,
          this.previous_page = response.data.previous,
          this.total = response.data.count,
          this.items = response.data.results
        })
        .catch(error => console.error('timeout exceeded', console.log(error)))
    },
    updatePage(currentPage){
      var page = null
      if (currentPage > 0){
        page = currentPage
      }
      this.getItems(page)
    },
    onRowSelected(items) {
      this.goToRetrieveLents(items[0].id)
    },
  },
  mounted() {
    this.getItems()
  },
}
</script>
