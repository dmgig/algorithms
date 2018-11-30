const args = process.argv.slice(3)

const maximum = (args) => {
  args.sort((a, b) => b - a)
  const result = parseInt(args[0]) * parseInt(args[1])
  return result
}

console.log(maximum(args))
