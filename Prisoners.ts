/*
1,2,3,4,5
There are N prisoners standing in a circle, waiting to be executed. 
The executions are carried out starting with the kth person, 
and removing every successive kth person going clockwise until there is no one left.

Given N and k, 
write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
*/

const solution = (N: number, k: number) => {
    var last_person: number = 0;
    var next_prisoner: number = 0;

    //init array with the length of k
    var prisoners: number[] = Array.from({length: 5}, (_, index) => index + 1);

    while(prisoners.length){
        //find the next prisoner
        next_prisoner = (next_prisoner + k - 1) % prisoners.length;
        last_person = prisoners[next_prisoner]
        //remove the next prisoner
        prisoners.splice(next_prisoner, 1);
    }

    return last_person;
}

console.log(solution(5, 2));