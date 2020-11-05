function madlid(name,subject){

console.log(`${name}'s favorite subject in school is ${subject}.`);
}
madlid('Keyz','gym')



function tipamount(bill,service){
    let tip:
    switch(service){
        case 'good':
            tip = .20;
            break;
        case 'fair':
            tip = .15;
            break;
        case 'bad':
            tip = .10;
            break;
        default:
            tip = .20;
    }
    return bill * tip;
}
    
tipamount(100, 'good');