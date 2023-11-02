function exchart2(data) {
  Highcharts.chart("chart2", {
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
      zoomType: "x",
    },
    title: {
      text: "Number of songs released per year",
      align: "left",
    },
    subtitle: {
      text:
        document.ontouchstart === undefined
          ? "Click and drag in the plot area to zoom in"
          : "Pinch the chart to zoom in",
      align: "left",
    },
    xAxis: {
      type: "date",
      title: {
        text: "Date",
      },
    },
    yAxis: {
      title: {
        text: "Number of songs",
      },
    },
    legend: {
      enabled: true,
    },
    plotOptions: {
      area: {
        fillColor: {
          linearGradient: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 1,
          },
          stops: [
            [0, Highcharts.getOptions().colors[0]],
            [
              1,
              Highcharts.color(Highcharts.getOptions().colors[0])
                .setOpacity(0)
                .get("rgba"),
            ],
          ],
        },
        marker: {
          radius: 2,
        },
        lineWidth: 1,
        states: {
          hover: {
            lineWidth: 1,
          },
        },
        threshold: null,
      },
    },
    series: [
      {
        name: "Number of songs released per year",
        data: data,
      },
    ],
  });
}
