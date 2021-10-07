function gaussian(mu, sigma) {
  // draws a sample from N(mu, sigma^2)
  let u = Math.random(), v = Math.random();
  let x = Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v ) * sigma/2 + mu ;
  return Math.round(x);
}
  
function randInt(min, max) {
  // returns a random integer between [min, max]
  return Math.floor(Math.random() * (max - min + 1) + min);
}

// name and legend of Smarties
const sName = ['green', 'red', 'orange', 'blue', 'pink', 'yellow', 'purple', 'brown'];
const sLeg = ['G', 'R', 'O', 'B', 'I', 'Y', 'U', 'N'];

function makeSmarty(index) {
  // returns a <span> that draws Smarty of the specified kind (as index)
  return `<span class='smarties smarties-${sName[index]} m-1'>${sLeg[index]}</span>`;
}

function makeSmarties() {
  // creates a random number of random Smarties inside #container-smarties
  const d = document.getElementById("container-smarties");
  d.innerHTML = "";
  let no = gaussian(12.5, 2);
  for (let i=0; i<no; i++) {
    d.innerHTML += makeSmarty(randInt(0,7));
  }
}