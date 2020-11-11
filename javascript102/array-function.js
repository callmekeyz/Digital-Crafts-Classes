let letters = ["a","b","c","d"]
let letterPlus = letters.map(function(letter){
    return letter+letter
  })
  console.log(letters)
  console.log(letterPlus)

  let letterObj = letters.map(f(letter,idx)=>{
    return {
        name:letter,
        index:idx,
        letterIdx : letter+idx
    }
})
console.log(letterObj)

let random = letter.map(()=>3)
console.log(random)

let numbers = [6,1,3,4,3,5,5,10]
  //function has a conditional return
let increased = numbers.map(function((num, idx){
    if(num > numbers[idx-1]) return num;
  })
console.log(increased)

let family = [
    {
        name:"keyz",
        age:32
    },
    {
        name:"rick",
        age:34
    },
    {
        name:"jordan",
        age:12
    },
    {
        name:"lyric",
        age:6
    },
    {
        name:"denver",
        age:2
    }
]

//returns just names
let justNames = family.map(function(member){
    return member.name
})
let updated = family.map((member)=>{
    member.surName = "Fleetwood"
    return member
})
console.log(updated)
// accidently updating objects this can lead to bugs
console.log(family)
//better way ... create a new object
let updated = family.map((member)=>{
    let newMember = {}
    for(key in member){
        newMember[key] = member[key]
    }
    newMember.surName = 'Fleetwood'
    return newMember
})
console.log(updated)
console.log(family)//no change