

int maxProfit(int* prices, int pricesSize){
    int l = 0;
    int res = 0;
    
    for (int r = 1; r < pricesSize; r++) {
        if (prices[r] - prices[l] > res) {
            res = prices[r] - prices[l];
        }
        if (prices[r] < prices[l]) {
            l = r;
        }
    }
    
    return res;
}