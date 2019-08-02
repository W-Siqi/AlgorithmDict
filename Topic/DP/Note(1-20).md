# 1 - Range Sum Query 2D
## a) range sum 的 trick： 
s(i,j) 为 从0,0 到i, j 的累加和  
sum（x1,y1,x2,y2）= s（x2,y2）- s(x2,y1-1) - s(x1-1,y2)+s(x1-1,y1-1)  
## b) 经典的2D grid 规划  
下标从小到大这样遍历过去就行了，对于i,j时，任何下标小于i-1，i-2... 和 j-1，j-2,j-3...都可以利用
```
for(int i=0;...){
    for(int j;...){

    }
}
```