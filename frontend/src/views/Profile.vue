<template>
  <section>
    <h1>Perfil</h1>
    <hr/><br/>
    <div>
      <p><strong>Usuario:</strong> <span>{{ user.user.username }}</span></p>
      <p><strong>Email:</strong> <span>{{ user.user.email }}</span></p>

      <div v-if="user.vehicle_workday != null">
        <p><strong>Vehiculo Asignado:</strong> <span>{{ user.vehicle_workday.vehicle.slug_name }}</span></p>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Profile',
  computed: {
    ...mapGetters({user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['deleteUser']),
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    }
  },

  // created() {
  //   if (this.user.user.groups.includes('driver')){
  //     this.$router.push('/login-vehicle');
  //   }
  // }

}
</script>
