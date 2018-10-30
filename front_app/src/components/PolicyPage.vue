<template>
  <v-app>
    <v-content>
      <v-layout>
        <PolicyList/>
        <AddPolicy/>
      </v-layout>
    </v-content>
  </v-app>
</template>

<script>
import PolicyList from '@/components/PolicyList'
import AddPolicy from '@/components/AddPolicy'

export default {
  name: 'policies',
  components: {
    PolicyList,
    AddPolicy
  },
  data () {
    return {
      //
    }
  }
}
</script>

<style>

</style>
