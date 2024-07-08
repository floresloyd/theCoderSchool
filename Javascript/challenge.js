function addTwoNumbers(num1, num2) {
    return num1 + num2;
}

function subtractTwoNumbers(num1, num2) {
    return num1 - num2;
}

function addOneToEachElement(array) {
    return array.map(element => element + 1);
}

function addArrays(array1, array2) {
    return array1.map((element, i) => element + array2[i]);
}

function printReverse(array) {
    for (let i = array.length - 1; i >= 0; i--) {
        console.log(array[i]);
    }
}

// .reduce(accumulator, element_of_arr) => operation to accumulator 
function sumArray(array) {
    return array.reduce((sum, number) => sum + number, 0);
}

function countLetter(string, letter) {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        if (string[i] === letter) {
            count++;
        }
    }
    return count;
}

function arrayToString(array) {
    string = array.reduce((stringify, num) => stringify += num)
    return string

} 

const arr = [1, 2, 3, 4]
const arr2 = [1, 2, 3, 4]
const letterarr = ['a', 'b', 'c']

console.log(addArrays(arr, arr2))
console.log(arrayToString(letterarr))