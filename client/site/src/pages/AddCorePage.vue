<template>
  <div class="q-pa-md">
    <img class="ico" src="../../public/from_site_logo.png" />
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="gutter-md"
    >
      <q-input
        ref="codeRef"
        filled
        v-model="code"
        type="number"
        label="Código:"
        lazy-rules
        :rules="codeRules"
      />

      <q-input
        ref="nameRef"
        filled
        v-model="name"
        label="Nombre del Núcleo:"
        lazy-rules
        :rules="nameRules"
      />

      <q-input
        ref="districtRef"
        filled
        type="number"
        v-model="district"
        label="Distrito:"
        lazy-rules
        :rules="districtRules"
      />

      <q-input
        ref="areaRef"
        filled
        v-model="area"
        label="Area Política:"
        lazy-rules
        :rules="districtRules"
      />

      <q-input
        ref="sectorRef"
        filled
        v-model="sector"
        label="Sector:"
        lazy-rules
        :rules="areaRules"
      />

      <q-input
        ref="subordinateRef"
        filled
        v-model="subordinate"
        label="Subordinado a:"
        lazy-rules
        :rules="subordinateRules"
      />

      <div class="btns">
        <q-btn label="Submit" type="submit" color="primary" />
        <q-btn
          label="Reset"
          type="reset"
          color="primary"
          flat
          class="q-ml-sm"
        />
      </div>
    </form>
  </div>
</template>

<script>
import { useQuasar } from "quasar";
import { ref } from "vue";

export default {
  setup() {
    const $q = useQuasar();

    const name = ref(null);
    const nameRef = ref(null);

    const code = ref(null);
    const codeRef = ref(null);

    const district = ref(null);
    const districtRef = ref(null);

    const area = ref(null);
    const areaRef = ref(null);

    const sector = ref(null);
    const sectorRef = ref(null);

    const subordinate = ref(null);
    const subordinateRef = ref(null);

    const accept = ref(false);

    return {
      code,
      codeRef,
      codeRules: [(val) => (val && val.length > 0) || "Please type something"],

      name,
      nameRef,
      nameRules: [(val) => (val && val.length > 0) || "Please type something"],

      district,
      districtRef,
      districtRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      area,
      areaRef,
      areaRules: [(val) => (val && val.length > 0) || "Please type something"],

      sector,
      sectorRef,
      sectorRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      subordinate,
      subordinateRef,
      subordinateRules: [
        (val) => (val && val.length > 0) || "Please type something",
      ],

      accept,

      onSubmit() {
        nameRef.value.validate();
        ageRef.value.validate();

        if (nameRef.value.hasError || ageRef.value.hasError) {
        } else if (accept.value !== true) {
          $q.notify({
            color: "negative",
            message: "You need to accept the license and terms first",
          });
        } else {
          $q.notify({
            icon: "done",
            color: "positive",
            message: "Submitted",
          });
        }
      },

      onReset() {
        name.value = null;
        age.value = null;

        nameRef.value.resetValidation();
        ageRef.value.resetValidation();
      },
    };
  },
};
</script>

<style>
.gutter-md {
  margin-left: 45%;
  margin-top: 1em;
}
.ico {
  margin-left: 660px;
}
.q-pa-md {
  max-height: 1000px;
  max-width: 1000px;
}

.q-input {
  margin-top: 10px;
}
.btns {
  margin-top: 5px;
}
</style>
