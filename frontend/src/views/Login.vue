<template>
  <section>
    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="username" class="form-label">Username:</label>
        <input type="text" name="username" v-model="form.username" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password:</label>
        <input type="password" name="password" v-model="form.password" class="form-control" />
      </div>
      <b-button block type="submit" class="btn btn-primary" variant="primary">Ingresar</b-button>
    </form>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: '',
        password:'',
      }
    };
  },
  computed: {
    ...mapGetters({user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
      await this.logIn(User);
      if (this.user.vehicle_workday == null && this.user.user.groups.includes('driver')){
        this.$router.push('/login-vehicle');
      } else {
        this.$router.push('/profile').catch((e) => console.log(e));
      }
    }
  }
}
</script>
