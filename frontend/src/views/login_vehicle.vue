<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group-2" label="Kilometraje:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.km"
          placeholder="ingrese kilometraje"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Vehiculos:" label-for="input-3">
        <b-form-select
          class="form-select"
          id="input-3"
          v-model="form.vehicle"
          :options="vehicles"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group id="input-group-3" label="Foto Kilometraje:" label-for="input-3">
        <b-form-file
          v-model="form.file"
          :state="Boolean(form.file)"
          placeholder="Eliga un archivo o arrastrelo aqui..."
          drop-placeholder="arroje el archivo..."
          required
        ></b-form-file>
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
  export default {
    name: 'LoginVehicle',
    data() {
      return {
        form: {
          fieldsBlured : false,
          valid : false,
          submitted : false,
          km: '',
          vehicle: null,
          file: null,
        },
        vehicles: [{ text: 'Seleccione uno', value: null }, 'mazda', 'chevrolet', 'ford', 'moto'],
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
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
    }
  }
</script>
