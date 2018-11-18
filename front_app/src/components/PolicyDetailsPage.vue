<template>
  <v-app>
    <v-content>
      <v-layout>
        <v-flex class="justify-center" xs6 offset-xs2-right>
            <PolicyFields :id="id"></PolicyFields>
        </v-flex>
        <!--<v-flex column>-->
            <!--<AddField :id="id"></AddField>-->
        <!--</v-flex>-->
      </v-layout>
    </v-content>
  </v-app>
</template>

<script>
import PolicyFields from '@/components/PolicyFields'

export default {
    props: ['id'],
    name: 'risk_details',
    components: {
        PolicyFields
    },
    data () {
        return {
        }
    }
}
</script>

<style>

</style>
