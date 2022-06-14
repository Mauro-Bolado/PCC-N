<template>
  <div class="q-pa-md" style="max-width: 300px">
    <form
      @submit.prevent.stop="onSubmit"
      @reset.prevent.stop="onReset"
      class="q-gutter-md"
    >
      <q-input
        ref="nameRef"
        filled
        v-model="name"
        label="Nombre *"
        hint="Nombre de Usuario"
        lazy-rules
        :rules="nameRules"
      />

      <q-input
        ref="passwordRef"
        filled
        type="password"
        v-model="password"
        label="Your password *"
        lazy-rules
        :rules="passwordRules"
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

    const password = ref(null);
    const passwordRef = ref(null);

    return {
      name,
      nameRef,
      nameRules: [(val) => (val && val.length > 0) || "Please type something"],

      password,
      passwordRef,
      passwordRules: [
        (val) => (val !== null && val !== "") || "Please type your password",
        (val) => (val > 0 && val < 100) || "Please type a real password",
      ],

      onSubmit() {
        nameRef.value.validate();
        passwordRef.value.validate();

        if (nameRef.value.hasError || passwordRef.value.hasError) {
          // form has error
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
        password.value = null;

        nameRef.value.resetValidation();
        passwordRef.value.resetValidation();
      },
    };
  },
};
</script>
