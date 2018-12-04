const greatest_common_divisor_naive = function(a,b) {
  let greatest = 0;
  min = Math.min(a,b);
  for(i=0; i<min; i++){
    if(a % i === 0 && b % i === 0)
      greatest = i;
  }
  return greatest;
}

const greatest_common_divisor_fast = function(a,b) {
  let aa = Math.max(a, b)
  let bb = Math.min(a, b)
  let divisor = aa % bb
  if(bb === 0) return aa
  return greatest_common_divisor_fast(bb,divisor)
}

const greatest_common_divisor_stress_test = function(a, b) {

  while(true) {
    let aa = a || Math.ceil(Math.pow(10,9) * Math.random()) + 2
    let bb = b || Math.ceil(Math.pow(10,9) * Math.random()) + 2

    console.log(aa,bb)

    let start = Date.now();
    let naive = greatest_common_divisor_naive(aa, bb)
    var naiveTime = Date.now() - start;

    start = Date.now();
    let fast = greatest_common_divisor_fast(aa, bb)
    var fastTime = Date.now() - start
    console.log('result', naive, 'naive time: '+naiveTime, fast, 'fast time: '+fastTime)

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
    console.log(greatest_common_divisor_stress_test(input[0], input[1]));
  } else
    console.log(greatest_common_divisor_stress_test(false, false));

});
