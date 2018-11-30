
const slowMaximum = (args) => {
  let result = 0, oldresult = 0, ans
  for(i in args){
    for(j in args){
      if(i === j) continue
      result = Math.max(parseInt(args[i]) * parseInt(args[j]), result)
      if(result !== oldresult){
        oldresult = result
        ans = [args[i], args[j], '=', result]
        // console.log(ans)
      }
    }
  }
  return result
}

const fastMaximum_dg = (args) => { // dg
  args.sort((a, b) => b - a)
  const result = parseInt(args[0]) * parseInt(args[1])
  return result
}

const fastMaximum_2n = (args) => { // week 1 2.5 example 2n speed
  // console.log('input   ', args)
  let compCnt = 0
  let index = 0
  for(i = 1; i < args.length; i++){ // find index w/ highest value
    compCnt++
    if(args[i] > args[index]) {
      index = i
    }
  }
  args.push(args[index])
  args.splice(index, 1);

  // console.log('1st loop', args)
  index = 0
  for(i = 1; i < args.length - 1; i++){
    compCnt++
    if(args[i] > args[index]) {
      index = i
    }
  }

  args.splice(args.length - 1, 0, args[index])
  args.splice(index, 1);
  // console.log('2nd loop', args)
  console.log('n time', compCnt/args.length)
  const result = parseInt(args[args.length-1]) * parseInt(args[args.length-2])
  return result
}

// https://cs.stackexchange.com/questions/83022/find-largest-and-second-largest-elements-of-the-array
const fastMaximum_1pt5n = (args) => { // week 1 2.5 example 1.5n speed
  let compCnt = 0

  compCnt++
  if(args.length % 2 !== 0)
    args.push(0)

  let pairs = []
  for(i=0; i<args.length; i=i+2){
    compCnt++
    if(args[i] > args[i+1])
      pairs.push([args[i+1], args[i]])
    else
      pairs.push([args[i], args[i+1]])
  }

  let L = 0, indexL = 0, pairL
  for(i in pairs) {
    compCnt++
    if(pairs[i][1] > L){
      L = pairs[i][1]
      indexL = i
    }
  }
  pairL = pairs.splice(indexL,1)

  let S = 0, indexS = 0
  if(pairs.length){
    for(i in pairs) {
      compCnt++
      if(pairs[i][1] > S){
        S = pairs[i][1]
        indexS = i
      }
    }
  }

  compCnt++
  S = (S < pairL[0][0] ? pairL[0][0] : S)

  console.log('n time', compCnt/args.length)
  const result = parseInt(L) * parseInt(S)
  return result
}

const stressTest = (N, M) => {
  while(true) {
    let n = Math.max(2, Math.ceil(Math.random() * N)),
        testArgs = []
    while(n > 0){
      testArgs.push(Math.ceil(Math.random() * M));
      n--
    }
    // console.log(testArgs)
    let results = {
      '_slow': slowMaximum(testArgs),
      '_2n':   fastMaximum_2n(testArgs),
      '_1pt5': fastMaximum_1pt5n(testArgs),
      '_dg':   fastMaximum_dg(testArgs)
    }

    let success = false
    let check = false
    for(i in results){
      if(check === false)
        check = results[i]
      else{
        success = (results[i] === check);
        if(success){
          console.log('OK', results)
        }else {
          console.log('WRONG', results)
          return
        }
      }
    }
  }
}

args = process.argv.slice(2)
stressTest(args[0], args[1])
