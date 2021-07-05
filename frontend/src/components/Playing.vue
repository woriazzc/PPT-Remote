<template>
  <div id="Playing">
    <div class="container">
      <el-button class="play-btn el-icon-arrow-up" v-on:click="onClick(1)" circle></el-button>
      <br>
      <br>
      <el-button class="play-btn el-icon-video-play" v-on:click="onClick(0)" circle></el-button>
      <br>
      <br>
      <el-button class="play-btn el-icon-arrow-down" v-on:click="onClick(2)" circle></el-button>
      <br>
      <br>
      <el-button class="play-btn el-icon-switch-button" v-on:click="goEnd" circle></el-button>
      <br>
      <br>
      <el-button class="play-btn el-icon-refresh-left" v-on:click="goBack" circle></el-button>
      <br>
      <br>
    </div>
    <div class="text">
      {{ this.id }} / {{ this.tot }}
    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Playing',
  data() {
    return {
      id: 0,
      tot: 0,
    };
  },
  methods: {
    onClick(e) {
      axios.get('/api/changePage?mov=' + e).then((response) => {
        let d = response.data;
        this.id = d["id"];
        this.tot = d["tot"];
      });
    },
    goBack() {
      this.$router.go(-1);
    },
    goEnd(){
      axios.get('/api/end');
      this.$router.go(-1);
    }
  },
  mounted() {
    axios.get('/api/getPage').then((response) => {
      let d = response.data;
      this.id = d["id"];
      this.tot = d["tot"];
    });
  },
}
</script>

<style scoped>
.container {
  position: absolute;
  left: 50%;
  top: 15%;
}

.play-btn {
  font-size: 60px;
  color: #000000;
  transform: translate(-50%, -50%);
}

.text {
  position: absolute;
  bottom: 5%;
  left: 40%;
  font-size: 30px;
}
</style>