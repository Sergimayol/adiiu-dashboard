function exchart5(data) {
    Highcharts.chart("chart5", {
        chart: {
            type: 'column',
        },
        title: {
            text: 'Most streamed songs'
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