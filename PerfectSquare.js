// Write a program that determines the smallest number of perfect squares that sum up to N

// Here are a few examples:

// Given N = 4, return 1 (4)
// Given N = 17, return 2 (16 + 1)

const numOfPerfectSquares = (num, count) => {
    //edge case
    if(num === 0){
        return 0;
    };
    const checkSquare = isPerfectSquare(num);
    //checks if the num is already a perfect square
    if(checkSquare === true) {
        count++;
        return count;
    } else{
        var temp = num;
        //substract 1 from num until its a perfect square
        while(true){
            let findSquare = isPerfectSquare(temp-1);
            //check if the number is a perfect square
            if(findSquare === true){
                //substract the found number from num
                num -= temp-1;
                count++;
                //check the remaining number recursively
                return numOfPerfectSquares(num, count);
            }else{
                temp--;
                continue;
            }
        };
        return count;
    };
    return count;
};

const isPerfectSquare = (num) => {
    return num > 0 && Math.sqrt(num) % 1 === 0;
}

console.log(numOfPerfectSquares(4, 0)) // -> 1
console.log(numOfPerfectSquares(17, 0)) // -> 2
