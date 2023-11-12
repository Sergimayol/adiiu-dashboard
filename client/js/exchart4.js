function exchart4(data) {
    Highcharts.chart("topSongs", {
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
            type: 'column',
        },
        title: {
            text: 'Most streamed songs'
        },
        subtitle: {
          text: "The top songs with the number of streams of each one",
          align: "left",
        },
        plotOptions: {
            column: {
              depth: 25
            }
          },
          xAxis: {
            categories: data.map(item => item[0]),
            title: {
              text: "Songs",
            },
          },
          series: [{
            data:  data.map(item => item[1]),
            colorByPoint: true,
          }]
    });
}