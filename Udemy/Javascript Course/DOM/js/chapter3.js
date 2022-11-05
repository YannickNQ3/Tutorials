//CHAPTER 3: Built-in Constants
// Section 3.1: null

 console.log(null == undefined);
 console.log(null === undefined);

 console.log(typeof null);

 var a = null;

 console.log(a === null);
//  Testing for NaN using isNaN()
console.log("Testign for NaN");
console.log(isNaN(NaN));
console.log(isNaN(1));
console.log(isNaN(-2e-4));
console.log(isNaN(Infinity));
console.log(isNaN(true));
console.log(isNaN(false));
console.log(isNaN(null));
console.log(isNaN(""));
console.log(isNaN(" "));
console.log(isNaN("45.3"));
console.log(isNaN("1.2e3"));
console.log(isNaN("Infinity"));
console.log(isNaN(new Date));
console.log(isNaN("10$"));
console.log(isNaN("hello"));
console.log(isNaN(undefined));
console.log(isNaN());
console.log(isNaN(function(){}));
console.log(isNaN({}));
console.log(isNaN([1,2]));

// Section 3.3: NaN
console.log(typeof NaN);

//Section 3.4: undefined and null
//evalute undefined
let foo;
console.log('is undefined?', foo === undefined);
let fooo = {a: 'a'};
console.log('is undefined?', fooo.b === undefined);
function foooo(){return;}
console.log('is undefined?', foooo() === undefined);
function fooooo(param){
    console.log('is undefined?', param === undefined);
}
fooooo('a');
fooooo();

//Section 3.5: Infinity and -Infinity

console.log(Infinity > 123192310293); // true
console.log(-Infinity < -123192310293); // true
console.log(1 / 0); // Infinity
console.log(Math.pow(123123123, 9123192391023)); // Infinity
console.log(Number.MAX_VALUE * 2); // Infinity
console.log(23 / Infinity); // 0
console.log(-Infinity); // -Infinity
console.log(-Infinity === Number.NEGATIVE_INFINITY); // true
console.log(-0); // -0 , yes there is a negative 0 in the language
console.log(0 === -0); // true
console.log(1 / -0); // -Infinity
console.log(1 / 0 === 1 / -0); // false
console.log(Infinity + Infinity); // Infinity
var a = 0, b = -0;
console.log(a === b); // true
console.log(1 / a === 1 / b); // false

//Section 3.6:  Number Constans

console.log(Number.EPSILON);
console.log(Number.MAX_VALUE);
console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.MIN_VALUE);
console.log(Number.MIN_SAFE_INTEGER);
// Section 3.7: Operations that return NaN
// Mathematical operations on values other than  numbers returns NaN
// Section 3.8: Math library functions that return NaN
console.log(Math.floor("a"),
Math.sqrt(-1));


