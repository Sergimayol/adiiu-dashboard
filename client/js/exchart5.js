function exchart5(data) {
    var chartData = data.map(function(item) {
        return { name: item[0], y: item[1] };
      });
    Highcharts.chart('artistSongs', {
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
          type: 'variablepie'
        },
        title: {
          text: 'Songs streamed from the artist selected',
          align: 'left'
        },
        subtitle: {
          text: "Top songs from the artist selected",
          align: "left",
        },
        tooltip: {
          headerFormat: '',
          pointFormat: '<span style="color:{point.color}">\u25CF</span> <b>{point.name}</b>: <b>{point.y}</b><br/>'
        },
        series: [{
          minPointSize: 80,
          innerSize: '40%',
          zMin: 0,
          name: 'Songs',
          borderRadius: 5,
          data: chartData,
        }]
      });
   
}