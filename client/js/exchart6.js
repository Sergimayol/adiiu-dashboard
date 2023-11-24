function exchart6(data) {
  Highcharts.chart("modevsstreams", {
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
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      type: "pie",
    },
    title: {
      text: "Songs Mode vs Streams",
      align: "center",
    },
    subtitle: {
      text: "The following pie chart shows the percentage of streams of each song mode",
      align: "left",
    },
    tooltip: {
      pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>",
    },
    accessibility: {
      point: {
        valueSuffix: "%",
      },
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: "pointer",
        dataLabels: {
          enabled: true,
          format: "<b>{point.name}</b>: {point.percentage:.1f} %",
        },
      },
    },
    series: [
      {
        name: "Brands",
        colorByPoint: true,
        data: data,
      },
    ],
  });
}
