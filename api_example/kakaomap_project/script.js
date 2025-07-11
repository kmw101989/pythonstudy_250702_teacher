const url =
  "https://apis.data.go.kr/B551011/GoCamping/basedList?numOfRows=4000&pageNo=1&MobileOS=ETC&MobileApp=camping&serviceKey=RGzR0pEvB08eGZWqjj0mYonhz1%2Bkj6rzw2MBbGWGY99AroOuOwtjHo8LOJESQ8Q6jyV9jhaIcfndl%2BG6pi4v0A%3D%3D&_type=json";

fetch(url)
  .then((response) => response.json())
  .then((result) => {
    const data = result.response.body.items.item;

    const showPosition = (position) => {
      const { latitude, longitude } = position.coords;

      const container = document.getElementById("map");
    };

    const errorPosition = (error) => {
      alert(error.message);
    };

    window.navigator.geolocation.getCurrentPosition(
      showPosition,
      errorPosition
    );
  });
