function exchart1(data) {
  Highcharts.chart("chart1", {
    accessibility: {
      screenReaderSection: {
        beforeChartFormat:
          "<h1>{chartTitle}</h5>" +
          "<div>{chartSubtitle}</div>" +
          "<div>{chartLongdesc}</div>" +
          "<div>{viewTableButton}</div>",
      },
    },
    series: [
      {
        type: "wordcloud",
        data,
        name: "Occurrences",
      },
    ],
    title: {
      text: "Wordcloud of the artists names",
      align: "left",
    },
    subtitle: {
      text: "Source: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023",
      align: "left",
    },
    tooltip: {
      headerFormat:
        '<span style="font-size: 16px"><b>{point.key}</b></span><br>',
    },
  });
}
