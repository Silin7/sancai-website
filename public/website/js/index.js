new Vue({
  el: '#app',
  data: {
    loginVisible: false,
    firstName: '',
    lastName: '',
    headSearchValue: '',
  },
  mounted() {
    window.addEventListener("scroll", function () {
      const scrollY = window.pageYOffset;
      console.log('scrollY -------->', scrollY)
      if (scrollY > 900) {
        document.getElementById("newProducts").classList.add("animate__animated", "animate__flipInX");
      }
      if (scrollY > 1200) {
        document.getElementById("applications").classList.add("animate__animated", "animate__backInLeft");
      }
    });
  },
  methods: {
    // header search click
    headSearchClick() {
      console.log('this.headSearchValue -------->', this.headSearchValue)
    },
    // inquier item delete
    inquierItemDelete() {
      alert('Inquier Clicked');
    }
  }
});