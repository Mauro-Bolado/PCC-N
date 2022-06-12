<template>
    <div class="militants_container">
        <div class="militants_contents">
            <h1>Militantes</h1>
            <ul class="militants_list">
                <li v-for="militant in militant_page" :key="militant.ci">

                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from "axios";
</script>