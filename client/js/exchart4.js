function exchart4(data) {
    Highcharts.chart("chart4", {
      accessibility: {
        screenReaderSection: {
          beforeChartFormat:
            "<h1>{chartTitle}</h5>" +
            "<div>{chartSubtitle}</div>" +
            "<div>{chartLongdesc}</div>" +
            "<div>{viewTableButton}</div>",
        },
      },
      chart: {
        type: 'bar',
      },
      title: {
        text: "Artists with most streamed song",
      },
      subtitle: {
        text: "The following chart shows the top ten artists with the most streamed songs",
        align: "left",
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
  