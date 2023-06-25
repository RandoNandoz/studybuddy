function generateList() {
  fetch("../../data/data.json")
    .then(response => response.json())
    .then(data => createList(data));
}

function createList(data) {
  const mainUL = document.createElement('ol');
  for (let i = 0; i < data.result.length; i++) {
    const taskLI = document.createElement('li');
    taskLI.innerHTML = data.result[i].name;

    const durationUL = document.createElement('ul');
    for (var key in data.result[i].duration) {
      const durationLI = document.createElement('li');
      durationLI.innerHTML = key + ': ' + data.result[i].duration[key];
      durationUL.appendChild(durationLI);
    }


    taskLI.appendChild(durationUL);
    mainUL.appendChild(taskLI);
  }

  document.body.appendChild(mainUL);
}