<template>
  <div>
    <!-- <b-form @submit.prevent="onSubmit" @reset="onReset" v-if="show"> -->
    <b-form @submit.prevent="onSubmit"  v-if="show">

      <b-form-group id="input-group-2" label="Expediente:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.expediente"
          placeholder="ingrese ID/Expendiente"
          required
          v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.expediente) && fieldsBlured}"
          v-on:blur="fieldsBlured = true"
        ></b-form-input>
        <div class="invalid-feedback">El Expediente es requerido</div>
      </b-form-group>

      <b-form-group id="input-group-3" label="Tipo de conexión:" label-for="input-3">
        <b-form-select
          class="form-select"
          id="input-3"
          v-model="form.tipo_conexion"
          :options="tipo_conexion.items"
          required
          v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.tipo_conexion) && fieldsBlured}"
          v-on:blur="fieldsBlured = true"
        ></b-form-select>
        <div class="invalid-feedback">Seleccione un tipo de conexión</div>
      </b-form-group>

      <b-form-group id="input-group-3" label="Foto Servicio:" label-for="input-3">
        <div class="container">
          <div class="large-12 medium-12 small-12 cell">
              <input required type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
          </div>
        </div>
      </b-form-group>

      <div>
          <b-button type="reset" variant="danger">Resetear</b-button>
        <div style="float:right" class="">
          <b-button type="submit" variant="primary">Guardar</b-button>
        </div>
      </div>

    </b-form>
  </div>

</template>

<script>

import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';

  export default {
    endpoint: process.env.BASE_URL,
    name: 'createExpedientes',
    data() {
      return {
        fieldsBlured : false,
        validated: 0,
        disabledForm: true,
        valid : false,
        submitted : false,
        form: {
          expediente: '',
          tipo_conexion: '',
        },
        materiales: {
          items: [],
        },
        tipo_conexion: {
          items: [],
        },
        articulos: {
          items: [],
        },
        show: true,
        files: null,
      }
    },
    methods: {
      ...mapActions(['VehicleWorkdayToUser']),
      handleFileUpload(){
        this.files = this.$refs.file.files[0];
      },
      validate : function(){
        // var vehicle_selected = null
        // let _return = false;
        // this.vehicles.items.forEach(element => {
        //   if(element.value == this.form.vehicle){
        //     vehicle_selected = element
        //   }
        // })
        // if ((vehicle_selected.km_tolerance_up) > parseInt(this.form.km)  &&  parseInt(this.form.km) > (vehicle_selected.km_tolerance_down)){
        //     _return = true;
        // }
        // return _return
      },

      validInputTexts : function(field) {
        if (field !== '' && field !== null && field !== undefined){
          let _return = false;
          if ((field.length > 0) || (field > 0) || (field.size > 0)){
            _return = true
          }
          return _return;
          }
      },
      // validInputKm : function(field) {
      //   var vehicle_selected = null
      //   this.vehicles.items.forEach(element => {
      //     if(element.value == this.form.vehicle){
      //       vehicle_selected = element
      //     }
      //   })
      //   let _return = false;
      //   if ((vehicle_selected.km_tolerance_up) > parseInt(field)  &&  parseInt(field)> (vehicle_selected.km_tolerance_down)){
      //       _return = true;
      //   }
      //   return _return
      // },
      onSubmit() {
        this.valid = this.validate();
        if(this.valid){
          event.preventDefault()
          this.saveFile()
        }
      },

      async saveFile(){
        const FormData = require('form-data');
        const form = new FormData();

        form.append('km', this.form.km);
        form.append('vehicle',  this.form);
        form.append('file', this.files);

        axios.post('api/vehicles-workday/', form, {
              headers: {
                  "Content-Type": "multipart/form-data",
                  "Authorization": `Token ${this.user.access_token}`
                  // 'Access-Control-Allow-Origin': '*'
              }
            })
          .then(response => {
            this.VehicleWorkdayToUser(response.data)
            this.$router.push('/profile').catch((e) => console.log(e));
          })
          .catch(function (error) {
            console.log(error);
          });
      },

      getInfoToFields: function(){
          axios({
            method: 'get',
            url: '/api/data-for-services',
            timeout: 4000,    // 4 seconds timeout
            headers: {
                  "Authorization": `Token ${this.user.access_token}`
              }
          })
          .then(response => {
            let info = response.data              
            
            info.materiales.forEach(element => {
              var dict = {
                text: element.name,
                value: element.id,
              }
              this.materiales.items.push(dict)
            })
            
            info.articulos.forEach(element => {
              var dict = {
                text: element.name,
                value: element.id,
              }
              this.articulos.items.push(dict)
            })
            
            info.tipo_conexion.forEach(element => {
              var dict = {
                text: element.name,
                value: element.id,
              }
              this.tipo_conexion.items.push(dict)
            })
          })
          .catch(error => console.error('timeout exceeded', console.log(error)))
      },

    },
    mounted() {
      this.getInfoToFields()
    },

  computed: {
    ...mapGetters({user: 'stateUser'}),
    },
  }

</script>
