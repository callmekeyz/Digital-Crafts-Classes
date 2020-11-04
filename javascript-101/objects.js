let aboutMe = {}
aboutMe.name = 'Clint F'
console.log(aboutMe)

//adding new key
aboutMe.gender = 'Male'
console.log(aboutMe)

//removeing a key
delete aboutMe.tall
console.log(aboutMe)

for(attrib in aboutMe){
    if(!aboutMe.hasOwnProperty(attrib)) continue;
    console.log(attrib)
    console.log(aboutMe[attrib])
}