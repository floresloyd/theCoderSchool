function addTwoNumbers(number1, number2){
    return number1 + number2
}



function subTwoNumbers(number1, number2){
    return number1 - number2
}


function printElement(array){
    for(let i = 0; i <= array.length ; i++){
        console.log(array[i])
    }
}

function revPrint(array){
    for(let i = array.length - 1; i >= 0; i--){
        console.log(array[i])
    }
}


// const arra = [1, 2, 3, 4]
// arra[0] == 1

function addElements(arr){
    let sum = 0
    for(let i = 0; i < arr.length; i++){
        // we walk over every value until we reach end   
        sum = sum + arr[i]    
        //console.log(arr[i]) 
    }
    return sum
}

function addElementz(arr){
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
        sum += arr[i];
        //console.log(arr[i]); // Optional: if you want to see each element
    }
    return sum;
}


// sum = sum + 1 
// sum += 1 



function countAnumberz(array, num_to_find){
    let counter = 0;
    for (let i = 0; i < array.length; i++){
        if (array[i] == num_to_find){
            counter += 1;
        }
    }
    return counter;
}

// % === divisible 
// n = 100
for(let i = 0; i <= 100; i++){

    if (i % 3 == 0 && i % 5 == 0){
        console.log("FizzBuzz")
    }

    // fizz if divisible 3
    else if(i % 3 == 0 ){
        console.log("Fizz")
    }


    // buzz if div by 5
    else if( i % 5 == 0){
        console.log("Buzz")
    }
    // fizzbuz if both 

}



function num(number){
    if(number % 3 == 0 && number % 5 == 0){
        console.log("FizzBuzz")
    }
}


num(15)