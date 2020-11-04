function Makeup(type,use,size){
    this.type = type;
    this.size = size;
}

let Juviasplace = new Makeup("Foundation","fullcoverage","3 oz")

console.log(Array.isArray(Juviasplace));

let myArray = [1,2,3,4];

console.log(Array.isArray(myArray));

console.log(myArray.join(" "))