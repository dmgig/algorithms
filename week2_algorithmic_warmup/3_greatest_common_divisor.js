const greatest_common_divisor_fast = function(a,b) {
  let aa = Math.max(a, b)
  let bb = Math.min(a, b)
  let divisor = aa % bb
  if(bb === 0) return aa
  return greatest_common_divisor_fast(bb,divisor)
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
  let input = lines[0].split(' ')

  console.log(greatest_common_divisor_fast(input[0], input[1]))
});
