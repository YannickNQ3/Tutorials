// Section 1.1: Using console.log()

console.log("Hello, world!");

// Logging variables

var foo = "bar"
console.log(foo)

var thisVar = 'first value';
var thatVar = 'second value';
console.log("thisVar:", thisVar, "and thatVar: ", thatVar);

// Placeholders
var greet = "Hello", who = "World";
console.log("%s, %s!", greet, who);

// Logging Objects
console.log({
    'Email': '',
    'Groups': {},
    'Id': 33,
    'IsHiddenInUI': false,
    'IsSiteAdmin': false,
    'LoginName': 'i:0#.w|virtualdomain\\user2',
    'PrincipalType': 1,
    'Title': 'user2'
});

// Logging HTML elements

console.log(document.body);

// Section 1.2: Using the DOM API

document.getElementById("paragraph").textContent = "Hello, World"

//Create a new HTML element programmatically

var element    = document.createElement('p');
element.textContent = "Hola, mundo";
document.body.appendChild(element); //add the newly created element to the DOM

//Section 1.3: Using window.alert()

var message = "This is a new message";
// window.alert(message);
// alert(message)
// alert('Pause!');
// console.log('Alert was dismissed');

//Section 1.4: Using window.prompt()
// var age = prompt("How old are you?");
// console.log(age);

//Section window.confirm()
// result = window.confirm(message);
// var deleteConfirm = window.confirm("Are you sure you want to delete this")
// if(deleteConfirm){
//     deleteItem(itemId)
// }

//Section 1.6: Using the DOM API (with graphical text: Canvas, SVG, or image file)
// Using canvas elements
//Build a canvas
var canvas = document.createElement('canvas');
canvas.width = 500;
canvas.height = 250;
//select a context
var ctx = canvas.getContext('2d');
// set properties

ctx.font = '30px Cursive';
ctx.fillText("Hello world", 50, 50);
//insert canvas into page

document.body.appendChild(canvas);

// using SVG
// create an svg element container with dimensitions
var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
svg.width = 500;
svg.height = 50;

// build a text element

var text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
text.setAttribute('x', '0');
text.setAttribute('y', '50');
text.style.fontFamily = 'Times New Roman';
text.style.fontSize = '50';

// add the text to display
text.textContent = "Hello World";

//add the text element to our svg
svg.appendChild(text);
document.body.appendChild(svg);

//Image File

var img = new Image();
img.src = 'https://i.ytimg.com/vi/zecueq-mo4M/maxresdefault.jpg';
document.body.appendChild(img);