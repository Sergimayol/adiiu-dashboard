function exchart4(data) {
    Highcharts.chart("chart4", {
      chart: {
        type: 'bar',
      },
      title: {
        text: "Artists with most streams song",
      },
      xAxis: {
        categories: data.map(item => item[0]),
        title: {
          text: "Artist",
        },
      },
      yAxis: {
        title: {
          text: "Number of streams",
        },
      },
      legend: {
        enabled: true,
      },
      series:[{
        name: 'Streaming Numbers',
        data: data.map(item => item[1]),
      }]
    });
  }
  