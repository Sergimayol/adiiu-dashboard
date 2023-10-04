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
  ];

  // Usar Promise.all() para manejar múltiples solicitudes en paralelo
  Promise.all(urls.map((url) => fetchAPI(url).then((data) => data.data)))
    .then(([data1, data2, data3]) => {
      exchart1(data1);
      exchart2(data2);
      exchart3(data3);
    })
    .then(() => {
      console.log("All charts loaded successfully");
    })
    .catch((error) => {
      console.error("Error loading charts:", error);
    });
}

loadChartsData();
