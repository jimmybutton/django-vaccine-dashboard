const COLUMNS = [
  {
    name: "Country",
    id: "country",
  },
  {
    name: "Total vaccinations",
    id: "total_vaccinations",
  },
  {
    name: "People vaccinated",
    id: "people_vaccinated",
  },
  {
    name: "Daily vaccinations",
    id: "daily_vaccinations",
  },
  {
    name: "Total vaccinations per hundred",
    id: "total_vaccinations_per_hundred",
  },
  {
    name: "People vaccinated per hundred",
    id: "people_vaccinated_per_hundred",
  },
  {
    name: "People fully vaccinated per hundred",
    id: "people_fully_vaccinated_per_hundred",
  },
  {
    name: "Daily vaccinations per million",
    id: "daily_vaccinations_per_million",
  },
];

function renderGrid(wrapper) {
  let url = wrapper.dataset.url;
  new gridjs.Grid({
    columns: COLUMNS,
    pagination: true,
    sort: true,
    // search: true,
    // fixedHeader: true,
    // height: '400px',
    server: {
      url: url,
      then: (data) => {
        return data.data
      },
    },
  }).render(wrapper);
}
