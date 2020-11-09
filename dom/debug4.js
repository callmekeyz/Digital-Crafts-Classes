function nextFunc(random){
    console.log(
        `Hubba, 
        Hubba,
        Hubba,
    `)
    random()
}

const anotherFunc = function(){
    console.log('I am here.')
}

nextFunc(anotherFunc, 12)