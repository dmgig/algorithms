const fibonacci_number_fast = function(n) {
  const store = [0,1];
  for(i=1; i<n; i++){
    store.push(store[i-1] + store[i])
  }
  return store[store.length - 1];
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

  console.log(fibonacci_number_fast(lines[0]))

});
