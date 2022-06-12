<template>
    <div class="militant_container">
        <div class="militant_content">
            <h1>Militantes</h1>
            <ul class="militant_list">
                <li v-for="militant in militants" :key="militant.id">
                    <h3>{{ militant.militant_name }}</h3>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import "jquery/dist/jquery.min.js";
import "bootstrap/dist/css/bootstrap.min.css";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import axios from "axios";
import $ from "jquery";
export default {
  mounted() {
    axios.get("http://localhost:8000/pcc/militant/").then((response) => {
      this.militants = response.data;
      $("#datatable").DataTable();
    });
  },
  data: function () {
    return {
      militants: [],
    };
  },
};
</script>