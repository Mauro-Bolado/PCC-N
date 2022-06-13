<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <q-table
        class="my-sticky-header-column-table"
        title="Atrasos"
        :rows="posts"
        :columns="columns"
        row-key="name"
      />
    </div>
    <h5>{{ posts.debts }}</h5>
  </q-page>
</template>
<script>
import { defineComponent } from "vue";
import axios from "src/boot/axios";

export default defineComponent({
  name: "DebtsPage",
  data() {
    return {
      columns: [
        {
          name: "ci",
          label: "No. Identidad",
          align: "left",
          field: "ci",
          sortable: true,
        },
        {
          name: "militant_name",
          align: "center",
          label: "Nombre",
          field: "militant_name",
          sortable: true,
        },
        {
          name: "first_lastname",
          align: "center",
          label: "Primer Apellido",
          field: "first_lastname",
          sortable: true,
        },
        {
          name: "second_lastname",
          align: "center",
          label: "Segundo Apellido",
          field: "second_lastname",
          sortable: true,
        },
        {
          name: "debts",
          align: "center",
          label: "Atrasos",
          field: "debts",
          sortable: true,
        },
      ],

      posts: [],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      this.$axios
        .get("http://localhost:8000/pcc/debts/")
        .then((res) => {
          this.posts = res.data;
          this.posts = this.giveFormat(this.posts);
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    giveFormat(post) {
      let result = "";
      for (let mil = 0; mil < post.length; mil++) {
        let debts = post[mil]["debts"];
        result =
          "Fecha más antigua: mes: " +
          debts[0]["month"] +
          " año: " +
          debts[0]["year"] +
          " ";
        let not_declared = "";
        let sum = 0;
        for (let index = 0; index < debts.length; index++) {
          if (debts["amount"] == null)
            not_declared = ". Hay fechas sin salario declarado.";
          else sum += debts["amount"];
        }
        result += ". Total: " + sum;
        result += not_declared;
        post[mil].debts = result;
      }
      return post;
    },
  },
  created() {
    this.getData();
  },
});
</script>

<style lang="sass">
.my-sticky-header-column-table
  /* height or max-height is important */
  height: 310px

  /* specifying max-width so the example can
    highlight the sticky column on any browser window */
  max-width: 600px

  td:first-child
    /* bg color is important for td; just specify one */
    background-color: #c1f4cd !important

  tr th
    position: sticky
    /* higher than z-index for td below */
    z-index: 2
    /* bg color is important; just specify one */
    background: #fff

  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
    /* highest z-index */
    z-index: 3
  thead tr:first-child th
    top: 0
    z-index: 1
  tr:first-child th:first-child
    /* highest z-index */
    z-index: 3

  td:first-child
    z-index: 1

  td:first-child, th:first-child
    position: sticky
    left: 0
</style>
