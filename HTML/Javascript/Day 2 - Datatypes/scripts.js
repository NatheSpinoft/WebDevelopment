// Strings
let string = "Javascript"
let firstLetter = string[0]
console.log(firstLetter)// J
let secondLetter = string[1]
let thirdLetter = string[2]
let lastLetter = string[9]
console.log(lastLetter)
let lastIndex = string.length - 1
console.log(lastIndex) // 9 
console.log(string[lastIndex]) //t

//
console.log("-----")

// CharAt()
let sample = string.charAt(0)
console.log(sample)
let sample2 = string.length - 1
console.log(sample2)

//
console.log("-----")

//Charcode()
let sample3 = string.charCodeAt(0)
console.log(sample3)

//
console.log("-----")

//concat()
let sample4 = "land"
console.log(sample4.concat("fin"))
console.log(sample4.concat(" island"," mountain"," swamp"))

//
console.log("-----")

//ends-wth
console.log(string.endsWith("script"))
console.log(string.endsWith("scrypt"))

//
console.log("-----")

//includes
console.log(string.includes("java"))
console.log(string.includes("script"))
console.log(string.includes("30"))

//
console.log("-----")

//indexof
console.log(string.indexOf("j"))
console.log(string.indexOf("i"))

//
console.log("-----")

//last_index_of
console.log(string.lastIndexOf("script"))

//
console.log("-----")

//length
console.log(string.length)
console.log("There is nothing".length)

//
console.log("-----")

//match
let stringy = 'There is only one person'
let pattern1 = /There/
console.log(stringy.match(pattern1))

//
console.log("-----")

//repeat
console.log("This could be a string or variable".repeat(3))

//
console.log("-----")

//replace
let frings = "I like Python"
console.log(frings)
console.log(frings.replace('Python', 'Javascript'))

//
console.log("-----")

//search
let frings1 = "There could be only one"
console.log(frings1)
console.log(frings1.search('one'))

//
console.log("-----")

//split
frings2 = "Apple, Banana, Mango, Pineapple, Strawberry"
console.log(frings2.split(','))

//
console.log("-----")

//starts_with
frings3 = "There was an old man from orange county"
console.log(frings3)
console.log(frings.startsWith("old"))

//
console.log("-----")

//substr
wings = "I like BBQ wings"
console.log(wings)
console.log(wings.substr(7, 3))

//
console.log("-----")

//to_lowercase
wings1= "SuperDuperLanguage"
console.log(wings.toLowerCase())

//
console.log("-----")

//to_UpperCase
wings2 = "I\'m just slow"
console.log(wings2.toUpperCase())

//
console.log("-----")

wings3 = "  There are   too    many  Spaces    "
console.log(wings3.trim(" "))

//
console.log("-----")

//typeof
console.log(typeof false)