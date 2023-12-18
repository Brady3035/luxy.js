console.log("started");
let width = window.innerWidth;
let height = window.innerHeight;
let color = d3.scaleOrdinal(d3.schemeTableau10);
let context = context2d(width, height);
let nodes = createData();


function createData() {
  var dropdownButton = document.getElementById("dropdownButton");
  console.log(dropdownButton.textContent)
  if (dropdownButton.textContent == "Dropdown") {
    const k = width / 200;
    const r = d3.randomUniform(k, k * 4);
    const n = 4;
    return Array.from({ length: 200 }, (_, i) => ({ r: r(), group: i && (i % n + 1) }));
  } else if (dropdownButton.textContent == "Charging a Phone") {
    const k = width / 200;
    const r = d3.randomUniform(k, k * 4);
    const n = 4;
    return Array.from({ length: 200 }, (_, i) => ({ r: r(), group: i && (i % n + 1) }));
  } else if (dropdownButton.textContent == "Charging a Computer") {
    // Add logic for the "Charging a Computer" option
  } else if (dropdownButton.textContent == "Microwave") {
    // Add logic for the "Microwave" option
  } else if (dropdownButton.textContent == "Lightbulb") {
    // Add logic for the "Lightbulb" option
  } else if (dropdownButton.textContent == "T.V.") {
    // Add logic for the "T.V." option
  }
}





  function context2d(width, height, dpi) {
  if (dpi == null) dpi = devicePixelRatio;
  var canvas = document.createElement("canvas");
  canvas.width = width * dpi;
  canvas.height = height * dpi;
  canvas.style.width = width + "px";
  var context = canvas.getContext("2d");
  context.scale(dpi, dpi);
  return context;
  }

  var simulation = d3.forceSimulation(nodes)
      .alphaTarget(0.3) // stay hot
      .velocityDecay(0.1) // low friction
      .force("x", d3.forceX().strength(0.01))
      .force("y", d3.forceY().strength(0.01))
      .force("collide", d3.forceCollide().radius(d => d.r + 1).iterations(3))
      .force("charge", d3.forceManyBody().strength((d, i) => i ? 0 : -width * 2 / 3))
      .on("tick", ticked);

  d3.select(context.canvas)
      .on("touchmove", event => event.preventDefault())
      .on("pointermove", pointermoved);

  

  function pointermoved(event) {
      const [x, y] = d3.pointer(event);
      nodes[0].fx = x - width / 2;
      nodes[0].fy = y - height / 2;
  }

  function ticked() {
      context.clearRect(0, 0, width, height);
      context.save();
      context.translate(width / 2, height / 2);
      for (let i = 1; i < nodes.length; ++i) {
      const d = nodes[i];
      context.beginPath();
      context.moveTo(d.x + d.r, d.y);
      context.arc(d.x, d.y, d.r, 0, 2 * Math.PI);
      context.fillStyle = color(d.group);
      context.fill();
      }
      context.restore();
  }
  graphballs.append(context.canvas)
  




// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
if (!event.target.matches('.dropbtn')) {
  var dropdowns = document.getElementsByClassName("dropdown-content");
  for (var i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (openDropdown.classList.contains('show')) {
      openDropdown.classList.remove('show');
    }
  }
}

}