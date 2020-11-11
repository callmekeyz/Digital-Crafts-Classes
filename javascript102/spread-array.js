let array1 = [1,2,3]
let array2  = [...array1,4,5]
console.log(array2)

//spread anywhere
let array3 = [...array1, 100,200, ...array2]


//syntax
{...iteratableObject, key1:value1, key2:value2}

let me = {firstName:"Clint",lastName:"Fleetwood", email:"clint@digitalcrafts.com"}

let newPerson = {age:39, ...me}
console.log(newPerson)


//Math Functions
let number = [10,20,30]
console.log(Math.max(...numbers)) // spread the numbers as arguments
//updating objects (Very Important for React)
let family = [
  {
      name:"clint",
      age:38
  },
  {
      name:"Anna",
      age:37
  },
  {
      name:"Olivia",
      age:11
  },
  {
      name:"Alle",
      age:9
  },
  {
      name:"Mark",
      age:7
  }
]
const update = member=>({...member, surName:"Fleetwood"})
let updatedFamily = family.map(update)
//results
console.log(updatedFamily)
console.log(family)


 // in place alternative to be more functional style

  //remove via filter
  let updated = [...family.filter(p=>p.name != 'Mark')] 

  //update a single item from the list as filtered
  let oliviaMarried = {
      name:"Olivia",
      surname:"Musk",
      age:24
  }

  //cool but it's at the end
  let updated = [...family.filter(p=>p.name != 'Olivia'), oliviaMarried]
  
  //using sort to keep the same order
  let updated = [...family.filter(p=>p.name != 'Olivia'), oliviaMarried]
  .sort((a,b)=>b.age - a.age)
  /* The Above Pattern you will see again...Take Time to learn it*/