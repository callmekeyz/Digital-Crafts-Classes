const myArrowFunc = (foo, bar)=>{
    console.log(foo)
}
//called the same way
myArrowFunc('got some data for ya')

const myfunc = (foo)=>{
    console.log(foo)
}

const returnStuff = (arg)=>{
    return 'stuff'+arg
}
let result = returnStuff('My text')
console.log(result)


const doSomething = function(callback){
    console.log('I did something')
    callback()
}

let myArr = ['a','b','c','d']
  myArr.forEach((letter,idx)=>console.log(letter, idx))





