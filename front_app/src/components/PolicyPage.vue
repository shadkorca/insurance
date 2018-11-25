<template>
  <v-app>
    <v-content>
      <v-layout>
        <v-flex column>
          <PolicyList/>
        </v-flex>
        <v-flex column>
          <AddPolicy/>
        </v-flex>
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
    }
  }
}
</script>

<style>

</style>
