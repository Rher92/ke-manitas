<template>
<div class="bg-dark">
<div class="container-md">
    <b-navbar toggleable="lg" type="dark" variant="info" class="bg-dark">
      <b-navbar-brand href="/">Inicio</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <ul v-if="isLoggedIn" class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/profile">Mi Perfil</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="logout">Cerrar sesión</a>
            </li>
            <li class="nav-item">
              <b-nav-item-dropdown text="Vehiculo" right type="dark">
                <!-- <b-dropdown-item href="#">Perfil</b-dropdown-item> -->
                <div v-if="VehicleLogin == null">
                  <b-dropdown-item href="/login-vehicle">Iniciar Sesion</b-dropdown-item>
                </div>
                <div v-else>
                  <b-dropdown-item href="/logout-vehicle">Cerrar Sesion</b-dropdown-item>
                </div>
                <div>
                  <b-dropdown-item href="/list-vehicle-workdays">Actividades</b-dropdown-item>
                </div>

              </b-nav-item-dropdown>
            </li> 
          </ul>
          <ul v-else class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/login">Iniciar sesión</router-link>
            </li>
          </ul>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    VehicleLogin: function() {
      return this.$store.getters.stateUser.vehicle_workday;
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    }
  },
}
</script>

<style scoped>
a {
  cursor: pointer;
}
</style>
