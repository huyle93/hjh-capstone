//
// //
// // // // For dashboard's charts
// //
//
// Data for Radar Chart
var dataRadar = {
    labels: ['Environmental', 'Civil', 'Family', 'Criminal', 'Supreme Court', 'Juvenile'],
    datasets: [
        {
        label: 'Paul S. Gillies',
        backgroundColor: 'rgba(243, 57, 57, 0.3)',
        borderColor: 'rgba(243, 57, 57, 1)',
        pointBackgroundColor: 'rgba(243, 57, 57, 1)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgba(243, 57, 57, 1)',
        data: [90, 59, 20, 31, 56, 40]
        },
        {
        label: 'Jon Hall',
        backgroundColor: 'rgba(153, 102, 255, 0.3)',
        borderColor: 'rgba(153, 102, 255, 1)',
        pointBackgroundColor: 'rgba(153, 102, 255, 1)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgba(153, 102, 255, 1)',
        data: [28, 38, 80, 59, 16, 27]
        }
    ]
};
var radarOptions = {
    animation: {animateRotate: true, animateScale: true},
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    },
    legend: {
        display: true
    }
};
// Data for Pie Chart Doughnut
var dataPie = {
    labels: [
		'Lose',
		'Win'
	],
	datasets: [{
		data: [17, 83],
		backgroundColor: [
		'#FF6384',
		'#36A2EB'
		],
		hoverBackgroundColor: [
		'#FF6384',
		'#36A2EB'
        ]
	}]
};
// Options for Pie Chart Doughnut
var pieOptions = {
    animation: {animateRotate: true, animateScale: true},
    responsive: true,
    maintainAspectRatio: false,
    legend: {
        display: true
    }
};

// Data and listener animation for Line Chart
var dataSales = {
  labels: ['9:00AM', '12:00AM', '3:00PM', '6:00PM', '9:00PM', '12:00PM', '3:00AM', '6:00AM'],
  series: [
     [287, 385, 490, 492, 554, 586, 698, 695]
    // [67, 152, 143, 240, 287, 335, 435, 437],
    // [23, 113, 67, 108, 190, 239, 307, 308]
  ]
};
var optionsSales = {
  low: 0,
  high: 800,
  showArea: true,
  height: "245px",
  axisX: {
    showGrid: false,
  },
  lineSmooth: true,
  showLine: true,
  showPoint: true,
  fullWidth: true,
  chartPadding: {
    right: 50
  }
};
var listener = {
    draw: function (data) {
        if (data.type === 'line' || data.type === 'area') {
            data.element.animate({
                d: {
                    begin: 2000 * data.index,
                    dur: 2000,
                    from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
                    to: data.path.clone().stringify(),
                    easing: [.17,.67,.83,.67]//Chartist.Svg.Easing.easeOutQuint
                }
            });
        }
    }
}
var responsiveSales = [
  ['screen and (max-width: 640px)', {
    axisX: {
      labelInterpolationFnc: function (value) {
        return value[0];
      }
    }
  }]
];
var legendSales = {
    names: ["Open","Click","Click Second Time"],
    types: ["info","danger","warning"]
};
// Data for Chartjs Bar Chart
const dataBar = {
    labels: [ 'William Fead',  'Hans Huessy', 'Jordan Gonda', 'James Dumont', 
     'Lisa Baker','Peter Gill','Carl McPhee','James Carroll', 'Jon Hall','Paul Gillies' ],
    datasets: [
      {
        label: 'Winning Chance against Judge Thomas Durkin',
        backgroundColor: ['rgba(255,99,132,0.3)',
        'rgba(54, 162, 235, 0.3)',
        'rgba(255, 206, 86, 0.3)',
        'rgba(75, 192, 192, 0.3)',
        'rgba(92, 238, 214, 0.3)',
        'rgba(255, 159, 64, 0.3)',
        'rgba(63, 242, 63, 0.3)',
        'rgba(223, 52, 223, 0.3)',
        'rgba(153, 102, 255, 0.3)',
        'rgba(243, 57, 57, 0.3)',
    
    ],
        
        borderColor: [ 'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(92, 238, 214, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(63, 242, 63, 1)',
        'rgba(223, 52, 223, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(243, 57, 57, 1)'],
        borderWidth: 1,
        
        hoverBackgroundColor: ['rgba(255,99,132,0.3)',
        'rgba(54, 162, 235, 0.3)',
        'rgba(255, 206, 86, 0.3)',
        'rgba(75, 192, 192, 0.3)',
        'rgba(92, 238, 214, 0.3)',
        'rgba(255, 159, 64, 0.3)',
        'rgba(63, 242, 63, 0.3)',
        'rgba(223, 52, 223, 0.3)',
        'rgba(153, 102, 255, 0.3)',
        'rgba(243, 57, 57, 0.3)',
    
    ],
        hoverBorderColor: [ 'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(92, 238, 214, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(63, 242, 63, 1)',
        'rgba(223, 52, 223, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(243, 57, 57, 1)'],
       
        data: [ 19, 37, 39, 42, 55, 56, 61, 70, 73, 92]
      }
    ]
};
  
const optionsBar = {
    maintainAspectRatio: false
};
  
const pluginsBar = [{
    afterDraw: (chartInstance, easing) => {
        const ctx = chartInstance.chart.ctx;
        ctx.fillText("This text drawn by a plugin", 100, 100);
    }
}];
// Data for Bar Chart
// Chartist JS
// var dataBar = {
//   labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
//   series: [
//     [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895],
//     [412, 243, 280, 580, 453, 353, 300, 364, 368, 410, 636, 695]
//   ]
// };
// var optionsBar = {
//     seriesBarDistance: 10,
//     axisX: {
//         showGrid: false
//     },
//     height: "245px"
// };
// var responsiveBar = [
//   ['screen and (max-width: 640px)', {
//     seriesBarDistance: 5,
//     axisX: {
//       labelInterpolationFnc: function (value) {
//         return value[0];
//       }
//     }
//   }]
// ];
var legendBar = {
    names: [],
    types: ["info","danger"]
};

module.exports = {
    dataRadar, radarOptions, dataPie, pieOptions, dataSales, optionsSales, listener, responsiveSales, legendSales, dataBar, optionsBar, pluginsBar, legendBar // For charts (Dashboard view)
};
