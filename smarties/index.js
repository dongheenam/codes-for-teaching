// draws a sample from N(mu, sigma^2)
function gaussian(mu, sigma) {
  let u = Math.random(), v = Math.random();
  let x = Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v ) * sigma + mu ;
  return Math.round(x);
}
  
// returns a random integer between [min, max]
function randInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}



// returns random Smartie <span>
function makeSmarty() {
  // name and legend of Smarties
  const sName = ['green', 'red', 'orange', 'blue', 'pink', 'yellow', 'purple', 'brown'];
  const sLeg = ['G', 'R', 'O', 'B', 'I', 'Y', 'U', 'N'];

  // choose a random index
  let i = randInt(0, sName.length-1);
  return `<span class='smarties smarties-${sName[i]} m-1'>${sLeg[i]}</span>`;
}

// creates a random number of random Smarties inside #container-smarties
function makeSmarties() {
  const d = document.getElementById("container-smarties");
  d.innerHTML = "";

  // number of Smarties
  let no = gaussian(12.5, 1);
  for (let i=0; i<no; i++) {
    d.innerHTML += makeSmarty();
  }
}