let content = document.createElement("div")
let bigList = document.createElement("ul")

const $ = function(selector){
    let r = document.querySelectorAll(selector)
    if(r.length < 2) return r[0];
    return r
}

console.log('items created')
console.log(content,bigList)
let main = document.querySelector("main")

console.log('added created items to document')
main.append(content,bigList)

console.log('added li items to list')
for(let i = 0; i < 6; i++){
    let l = document.createElement("li")
    l.append(`this is item`)
    bigList.append(l)
}






