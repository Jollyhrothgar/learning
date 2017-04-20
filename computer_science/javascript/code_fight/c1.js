function digitSumInverse(sum, numberLength) {
    /* 
     * constraints:
     * 2 <= numberLength <= 15
     * 0 <= sum <= 100
     * max_num < pow(10,numberLength)
     * 
     * count all positive integers in range
     * 0 <= x <= pow(10,numberLength) such that
     * the sum of the integers are less than the sum
     */
    
    var count = 0;
    for(var i = 0; i < Math.pow(10,numberLength); i++){
        var digits = String(i);
        var test_sum = 0;
        for(j = 0; j < digits.length; j++){
            // this seems like it could be optimized
            // to peek ahead to see if sum would be 
            // guaranteed to be exceeded.
            sum += Number(digits[j]);
        }
        if( test_sum < sum ){
            count = count + 1;
        }
    }
}
