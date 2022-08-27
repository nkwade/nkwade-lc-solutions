

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int start = 0;
    int sum;
    numbersSize--;
    *returnSize = 2;
    int* p = (int*) malloc(2 * sizeof(int));
    while(start<numbersSize) {
        sum = numbers[start]+numbers[numbersSize];
        if(sum == target) {
            p[0]= start+1;
            p[1]= numbersSize+1;
            return p;
        }
        else if(sum<target) {
            start++;
        }
        else {
            numbersSize--;
        }
    }
    return p;
}