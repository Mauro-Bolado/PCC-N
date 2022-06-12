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
import axios from 'axios';
export default {
    data() {
        return {
            militants: ['']
        }
    },
    methods: {
        async getData() {
            try {
                const response = await axios.get('http://localhost:8000/pcc/militant/');
                this.militants = response.data; 
            } catch (error) {
                console.log(error);
            }
        },
    },
    created() {
        this.getData();
    }
}
</script>