<template>
  <div>
    <!-- <b-form @submit.prevent="onSubmit" @reset="onReset" v-if="show"> -->
    <b-form @submit.prevent="onSubmit"  v-if="show">
      <b-form-group id="input-group-2" label="Vehiculo:" label-for="input-2">
        <div class="">
          <span class="input-group-text" >{{this.user.vehicle_workday.vehicle.slug_name}}</span>
      </div>
      </b-form-group>

      <b-form-group id="input-group-2" label="Kilometraje:" label-for="input-2">
        <b-form-input
          type="number"
          id="input-2"
          v-model="form.km"
          placeholder="ingrese kilometraje"
          required
          v-bind:class="{'form-control':true, 'is-invalid' : ((!validInputTexts(form.km)) || (!validInputKm(form.km))) && fieldsBlured}"
          v-on:blur="fieldsBlured = true"
        ></b-form-input>
        <div class="invalid-feedback">Kilometraje es requerido ó No coincide con el KM de inicio</div>
      </b-form-group>
      <p v-if="form.km > 0 ">Kilometraje formateado: {{this.km_formatted}}</p>

      <b-form-group id="input-group-3" label="Foto Kilometraje:" label-for="input-3">
        <div class="">
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
    name: 'LogoutVehicle',
    data() {
      return {
        fieldsBlured : false,
        valid : false,
        submitted : false,
        form: {
          km: '',
        },
        show: true,
        states: {
          km: false,
        },
        files: null,
      }
    },
    methods: {
      ...mapActions(['VehicleWorkdayToUser']),
      handleFileUpload(){
        this.files = this.$refs.file.files[0];
      },
      validate : function(){
        this.emailBlured = true;
        if(this.form.km != ''){
          if (parseInt(this.form.km) >= (this.user.vehicle_workday.km_init)){
            this.valid = true;
          }
        }
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
      validInputKm : function(field) {
        let _return = false;
        if (parseInt(field) >= (this.user.vehicle_workday.km_init)){
            _return = true;
        }
        return _return
      },
      onSubmit() {
        this.validate();
        if(this.valid){
          event.preventDefault()
          this.logOutVehicles()
        }
      },

      async logOutVehicles(){
        const FormData = require('form-data');
        const form = new FormData();

        form.append('km', this.form.km);
        form.append('vehicle', this.user.vehicle_workday.vehicle.id);
        form.append('file', this.files);

        axios.put(`api/vehicles-workday/${this.user.vehicle_workday.vehicle.plate}/`, form, {
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
    },
  computed: {
    ...mapGetters({user: 'stateUser'}),
    km_formatted() {
      return Number(this.form.km).toLocaleString()
    },
  },
  }
</script>
