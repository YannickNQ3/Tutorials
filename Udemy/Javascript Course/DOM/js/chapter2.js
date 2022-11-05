//CHAPTER 2: Javascript Variables
//Section 2.1: Defining a Variable

var myVariable = "This is a variable";

//Section 2.2: Using a Variable
var number1 = 5;
number1 = 3;
console.log(number1);
// alert(number1);

//To add, sustract, multiply, divide, etc.

number1 = number1 + 5;
number1 = number1 - 6;

var number2 = number1 * 10;
var number3 = number2 / number1;

console.log(number1,",", number2,",", number3);

//String
var myString = "I am a" + "string!"
console.log(myString);

//Section 2.3: Types of variables
var myInteger = 12; // 32 bit number from (-2,147,483,648 to 2,147,483,647) 
var myLong = 9310141419482; // 64 bit number from(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)

var myFloat = 5.5; // 32 bit floating-point number (decimal)
var myDouble = 9310141419482.22; // 64 bit floating point number

var myBoolean = true; 
var myBoolean2 = false;

var myNotANumber = NaN;
var Nan_Example = 0/0;

var notDefined;

// alert(aRandomVariable);

var myNull = null;

//Section 2.4: Arrays and Objects

var myArray = [];

var favoriteFruits = ["apple", "orange", "strawberry"];
var carsInParking = ["Toyota", "Ferrari", "Lexus"];
var employees = ["Billy", "Bob", "Joe"];
var primeNumbers = [2,3,5,7,11,13,17,19,23,29,31];

myArray = ["zero", "one", "two"];

console.log(myArray);

myArray = ["John Doe", "Billy"]
elementNumber = 1;

console.log(myArray[elementNumber]);

myObject = {};
john = {firstname: "John", lastname: "Doe", fullname: "John Doe"};
billy = {
    firstname: "Billy",
    lastname: undefined,
    fullname: "Billy"
}

console.log(john.fullname);
console.log(billy.fullname);
