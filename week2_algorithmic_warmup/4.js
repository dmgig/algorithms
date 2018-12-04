const least_common_multiple_naive = function(a,b) {
  for(i=1;i<=(a*b);i++){
    if(i % a == 0 && i % b == 0)
      return i
  }

  return a*b
}

const least_common_multiple_fast = function(a,b) {
  const gcd = greatest_common_divisor_fast(a,b);
  return a*b/gcd
}

const greatest_common_divisor_fast = function(a,b) {
  let aa = Math.max(a, b)
  let bb = Math.min(a, b)
  let divisor = aa % bb
  if(bb === 0) return aa
  return greatest_common_divisor_fast(bb,divisor)
}

const least_common_multiple_stress_test = function(a, b) {

  while(true) {
    let aa = a || Math.ceil(Math.pow(10,4) * Math.random()) + 2
    let bb = b || Math.ceil(Math.pow(10,4) * Math.random()) + 2

    console.log(aa,bb)

    let start = Date.now();
    let naive = least_common_multiple_naive(aa, bb)
    var naiveTime = Date.now() - start;
    console.log(aa, bb, 'result naive', naive, 'naive time: '+naiveTime)

    start = Date.now();
    let fast = least_common_multiple_fast(aa, bb)
    var fastTime = Date.now() - start
    console.log(aa, bb, 'result both', naive, 'naive time: '+naiveTime, fast, 'fast time: '+fastTime)

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

  input = lines[0].split(' ')
  if(input[0] > 2 && input[1] > 2){
    console.log(least_common_multiple_stress_test(input[0], input[1]));
  } else
    console.log(least_common_multiple_stress_test(false, false));

});
