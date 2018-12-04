const fibonacci_number_naive = function(n) {
  if(n <= 1)
    return n
  return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2);
}

const fibonacci_number_fast = function(n) {
  const store = [0,1];
  for(i=1; i<n; i++){
    store.push(store[i-1] + store[i])
  }
  return store[store.length - 1];
}

const fibonacci_stress_test = function() {
  while(true) {
    let n = Math.ceil(40 * Math.random())

    let start = Date.now();
    let naive = fibonacci_number_naive(n)
    var naiveTime = Date.now() - start;

    start = Date.now();
    let fast = fibonacci_number_fast(n)
    var fastTime = Date.now() - start;
    console.log(n, naive, 'naive time: '+naiveTime, fast, 'fast time: '+fastTime)

    if(naive !== fast){
      console.log('WRONG', naive, fast)
      return;
    }
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

  fibonacci_stress_test()

});
