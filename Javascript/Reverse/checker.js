var fs = require('fs');

module.exports.ReadBookFile = function() { return  fs.readFileSync('book.txt', 'utf8');}

module.exports.CheckText = function (txt){
    var text = fs.readFileSync('book.txt', 'utf8');
    var textLenght = text.length;
    var reversedText;
    for (var i = 0; i < textLenght; i++){
        reversedText += text[textLenght - (i + 1)];
    }
    if (txt != reversedText){
        console.log(txt);
        console.log("-------------------------------------------------------");
        console.log("INCORRECT");
        return;
    }
    console.log(txt);
    console.log("-------------------------------------------------------");
    console.log("CORRECT");
    return
}