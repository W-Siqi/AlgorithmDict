# DP 
## 1.0 为什么用DP
这题当时很快就看出是要用DP。 感觉就是规律总结多了，见多了，大脑有反射，而且很强烈且自然。  
具体来说，就是感觉上，数列，排列组合，最优解...这些要素一排，就有种最优子问题的味道了，然后仔细一思考，确实行得通。 
- 启发： sequence，subsequence，找排列最优解，这类问题，基本上是很符合DP的特质的（但其实刷多了，感觉是走在理论前面的）。

## 2.0 当时为什么写了O(mn(m+n))的时间复杂度？
因为我去检查状态的时候，对于dp[i][j]， 我把 d[0~i-1][j] 和 dp[i][0~j-1]都核算了一遍。  
因为我不敢确认，序号大的解一定比序号小的解要更优。 因为我对这里的状态的定义不明确。

## 2.1 状态定义的两种方法
这里dp[i][j]的状态有两种定义法：  
1. 以nums1[i] 和 nums2[j] 为结尾
2. 只考虑nums1前i个 和nums2前j的最优解(即i,j代表问题规模)
### 第一种
如果选择第1种，那么更新dp[i][j]的时候，就要考很多可能的状态。  
这里状态转移十分清晰，然后那些状态要转移就不清楚了。
### 第二种，i,j代表问题规模
其实就是我最后选择的解法（虽然当时我没有意识到）。  

这里的一个好处就是：**很好的保证了，i,j大的比i,j小的要最优**，也就是状态转移的时候不要考虑前面的所有状态


## 3.0 dp[i][j]为规模的通用实质
dp[i][j]代表规模，那么他的最优解有以下几个来源：  
1. 因为新加的元素不争气，就是相邻子问题（dp[i-1][j],dp[i][j-1]）的最优解。
2. 新加入的元素有贡献：考虑新的元素的累加之前的子问题，dp[i-1][j-1] + nums1[i]*nums2[j]
3. 之前子问题的最优太费，直接另起炉灶： nums1[i]*nums2[j]  

### Q:如何解决新的元素nums[i] 和 nums2里面非nums[j]相乘为最优解的情况？通用模板存在漏解？
如果nums1[i]和nums2[k](k < j)是最佳，那么在dp[i][k]的时候就会被考虑进去，然后一路顺承到dp[i][j-1]. 所以那个通用的模板还是完备的


## 初始化
这里要初始化dp[i][0]和dp[j][0] 为0.  
**他们不是有效的状态，但是是有效状态的垫脚石**

## 这题的特殊之处：非空sequence
不考虑新元素，在有个地方是不行的。  
如果dp[i-1][j]之类的，本身就是两个非空sequence，这个时候，就必须让现有的两个相乘。

因为这里我的初始化是吧dp[i][0]设为0，这样是有可能出错了。

## 类似的问题
In May 30 days challenge, today's question is just a variation of this problem.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/

Additional problems you might want to look -
Easy
https://leetcode.com/problems/unique-paths-ii/
https://leetcode.com/problems/unique-paths/

Medium
https://leetcode.com/problems/minimum-path-sum/
https://leetcode.com/problems/longest-common-subsequence/

Hard
https://leetcode.com/problems/edit-distance/