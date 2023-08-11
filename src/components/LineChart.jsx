// components/LineChart.js
import React, { useEffect } from "react";
import { Line } from "react-chartjs-2";
import { useState } from "react";
import { Data } from "../data/Data";


function LineChart({}) {

  const [chartData, setChartData] = useState({
    labels: Data.map((data) => data.year),
    datasets:[
      {
        label: "Water Temperature ",
        data: Data.map((data) => data.userGain),
        backgroundColor: [
          "rgba(75,192,192,1)",
          "&quot;#ecf0f1",
          "#50AF95",
          "#f3ba2f",
          "#2a71d0"
        ],
        borderColor: "black",
        borderWidth: 2,
      }
    ]
    
  });

  return(
    <Line
        data={chartData}
         options={{   
           maintainAspectRatio: false, 
            responsive: true,
            plugins: {
                 title: {
                 display: true,
                 text: "Water Sensor"
                 },
                legend: {
                 display: true
                 }
             },
            layout: {
               padding: {
                 top:10,
                 left:20,
                 right: 20,
                 //bottom: 10
               }
             }
         }}
       />


  );

}
export default LineChart;

// function LineChart({data, sensorType}) {
//   const [chartData, setChartData] = useState([]);
//   const chartLabels = ["MON", "SUN"]

//   useEffect(() => {
//     // (1) when component is created or updated
//     let filteredDaset = data.map(d => {
//       if (sensorType == "") {
//         // waterType data
//       } else {
//         if(d.sensorType === sensorType) {
//           let newData = {
//             ...d,
//             backgroundColor: [
//               "rgba(75,192,192,1)",
//               "&quot;#ecf0f1",
//               "#50AF95",
//               "#f3ba2f",
//               "#2a71d0"
//             ],
//             borderColor: "black",
//             borderWidth: 2,
//             legend: {} 
//           }
//           return newData
//         }
//       }
//     })

//     setChartData(filteredDaset)
//   }, [
//     // if value inside this array updates, call （1）
//     sensorType
//   ])
  

//   return (
    
//       <Line
//         data={chartData}
//         options={{   
//           maintainAspectRatio: false, 
//             responsive: true,
//             plugins: {
//                 title: {
//                 display: true,
//                 text: "Water Sensor"
//                 },
//                 legend: {
//                 display: false
//                 }
//             },
//             layout: {
//               padding: {
//                 left:20,
//                 right: 20,
//                 bottom: 50
//               }
//             }
//         }}
//       />

//   );
// }
