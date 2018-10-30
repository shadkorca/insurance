<template>
    <v-app>
        <v-content>
          <v-layout>
            <HelloWorld/>
          </v-layout>
        </v-content>
    </v-app>
</template>

<script>

import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: "home",
    components: {
        HelloWorld
    }
}
</script>

<style scoped>

</style>