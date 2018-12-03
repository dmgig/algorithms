data = '';

process.stdin.on('readable', function() {
  var chunk;
  while (chunk = process.stdin.read()) {
    data += chunk;
  }
});

process.stdin.on('end', function () {

  let lines = data.split(/\r\n|\r|\n|\\n/)

  const args = lines[0].split(' ')
  const a = parseInt(args[0]);
  const b = parseInt(args[1]);
  const result = a + b;
  console.log(result)

});
