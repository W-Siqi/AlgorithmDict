# 关于坐标变换
## 矩阵的坐标x,y
- 物理的存储上，x代表line，y代表row。   
- 逻辑上，看成2个维度，没有什么横竖关系..

## 坐标变换
- x，y 换符号的是镜像变换
- x，y互换，是绕着y=x这个线进行对称
- 旋转90度，或者x度，就用图形学的复数，或者用参数坐标自己推矩阵

## 这题矩阵旋转
### 方案1
变换到坐标中心，用旋转矩阵或者负数来进行旋转
### 方案2（solution的方案）
四个角为一轮旋转，直接枚举之间的而关系
### 方案3
先转置（颠倒x，y），再把每一行reverse

# solution
```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int base = 0;
        while(base < n/2){
            for(int i = base; i < n- base - 1;i++){
                int temp = matrix[i][n-base-1];
                matrix[i][n-base-1] = matrix[base][i];
                int temp2 = matrix[n-base-1][n-i-1];
                matrix[n-base-1][n-i-1] = temp;
                int temp3 = matrix[n-i-1][base];
                matrix[n-i-1][base] = temp2;
                matrix[base][i] = temp3;
            }
            base++;
        }
    }
};
```