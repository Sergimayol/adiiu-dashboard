async function fetchAPI(url) {
  const response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const data = await response.json();
  return data;
}

function loadChartsData() {
  const urls = [
    "http://127.0.0.1:8000/songs/artist-occurences",
    "http://127.0.0.1:8000/songs/releaseday-numsongs",
    "http://127.0.0.1:8000/songs/mode-streams",
    "http://127.0.0.1:8000/songs/artist-moststreams",
    "http://127.0.0.1:8000/songs/songs-moststreams",
    "http://127.0.0.1:8000/songs/songs-weeknd",

  ];

  // Usar Promise.all() para manejar múltiples solicitudes en paralelo
  Promise.all(urls.map((url) => fetchAPI(url).then((data) => data.data)))
    .then(([data1, data2, data3,data4,data5,data6]) => {
      exchart1(data1);
      exchart2(data2);
      exchart3(data3);
      exchart4(data4);
      exchart5(data5);
      exchart6(data6);
    })
    .then(() => {
      console.log("All charts loaded successfully");
    })
    .catch((error) => {
      console.error("Error loading charts:", error);
    });
}

loadChartsData();
