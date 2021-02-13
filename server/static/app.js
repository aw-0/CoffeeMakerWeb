const app = {
  data() {
    return {
      switchState: "fkdsjfakl;jfgklfhjasdklfjasd",
      switchResp: "f",
      switch: {'test': 'test'}
    }
  },
  methods: {
      toggle() {
          axios.get("http://192.168.128.173:5000/toggleSwitch")
          .then(response => {this.switchState = response.data.state});
          confetti({spread: 180, particleCount: 500});
      },
      print() {
        console.log(this.switchState);
      },
      syncState() {
        axios.get("http://192.168.128.173:5000/switchState")
        .then( response => {this.switchState = response.data.state;});
      }
  },
  mounted() {
        axios.get("http://192.168.128.173:5000/switchState")
        .then( response => {this.switchState = response.data.state;});
  },
}

Vue.createApp(app).mount('#app')