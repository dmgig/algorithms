const fibonacci_last_digit = function(n) {
  const store = [0,1];
  for(i=1; i<n; i++){
    store.push((store[i-1] + store[i]) % 10)
  }
  return store[store.length - 1];
}

const fibonacci_stress_test = function() {

  console.log(fibonacci_last_digit(331))

  while(true) {
    let n = Math.ceil(Math.pow(10, 7) * Math.random())
    console.log(n)
    let start = Date.now();
    let result = fibonacci_last_digit(n)
    var resultTime = Date.now() - start;

    console.log(n, result, 'result time: '+resultTime)

  }
}

data = '';

process.stdin.on('readable', function() {
  var chunk;
  while (chunk = process.stdin.read()) {
    data += chunk;
  }
});

process.stdin.on('end', function () {

  let lines = data.split(/\r\n|\r|\n|\\n/)
  console.log(fibonacci_stress_test())

});
