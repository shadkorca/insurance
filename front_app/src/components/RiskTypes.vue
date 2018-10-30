<template>
  <v-container>
    <v-layout text-xs-center wrap >
      <v-flex class="justify-center" xs6 offset-xs2>
        <h2 class="headline font-weight-bold">Risk Types</h2>
        <v-flex class="xs8 offset-xs2">
          <v-card class="my-4"
                  v-for="(eco, i) in ecosystem"
                  :key="i">
              <v-layout row wrap>
                <v-flex>
                  <v-card>
                    <v-card-actions class="justify-center xs12">
                      <v-btn flat class="justify" @click="submitForm(eco.id)" style="width:70%;">{{ eco.name }}</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn fab dark small color="primary" style="width: 30px; height: 30px;"
                      @click="deleteRisk(eco.id)">
                          <v-icon dark>remove</v-icon>
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-flex>
              </v-layout>
          </v-card>
        </v-flex>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
      data: () => ({
      ecosystem: [
        {
            "id": 1,
            "name": "Cars"
        },
        {
            "id": 2,
            "name": "House"
        }
      ]
    }),
  methods: {
    submitForm (data) {

      console.log(data)

    },
    deleteRisk(type) {
      console.log(type)
    }
  }
  }
</script>

<style>

</style>
