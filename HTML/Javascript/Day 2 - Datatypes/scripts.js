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

//