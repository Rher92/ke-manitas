<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group-2" label="Kilometraje:" label-for="input-2">
        <b-form-input
          type="number"
          id="input-2"
          v-model="form.km"
          placeholder="ingrese kilometraje"
          required
          v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.km)  && fieldsBlured}"
          v-on:blur="fieldsBlured = true"
        ></b-form-input>
        <div class="invalid-feedback">Matricula es requerida</div>
      </b-form-group>

      <b-form-group id="input-group-3" label="Vehiculos:" label-for="input-3">
        <b-form-select
          class="form-select"
          id="input-3"
          v-model="form.vehicle"
          :options="vehicles.items"
          required
          v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.vehicle)  && fieldsBlured}"
          v-on:blur="fieldsBlured = true"
        ></b-form-select>
        <div class="invalid-feedback">Seleccione un auto</div>
      </b-form-group>

      <b-form-group id="input-group-3" label="Foto Kilometraje:" label-for="input-3">
        <b-form-file
          v-model="form.file"
          placeholder="Eliga un archivo o arrastrelo aqui..."
          drop-placeholder="arroje el archivo..."
          required
          v-bind:class="{'form-control':true, 'is-invalid' : !validInputTexts(form.file)  && fieldsBlured}"
          v-on:blur="fieldsBlured = true"
        ></b-form-file>
         <div class="invalid-feedback">Seleccione una foto</div>
      </b-form-group>

      <div>
          <b-button type="reset" variant="danger">Resetear</b-button>
        <div style="float:right" class="">
          <b-button type="submit" variant="primary">Guardar</b-button>
        </div>
      </div>

    </b-form>
    <!-- <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card> -->
  </div>
</template>

<script>
import axios from 'axios';

  export default {
    // endpoint: process.env.VUE_APP_BASE_URL,
    endpoint: process.env.BASE_URL,
    name: 'LoginVehicle',
    data() {
      return {
        fieldsBlured : false,
        valid : false,
        submitted : false,
        form: {
          km: '',
          vehicle: '',
          file: null,
        },
        vehicles: {
          items: [],
        },
        show: true,
        states: {
          km: false,
          vehicle: false
        }
      }
    },
    methods: {
      validate : function(){
        this.emailBlured = true;
        if(this.km != '' && this.vehicle != ''){
            this.valid = true;
        }
      },
      validInputTexts : function(field) {
        console.log(field)
        if (field !== '' && field !== null && field !== undefined){
          console.log(field)
          let _return = false;
          if ((field.length > 0) || (field > 0) || (field.size > 0)){
            _return = true
          }
          return _return;
          }
      },
      onSubmit(event) {
        this.validate();
        if(this.valid){
          event.preventDefault()
          alert(JSON.stringify(this.form))
        }
      },

      getVehicles: function(){
          axios({
            method: 'get',
            url: '/api/vehicles',
            timeout: 4000,    // 4 seconds timeout
          })
          .then(response => {
            let vehicles = response.data.results
            vehicles.forEach(element => {
              var dict = { text: element.slug_name, value: element.id, disabled: !element.available }
              this.vehicles.items.push(dict)
            })
          console.log(this.vehicles.items)
          })
          .catch(error => console.error('timeout exceeded', console.log(error)))
      },

      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.km = ''
        this.form.vehicle = null
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    },
    mounted() {
      console.log('here')
      this.getVehicles()
    },
  }

  
</script>
