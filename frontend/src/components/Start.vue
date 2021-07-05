<template>
  <div id="Start">
    <div class="container" style="top: 40%">
      <el-button class="play-btn el-icon-video-play" v-on:click="onClick(0)" circle></el-button><nobr></nobr>
      <font class="text">
        从头开始
      </font>
    </div>
    <div class="container" style="top: 60%">
      <el-button class="play-btn el-icon-video-play" v-on:click="onClick(1)" circle></el-button>
      <font class="text">
        从当前开始
      </font>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Start",
  data() {
    return {
      id: 0,
      tot: 0,
    };
  },
  methods: {
    onClick(e) {
      axios.get('/api/play?mov=' + e).then((response) => {
        let d = response.data;
        this.id = d["id"];
        this.tot = d["tot"];
        this.$router.push({
          path: "/playing"
        })
      });
    }
  },
}
</script>

<style scoped>
.container {
  position: absolute;
  left: 40%;
}

.play-btn {
  font-size: 60px;
  color: #000000;
  transform: translate(-50%, -50%);
  float:left;
}

.text {
  font-size: 20px;
}
</style>