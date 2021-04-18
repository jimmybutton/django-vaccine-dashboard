const COLORS = [
  "#1170aa",
  "#fc7d0b",
  "#a3acb9",
  "#57606c",
  "#5fa2ce",
  "#c85200",
  "#7b848f",
  "#a3cce9",
  "#ffbc79",
  "#c8d0d9",
];
const BGCOLORS = COLORS.map((c) =>
  Chart.helpers.color(c).alpha(0.5).rgbString()
);

function drawLineChart(canvas) {
  let url = canvas.dataset.url;
  let ctx = canvas.getContext("2d");

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      new Chart(ctx, {
        type: "line",
        data: {
          datasets: data.datasets.map((dataset, index) => {
            return {
              backgroundColor: BGCOLORS[index],
              borderColor: COLORS[index],
              fill: false,
              ...dataset,
            };
          }),
        },
        options: {
          scales: {
            x: {
              type: "time",
            },
          },
          plugins: {
            legend: {
              position: "bottom",
            },
          },
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
