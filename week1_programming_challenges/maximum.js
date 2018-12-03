const args = process.argv.slice(3)




data = '';

process.stdin.on('readable', function() {
  var chunk;
  while (chunk = process.stdin.read()) {
    data += chunk;
  }
});

process.stdin.on('end', function () {

  let lines = data.split(/\r\n|\r|\n|\\n/)

  let args = lines[1].split(' ')
  const maximum = (args) => {
    args.sort((a, b) => b - a)
    const result = parseInt(args[0]) * parseInt(args[1])
    return result
  }

  console.log(maximum(args))

});
