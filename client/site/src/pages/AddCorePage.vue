<template>
  <div class="q-pa-md" style="max-width: 300px">
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="q-gutter-md"
    >
      <q-input
        ref="codeRef"
        filled
        v-model="code"
        label="Código: *"
        lazy-rules
        :rules="codeRules"
      />

      <q-input
        ref="nameRef"
        filled
        v-model="name"
        label="Nombre del Núcleo: *"
        lazy-rules
        :rules="nameRules"
      />

      <q-input
        ref="districtRef"
        filled
        type="number"
        v-model="district"
        label="Distrito: *"
        lazy-rules
        :rules="districtRules"
      />

      <q-input
        ref="areaRef"
        filled
        v-model="area"
        label="Area Política: *"
        lazy-rules
        :rules="districtRules"
      />

      <q-input
        ref="sectorRef"
        filled
        v-model="sector"
        label="Sector: *"
        lazy-rules
        :rules="areaRules"
      />

      <q-input
        ref="subordinateRef"
        filled
        v-model="subordinate"
        label="Subordinado a: *"
        lazy-rules
        :rules="subordinateRules"
      />

      <div>
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

    const age = ref(null);
    const ageRef = ref(null);

    const accept = ref(false);

    return {
      name,
      nameRef,
      nameRules: [(val) => (val && val.length > 0) || "Please type something"],

      age,
      ageRef,
      ageRules: [
        (val) => (val !== null && val !== "") || "Please type your age",
        (val) => (val > 0 && val < 100) || "Please type a real age",
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
