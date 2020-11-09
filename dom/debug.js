let footer = document.querySelector("footer");//should find the footer elements

//2
let ideas = document.querySelectorall('.child-idea') 
for(let i = 0; i < ideas.length; i++){
    console.log(ideas(i)) // should console log each idea
}

//3
let ps = document.querySelectorAll("p")

ps.forEach(function(p){
    console.log(ps) // showes each p's attributes as an object
})