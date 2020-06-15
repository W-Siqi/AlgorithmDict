# hash
这题原做法，就是x+y = sum的sum从遍历到最大。但是这样会超时，因为有的数组会特别短。会踩空。  
后来AC的方法就是，遍历具体数组，x+y为key value直接塞进buckets，最后根据buckets再排序输出res[]